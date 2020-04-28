class EvenLengthMixin:
    def even_len(self):
        return len(self)%2 == 0

class MyList(list, EvenLengthMixin):
    pass

print(MyList.mro())
x = MyList([1, 2, 3])
print(x)
# x.extend([1, 2, 3, 4])
print(x.even_len())
x.append(6)
print(x.even_len())