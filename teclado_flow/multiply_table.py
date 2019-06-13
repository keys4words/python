a, b, c, d = int(input()), int(input()), int(input()), int(input())
first_line = '\t'
for j in range(c, d+1):
    first_line += str(j)
    if j != d:
        first_line += '\t'
    else:
        print(first_line)
for i in range(a, b+1):
    line = str(i) + '\t'
    for j in range(c, d+1):
        line += str(i*j)
        if j != d:
            line += '\t'
        else:
            print(line)
