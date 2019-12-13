import re

# regexp = 'a'
# s = 'vasya.A@mail.ru'

# match = re.match(regexp, s)
# print(match.group(0))

# search = re.search(regexp, s)
# print(search.group(0), search.start(), search.end())

# findall = re.findall(regexp, s, re.IGNORECASE)
# print(findall)

# split = re.split('-', '10-20-30-40-50', maxsplit=2)
# print(split)
#
# subn = re.subn('a', 'b', s)
# print(subn)

#предварительное компилирование регулярных выражений для увелчения скорости
# pattern = re.compile(regexp, re.I)
# pattern.match(s)
# pattern.search(s)


s = 'Python Programming for the Absolute Beginner'
# r = re.findall(r'\w+$', s)   #[a-zA-Z0-9] equiv \w

s = 'abc.test@gmail.com'
r = re.findall(r'@\w+.\w+', s)
r1 = re.findall(r'\W', s)   #\w equiv [^a-zA-Z0-9]
r3 = re.findall(r'\.\w+$', s)

s = 'abc  12-1234 12-12-2019, asd 56-4648 01-05-2018, xyz 78-6521 25-09-2019'
r4 = re.findall(r'\d+-(\d+)-\d{4}', s)     #[0-9] equiv \d
r5 = re.search(r'@mail|@gmail|@hotmail|@yandex', s)

print(r4)