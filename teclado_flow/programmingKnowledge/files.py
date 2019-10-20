# fh = open('demo.txt', 'a')
#
# # fh.write('Maximus wins!\nAgain!')
#
# try:
#     for i in range(10):
#         fh.write('this is line number %d\n' % (i+1))
# finally:
#     fh.close()

with open('C:\\Users\\keys4.000\\Documents\\4git\\python\\teclado_flow\\demo.txt', 'w') as fh:
    for i in range(10):
        fh.write('this is line number %d\n' % (i+1))
