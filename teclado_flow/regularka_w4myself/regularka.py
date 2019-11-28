import re

# s = 'Это просто строка текста. А это еще одна строка текста.'
s = '''Это просто строка текста.
А это ещё одна строка текста.
А это строка с цифрами: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10, ٢, €, £, ¥, $
А это строка с разными символами: "!", "@", "-", "&", "?", "_"
a\\b\tc
test string'''

# pattern = 'строка'
#traditional methods
# print(s.find(pattern))
# print(pattern in s)

# if re.search(pattern, s):
#     print('Matched')
# else:
#     print('No matched')

# match = re.search(pattern, s)
# print(match.start())
# print(match.end())

# print(re.match(pattern, s))
# print(re.findall(pattern, s))
# print(re.split(r'\.', s, 1))

# pattern = r'\w+'    #только буквы, цифры и знак _ от 1 повтора
# pattern = r'[а-яё0-9]+'    #только буквы, цифры от 1 повтора
# pattern = r'\d+'
# pattern = r'[\d-]+'
# pattern = r'a\\b\tc'

def validate_email(email):
    return bool(re.match(r'^.+@(\w+\.){0,2}[a-z]{2,6}$', email, re.IGNORECASE))

# pattern = r'^\w+'
# print(re.findall(pattern, s, flags=re.IGNORECASE))

print(validate_email('mail@mail.ru'))
print(validate_email('mail@mail'))
print(validate_email('mail@ya.com.infotest'))