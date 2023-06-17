'''x & 29 ≠ 0 → (x & 12 = 0 → x & А ≠ 0)'''
def f(x, a):
    return(x & 29 != 0) <= ((x & 12 == 0) <= (x & a != 0))
for a in range(0, 100):
    if all(f(x, a) for x in range(0, 10000)):
        print(a)
        break