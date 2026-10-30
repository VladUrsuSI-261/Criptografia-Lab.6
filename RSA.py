import hashlib

message = "Ursu Vlad SI-261"

hash_val = int(hashlib.sha256(message.encode()).hexdigest(), 16)

p = 61
q = 53

n = p * q
phi = (p - 1) * (q - 1)

e = 17

d = pow(e, -1, phi)

print("Cheia publica:")
print("e =", e)
print("n =", n)

print("\nCheia privata:")
print("d =", d)

print("\nHash:")
print(hash_val)

signature = pow(hash_val, d, n)

print("\nSemnatura:")
print(signature)

verified = pow(signature, e, n)

print("\nVerificat:")
print(verified)

if verified == hash_val % n:
    print("\nSemnatura valida")
else:
    print("\nSemnatura invalida")
    