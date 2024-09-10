# MRO - Method Resolution Order.

class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 5


class D(B, C):
    num = 8


print(D.mro())
print(D.num)
