# AES 256 encryption/decryption using pycryptodom library
 
from Crypto.Cipher import AES
import hashlib
import os
import os.path
import chalk
 
class MyEncryptor:
    def __init__(self,key) -> None:
        self.key = key

    def decrypt(self, ciphertext, nonce, tag):

        cipher = AES.new(self.key, AES.MODE_EAX, nonce)

        try:
            plaintext = cipher.decrypt_and_verify(ciphertext,tag)
            return plaintext.rstrip(b"\0")
        except ValueError:
                print(chalk.red("Key incorrect or message corrupted"))
    
    def encrypt(self, data):
        # passing the data we want to encrypt to the encryption mode
        cipher = AES.new(self.key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data)
        return ciphertext, tag, cipher

    def encrypt_file(self, FileName):
      with  open(FileName, 'rb') as fo:
          plaintext = fo.read()

      ciphertext, tag, cipher = self.encrypt(plaintext)
    #creating a new file that is saved with .enc extension
      with open(FileName + ".enc", 'wb') as fo:
          [fo.write(x) for x in (cipher.nonce, tag, ciphertext)]
          fo.close()
    # removing the original file and changing to the encrypted file
    # with ciphertext, nonce and tags    
      os.remove(FileName)             

    def decrypt_file(self, FileName):

        with open(FileName, 'rb') as fo:
            nonce, tag, ciphertext = [ fo.read(x) for x in (16, 16, -1)]
        dec = self.decrypt(ciphertext, nonce, tag)

        # if a wrong value is passed for the ciphertext, nonce and tags it exits
        if(dec == None):
            exit()
        # if values are correct a file is created in a writing mode
        # And decrypted        
        with open(FileName[:-4], 'wb') as fo:
            fo.write(dec)
            fo.close()
        # if decryption is succesful it removes the .enc and returns to original file        
        os.remove(FileName)                

    def getAllFiles(self,mode):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        # I am using exlude to limit os.walk traversal ffrom encrypting specific directories
        exclude = set(['.vscode','extensions','node_modules'])
        dirs = []

        for dirName, subdirList, fileList in os.walk(dir_path, topdown=True):
            subdirList[:] = [d for d in subdirList if d not in exclude]
            for fname in fileList:
        # ensuring no python file or already encrypted file is being encrpted when in the subdirectory
        # and making sure the extension is saved with enc
                if(mode == 'e'):
                    if(fname[-2:] != 'py'and fname[-3:] != 'enc'):
                        dirs.append(dirName + "\\" + fname)
        #Only encrypted files should be decrypted
                elif(mode == 'd'):
                    if(fname[-3:] == 'enc'):
                        dirs.append(dirName + "\\" + fname)
        return dirs                      
        
    def encrypt_all_files(self):
         dirs = self.getAllFiles(mode = 'e')
         for FileName in dirs:
             self.encrypt_file(FileName)
    

    def decrypt_all_files(self):
         dirs = self.getAllFiles(mode = 'd')
         for FileName in dirs:
             self.decrypt_file(FileName)

def generate_key(password):
    key = hashlib.sha256(password.encode('utf-8')).digest()
    return key

clear = lambda: os.system('cls')              

while True:
    password = str(input(chalk.green("Enter encryption / decryption key")))
    repassword = str(input(chalk.green("confirm your key")))

    if (password == repassword):
        enc = MyEncryptor( generate_key(password))
        break
    else:
        print(chalk.red("Key mismatch"))
while True:
    clear()
    choice = int(input(
        chalk.green(
        "1. Press '1' to encrypt all files.\n2. Press '2' to decrypt all files.\n3. Press '3' to exit.\n "    
        )
    )) 
    clear()
    if choice == 1:
        enc.encrypt_all_files()
    elif choice == 2:
        enc.decrypt_all_files()
    elif choice == 3:
        exit() 
    else:
        print("please select a valid option")