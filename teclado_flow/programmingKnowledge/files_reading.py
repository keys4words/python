# fh = open('demo.txt')
#
# # print(fh.readlines()[9])
# # print(fh.readline())
# for line in fh:
#     print(line.split(' '))
#
# fh.close()

with open('demo.txt', 'r') as f:
    for line in f:
        print(line.split(' '))