    text = re.sub(r'[\.,;!?]', '', text)
        words = self.__sub__(text, self.pres)
        keys = [self.key[w.lower()] for w in words if w.lower() in self.key]
        keys.sort(key=lambda k: -k.weight)

        best_response = None
        max_length = -1
        for key in keys:
            response, length = self.match_key(key, words)
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