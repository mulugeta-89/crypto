from ecdsa import SigningKey, SECP256k1
sk = SigningKey.generate(curve=SECP256k1)
print(sk)

vk = sk.verifying_key
print(vk)
signature = sk.sign(b"not your keys, not your coins")

assert vk.verify(signature, b"not your keys, not your coins")
print("If this runs, I have signed and validated a message")