import re
import numpy as np
import random
from collections import defaultdict


class Key:
    def __init__(self, word, weight, listDecomp):
        self.word = word
        self.weight = weight
        self.decomp = listDecomp


class Decomp:
    def __init__(self, parts, save, reasmb):
        self.parts = parts
        self.save = save
        self.reasmb = reasmb
        self.used = 0  # để xoay vòng trả lời nếu muốn


class Eliza:
    def __init__(self):
        self.pres = {}
        self.post = {}
        self.synon = defaultdict(list)
        self.key = {}
        self.quit = []
        self.start = ""
        self.end = ""
        self.memory = []  # dùng để lưu tạm phản hồi chưa dùng

    def __load__(self, path):
        decomp = None
        key = None
        with open(path, encoding="utf-8") as file:
            for line in file:
                if ':' not in line:
                    continue
                type, content = line.strip().split(': ', 1)
                if type == "initial":
                    self.start = content
                elif type == "final":
                    self.end = content
                elif type == "quit":
                    self.quit.append(content)
                elif type == "pre":
                    parts = content.split(' ')
                    self.pres[parts[0]] = parts[1]
                elif type == "post":
                    parts = content.split(' ')
                    self.post[parts[0]] = parts[1]
                elif type == "synon":
                    parts = content.split(' ')
                    key_word = parts[0]
                    self.synon[key_word].extend(parts[1:])
                elif type == "key":
                    parts = content.split(' ')
                    word = parts[0]
                    weight = int(parts[1]) if len(parts) > 1 else 1
                    key = Key(word, weight, [])
                    self.key[word] = key
                elif type == "decomp":
                    parts = content.split(' ')
                    save = False
                    if parts[0] == "$":
                        save = True
                        parts = parts[1:]
                    decomp = Decomp(parts, save, [])
                    key.decomp.append(decomp)
                elif type == "reasmb":
                    words = content.strip().split(' ')
                    decomp.reasmb.append(words)

    def __sub__(self, text, sub_table):
        return [sub_table.get(word.lower(), word) for word in text.split()]

    def apply_post(self, words):
        return [self.post.get(w.lower(), w) for w in words]

    def match_decomp_r(self, words, parts, result, cnt):
        if not parts:
            return not words
        if parts[0] == '*':
            for i in range(len(words) + 1):
                sub_result = []
                sub_cnt = [0]
                if self.match_decomp_r(words[i:], parts[1:], sub_result, sub_cnt):
                    result.append(' '.join(words[:i]))
                    result.extend(sub_result)
                    cnt[0] += i + sub_cnt[0]
                    return True
            return False
        elif parts[0].startswith('@'):
            syn_key = parts[0][1:]
            for i in range(1, len(words) + 1):
                if words[i - 1].lower() in self.synon[syn_key]:
                    result.append(words[i - 1])
                    cnt[0] += 1
                    return self.match_decomp_r(words[i:], parts[1:], result, cnt)
            return False
        else:
            if not words or words[0].lower() != parts[0].lower():
                return False
            result.append(words[0])
            cnt[0] += 1
            return self.match_decomp_r(words[1:], parts[1:], result, cnt)

    def match_decomp(self, words, decomp):
        result = []
        cnt = [0]
        if self.match_decomp_r(words, decomp.parts, result, cnt):
            return result, cnt[0]
        return None, None

    def match_key(self, key_obj, words):
        best_match = None
        max_length = -1
        for decomp in key_obj.decomp:
            result, cnt = self.match_decomp(words, decomp)
            if result is not None and cnt > max_length:
                max_length = cnt
                k = np.random.randint(len(decomp.reasmb))
                response = decomp.reasmb[k]
                output = []
                for token in response:
                    if token.startswith('(') and token.endswith(')'):
                        idx = int(token[1:-1])
                        if 0 <= idx < len(result):
                            fragment = result[idx]
                            fragment = self.apply_post(fragment.split())
                            output.extend(fragment)
                    else:
                        output.append(token)
                if decomp.save:
                    self.memory.append(' '.join(output))
                else:
                    best_match = ' '.join(output)
        return best_match, max_length if best_match else None, None

    def check_quit(self, text):
        text = text.strip().lower()
        return text in self.quit

    def respond(self, text):
        text = re.sub(r'[\.,;!?]', '', text)
        words = self.__sub__(text, self.pres)
        keys = [self.key[w.lower()] for w in words if w.lower() in self.key]
        keys.sort(key=lambda k: -k.weight)

        best_response = None
        max_length = -1
        for key in keys:
            response, length, _ = self.match_key(key, words)
            if response and length > max_length:
                max_length = length
                best_response = response

        if best_response:
            return best_response
        if self.memory:
            return self.memory.pop(0)

        # fallback
        xnone = self.key.get('xnone')
        if xnone:
            for decomp in xnone.decomp:
                if decomp.reasmb:
                    k = np.random.randint(len(decomp.reasmb))
                    return ' '.join(decomp.reasmb[k])
        return "Sorry. I don't understand"

# Khởi động
eliza = Eliza()
eliza.__load__('doctor.txt')
print(eliza.start)
while True:
    user_input = input("Bạn: ")
    if eliza.check_quit(user_input):
        print("ELIZA:", eliza.end)
        break
    else:
        print("ELIZA:", eliza.respond(user_input))
