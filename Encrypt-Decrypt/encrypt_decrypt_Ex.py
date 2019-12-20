import os
import random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

def encrypt(key,filename):
    chunksize = 64 * 1024
    outputFile = "(encrypted)"+filename
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = ''
    for i in range(16):
        IV +=chr(random.randint(0,0xFF))
    encryptor = AES.new(key,AES.MODE_CBC,IV)
    with open(filename,"rb") as infile:
        with open(outputFile,"wb") as outfile:
            outfile.write(filesize)
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 !=0:
                    chunk +=' '*(16-(len(chunk) % 16))
                outfile.write(encryptor.encrypt(chunk))
def decrypt(key,filename):
    chunksize = 16 * 1024
    outputFile= filename[11:]
    with open(filename,"rb") as infile:
        filesize = long(infile.read(16))
        IV = infile.read(16)
        decryptor = AES.new(key,AES.MODE_CBC,IV)
        with open(outputFile,"wb") as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)
def get_key(password):
    hasher = SHA256.new(password)
    return hasher.digest()
def main():
    choice = raw_input("Would you like to Encrypt/Decrypt?")
    if choice == 'E':
        filename = raw_input("File is encrypt:")
        password = raw_input("password:")
        encrypt(get_key(password),filename)
        print "Done"
    elif choice == "D":
        filename = raw_input("File is encrypt:")
        password = raw_input("password:")
        decrypt(get_key(password),filename)
        print "Done"
    else:
        print "No option selected ...Closing..."
if __name__ == '__main__':
    main()
####################################################################################
# from Crypto.Cipher import AES
# import os
# import sys
# import base64

# def encryption(privateInfo):
#     BLOCK_SIZE = 16
#     PADDING = '{'
#     pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
#     print "-------pad-------",pad
#     EncodeAES = lambda c,s : base64.b64encode(c.encrypt(pad(s)))
#     print "--------EncodeAES-------",EncodeAES
#     secret = os.urandom(BLOCK_SIZE)
#     print "Encrypt Key is :",secret

#     cipher = AES.new(secret)
#     encoded = EncodeAES(cipher,privateInfo)
#     print "Encoded Stirng:",encoded
# encryption("Secret message that is very sensitive and even the governant!")

# def decryption(encryptedString):
#     PADDING = '{'
#     DecodeAES = lambda c,e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
#     
#     cipher = AES.new(key)
#     decode = DecodeAES(cipher,encryptedString)
#     print "Decoded String:",decode
# decryption('ZqeQaXoik6ZERxlf0r9qa7/jFRqXFGI82nueivSWOW7/DVqAHPpWRrndG7KvTMqiWC7Ie0d8AEH/ndYbUIBHtQ==')

#######################################################################################
# # Transposition Cipher Encrypt/Decrypt File

# # http://inventwithpython.com/hacking (BSD Licensed)

# import time, os, sys, transpositionEncrypt, transpositionDecrypt
# from Crypto.Cipher import AES

# def main():

#     inputFilename = 'frankenstein.txt'

#     #BE CAREFUL! If a file with the outputFilename name already exists,

#     # this program will overwrite that file.

#     outputFilename = 'frankenstein.encrypted.txt'

#     myKey = 10

#     myMode = 'encrypt' # set to 'encrypt' or 'decrypt'
#     # If the input file does not exist, then the program terminates early.

#     if not os.path.exists(inputFilename):
#         print('The file %s does not exist. Quitting...' % (inputFilename))
#         sys.exit()
#     # If the output file already exists, give the user a chance to quit.
#     if os.path.exists(outputFilename):

#         print('This will overwrite the file %s. (C)ontinue or (Q)uit?' % (outputFilename))

#         response = input('> ')

#         if not response.lower().startswith('c'):

#             sys.exit()
#     # Read in the message from the input file

#     fileObj = open(inputFilename)

#     content = fileObj.read()

#     fileObj.close()
#     print('%sing...' % (myMode.title()))

#     # Measure how long the encryption/decryption takes.
#     startTime = time.time()

#     if myMode == 'encrypt':

#         translated = transpositionEncrypt.encryptMessage(myKey, content)

#     elif myMode == 'decrypt':

#         translated = transpositionDecrypt.decryptMessage(myKey, content)

#     totalTime = round(time.time() - startTime, 2)
#     print('%sion time: %s seconds' % (myMode.title(), totalTime))

#     # Write out the translated message to the output file.

#     outputFileObj = open(outputFilename, 'w')

#     outputFileObj.write(translated)

#     outputFileObj.close()

#     print('Done %sing %s (%s characters).' % (myMode, inputFilename, len(content)))
#     print('%sed file is %s.' % (myMode.title(), outputFilename))

#     # If transpositionCipherFile.py is run (instead of imported as a module)

#     # call the main() function.

# if __name__ == '__main__':

#     main()