import hashlib

name = "Mulugeta Hailegnaw"
name2 = "mulugeta Hailegnaw"

print("the original name ", name)
print("The original name2", name2)

hashName = hashlib.sha256(name.encode())
hashName2 = hashlib.sha256(name2.encode())
print("the hash of name is ", hashName.hexdigest())
print("The hash of name2 is ", hashName2.hexdigest())