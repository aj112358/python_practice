# Exercise 174:

# a,b are positive integers
def compute_gcd(a, b):

    if b == 0:
        return a

    c = a % b
    return compute_gcd(b, c)


p, q = list(map(int, input("What numbers to compute gcd of: ").split()))
gcd = compute_gcd(p, q)
print(f"The gcd of {p} and {q} is: {gcd}")
