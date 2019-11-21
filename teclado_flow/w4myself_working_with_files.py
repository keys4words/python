f = open('file.txt', 'r', encoding='utf-8')

# text = f.read()
# lines = ['новая строка 1', 'новая строчка 2']
# # for i in lines:
# #     f.write(i + '\n')
# f.writelines(f'{i}\n' for i in lines)

for line in f:
    print(line, end='')

f.close()

# print(text)