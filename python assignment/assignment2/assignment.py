p = int(input("Enter first value: "))
q = int(input("Enter second value: "))
r = int(input("Enter third value: "))

if p >= q and p >= r:
    print(p, "is the largest number.")
elif q >= p and q >= r:
    print(q, "is the largest number.")
else:
    print(r, "is the largest number.")