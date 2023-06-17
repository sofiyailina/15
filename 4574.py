p = (55, 80)
q = (20, 105)

'''(x ∈ Q) → ( ((x ∈ P) ≡ (x ∈ Q)) ∨ (¬(x ∈ P) → (x ∈ A)) )
'''
def f(x, a):
    return (x in q) <= (((x in p) == (x in q)) or (not(x in p) <= (x in a)))

for a in range(0, 100):
    if all(f(x, a) for x in range(0, 10000)):
        print(a)
        break