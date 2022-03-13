m = int(input("Enter interval m: "))
n = int(input("Enter number n: "))
def krug(n,m):
    yield 1
    for i in range(m-1, n*m, m-1):
        v = i % n + 1
        if v == 1:
            return
        yield v
print(list(krug(n,m)))