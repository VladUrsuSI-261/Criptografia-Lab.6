import hashlib
import random
from math import gcd

message = "Ursu Vlad SI-261"

h = int(hashlib.sha256(message.encode()).hexdigest(), 16)

p = 467
g = 2

x = random.randint(1, p - 2)

y = pow(g, x, p)

while True:
    k = random.randint(2, p - 2)
    if gcd(k, p - 1) == 1:
        break

r = pow(g, k, p)

k_inv = pow(k, -1, p - 1)

s = (k_inv * (h - x * r)) % (p - 1)

print("Semnatura:")
print("r =", r)
print("s =", s)

left = pow(g, h, p)
right = (pow(y, r, p) * pow(r, s, p)) % p

print("\nVerificare:")

if left == right:
    print("Semnatura valida")
else:
    print("Semnatura invalida")
    