import os
from cryptography.fernet import Fernet

files = []
folders = []


class Encrypt:
    def __init__(self):
        self.key = ""
        return
        ## SELECT FOLDER ##

    def selectfolder(self):
        folder = input("Subdirectorios que se vayan a encriptar")
        return folder

    ## GENERATE KEY ##
    def generatekey(self):
        key = Fernet.generate_key()
        with open("thekey.key", "wb") as thekey:
            thekey.write(key)
        return key,print("key generated")

    ## READKEY ##
    def readkey(self):
        with open("thekey.key", "rb") as key:
            secret_key = key.read()
        return secret_key

    ## FIND FILEs ##
    def findFiles(self, folderin):

        for file in os.listdir():
            if file == "main.py" or file == "thekey.key":
                continue
            if os.path.isfile(file):
                files.append(file)
            else:
                if file == folderin:
                    folders.append(file)

        for folder in folders:
            if folder == folderin:
                os.chdir(os.path.join(os.path.dirname(__file__), folder))
                for file in os.listdir():
                    print(os.getcwd())
                    print(file)
                    files.append(file)
        os.chdir(os.path.join(os.path.dirname(__file__), "."))
        print("working directory", os.getcwd())
        print("files", files)
        print("folders", folders)
        return files, folders

    def encrypt(self, files, folderin, key):
        ## ENCRYPT ##

        for file in os.listdir():
            for filel in files:
                if file == filel:
                    with open(file, "rb") as the_file:
                        contents = the_file.read()
                    contents_encrypted = Fernet(key).encrypt(contents)
                    with open(file, "wb") as the_file:
                        the_file.write(contents_encrypted)
        os.chdir(os.path.join(os.path.dirname(__file__), folderin))
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

        os.chdir(os.path.join(os.path.dirname(__file__), '.'))
        print(os.getcwd())
        return print("files encripted")

    def decrypt(self, files, folderin, key):

        ## DECRYPT ##
        for file in os.listdir():
            for filel in files:
                if file == filel:
                    with open(file, "rb") as the_file:
                        contents = the_file.read()
                    contents_decrypted = Fernet(key).decrypt(contents)
                    with open(file, "wb") as the_file:
                        the_file.write(contents_decrypted)
        os.chdir(os.path.join(os.path.dirname(__file__), folderin))
        print(os.getcwd())

        for file in os.listdir():
            print(file)
            for filel in files:
                if file == filel:
                    print("entra")
                    with open(file, "rb") as the_file:
                        print(contents)
                        contents = the_file.read()
                    contents_decrypted = Fernet(key).decrypt(contents)
                    with open(file, "wb") as the_file:
                        the_file.write(contents_decrypted)

        return print("files decripted")
#TODO create Encryptonefile,Decryptonefile
#TODO create Encrypttext,Decrypttext
subidr="files"
key=Encrypt.generatekey()
files,folders=Encrypt.findFiles(subidr)
Encrypt.encrypt(files=files,folderin=subidr,key=key)