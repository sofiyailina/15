def ДЕЛ(x, A):
    return x % A == 0

for A in range(1, 1000):
    for x in range(1, 1000):
        if not ((ДЕЛ(x, 6) <= (not ДЕЛ(x, 14))) or (x + A >= 70) and ДЕЛ(A, 20)):
            break
    else:
        print(A)
        break