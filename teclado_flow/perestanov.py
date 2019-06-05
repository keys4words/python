def generate_numbers(N:int, M:int, prefix=None):
    """"Generate any numbers
        at N-dimensional system
        with length = M"""
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()


def gen_bin(M, prefix=""):
    if M == 0:
        print(prefix)
        return
    for digit in "0", "1":
        gen_bin(M-1, prefix+digit)



# gen_bin(5)
generate_numbers(3, 3)