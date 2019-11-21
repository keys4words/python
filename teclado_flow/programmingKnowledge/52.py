def add(x, y):
    sum = x+y
    return sum

def main():
    x = int(input("Num 1: "))
    y = int(input("Num 2: "))
    z = add(x, y)
    print(z)

if __name__=="__main__":
    main()