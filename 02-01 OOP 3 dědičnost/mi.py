# jen testování složité dědičnosti, neřešte
# mi = multiple inheritance

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass