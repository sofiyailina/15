'''(X & 13 = 0) → ((X & 40 ≠ 0) → (X & A ≠ 0))'''

def impl(a, b):
    return not a or b

def fn(x, a):
    p1 = x&13 == 0
    p2 = impl(x&40 != 0, x&a != 0)
    return impl(p1, p2)

for a in range(0, 1000):
    test = True
    for x in range(1000):
        if fn(x, a) != True:
            test = False
            break
    if test:
        print(a)
        break