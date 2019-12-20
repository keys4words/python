#inheritance - abstract class
#realization - interface

class A:
    def fn(self):pass

class B(A): pass

b = B()
b.fn()

#association:
#   aggregation - objects live independantly
class C:
    def __init__(self, obj):
        self.obj = obj
    def call_fn(self):
        self.obj.fn()

a = A()
c = C(a)
c.call_fn()

#   composition - objects live simultaneously
class D:
    def __init__(self):
        self.obj = A()
    def call_fn(self):
        self.obj.fn()

d = D()
d.call_fn()

