from Crypto.Util.number import *
from Crypto import Random
import Crypto
import libnum
from random import randint
import hashlib

bits = 60
msg = "Hello"

q = getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
alpha = 2
Xa = randint(0, q - 1)
k = getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

q, alpha, Xa, k, = 19, 10, 16, 5   # if you want to program work randomly delete this line and if, want to check other examples change numbers.

Ya = pow(alpha, Xa, q)
k_1 = (libnum.invmod(k, q - 1))
D = int.from_bytes(hashlib.sha256(msg.encode()).digest(), byteorder='big' )


S_1 = pow(alpha, k, q)
S_2 = ((D - Xa * S_1) * k_1) % (q - 1)

v_1 = (pow(Ya, S_1, q) * pow(S_1, S_2, q)) % q
v_2 = pow(alpha, D, q)


print("Message: %s " % msg)
print("alpha: %s" % alpha)
print("q: %s" % q)
print("\nYa: %s" % Ya)
print("k: %s" % k)
print("\nXa: %s" % Xa)
print("\nS_1= %s" % S_1)
print("S_2=%s" % S_2)
print("\nV_1=%s" % v_1)
print("v_2=%s" % v_2)
