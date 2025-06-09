import re


text = "Ngày tháng sinh của tôi là 14/04/2006 và 30/02/2006"
patten = r"\d{2}/\d{2}/\d{4}"
"""
    \d: là kí hiệu của số
    \d{2}: là tìm số có 2 chữ số 
    /: là kí tự ở giữa các số (nếu ngày sinh là 14-04-2006 thì sẽ thay '/' thành '-')
""" 

date = re.findall(patten, text)
"""
    findall(sub, s): tìm kiếm trong xâu s, những xâu con thỏa điều kiện của sub.
"""

print("Ngay sinh cua toi la:", date)
text1 = "Email của tôi là quanitk10@gmail.com"
patten1 = r'\b[\w.-]+@[\w.-]+\.\w+\b'

"""
    []:  Bắt đầu một chuỗi kí tự.
    [\w.-]: trong một chuỗi kí tự này có thể có chữ, '.' hoặc '-' (username).
    '@': bắt buộc phải có kí tự '@' trong email
    \.: (.com, .hcmus): vì '.' là một kí tự đặc biệt trong re nên là nếu muốn dùng thì phải thêm \
    \w+: có nghĩa là nhiều chứ liên tiếp nhau (= \w\w\w...)
    \b: có nghĩa là ranh giới từ, vd \bcat\b : là tìm những từ trong xâu có từ cat đứng một mình => cat, \bcat: là tìm những từ trong xâu có từ cat bắt đầu => cation
"""


email = re.search(patten1, text1)   
if email:
    print("Mail: ", email.group())
    


"""
    search(sub, s): kiểm tra xem trong xâu s có xâu con nào khớp với sub hay không.
    Nếu có thì dùng .group() để xuất ra.
"""