from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify


message = b'I love cryptography!'

private_key = RSA.generate(1024)
public_key = private_key.publickey()

private_pem = private_key.export_key().decode()
public_pem = public_key.export_key().decode()


with open("private.pem", 'w') as pr:
    pr.write(private_pem)

with open("public.pem", 'w') as pu:
    pu.write(public_pem)

# with open("private.pem", 'r') as pr:
#     print(pr.read())
# with open("public.pem", 'r') as pu:
#     print(pu.read())

pr_key = RSA.import_key(open("private.pem", 'r').read())
pu_key = RSA.import_key(open("public.pem", 'r').read())
print(type(pr_key), type(pu_key))
cipher = PKCS1_OAEP.new(key=pu_key)
cipher_text = cipher.encrypt(message)

cipher = PKCS1_OAEP.new(key=pr_key)
decrypted_text = cipher.decrypt(cipher_text)
print(cipher_text)
print(decrypted_text)
print("done")