def f(x, a):
    return((x & 42 != 0) or (x & 13 != 0 )) <= ((x & 30 == 0) <= (x & a != 0))
for a in range(0, 100):
    if all(f(x, a) for x in range(0, 10000)):
        print(a)
        break
