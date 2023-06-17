p = {1, 2, 3, 4, 5, 6}
q = {3, 5, 15}

for x in range(1, 1000):
    if not (1) <= ((not(x in p) and (x in q)) or (not(x in q))):
        print(x)
