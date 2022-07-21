#!/usr/bin/python3

# imports
from   os                  import urandom
from   Crypto.Cipher       import AES
from   cryptography.fernet import Fernet
from   colorama            import Fore
import pyaes
import pyAesCrypt
import bcrypt
import argparse

# Colors
err   = Fore.RED
green = Fore.GREEN
blue  = '\033[1;34;40m'
rst   = Fore.RESET

# Argument Parser
parser = argparse.ArgumentParser(description="Syntax: Krax.py [-f/--passwd/--str <string/file/password>] [-E / -D --key <key>] [--aes (optional)]")
parser.add_argument("--aes",    action='store_true', help="Enable AES encryption\n")
parser.add_argument("-f",       metavar='',          help="File to Encrypt or Decrypt [-f Important.txt]\n")
parser.add_argument("--key",    metavar='',          help="Provied the key [--key TheKeyis123] \n")
parser.add_argument("--str",    metavar='',          help="Encrypt a string [--str 'ThisWillBeEncrypted']\n")
parser.add_argument("-E",       action='store_true', help="encryption <-E>\n")
parser.add_argument("-D",       action='store_true', help="decryption <-D>\n")
parser.add_argument("--passwd", metavar='',          help="Hash a password <--passwd>\n")
args = parser.parse_args()

# Password Encryption
def password(passwd):

    # Generating Salt & Encrypting Password
    salt = bcrypt.gensalt(5)
    encrypted_passwd = bcrypt.hashpw(passwd.encode('utf-8'), salt)

    # Printing Results
    print(blue + "[HASHER] > "+rst, end='')
    print("Orignal_Passwd   => ", green + f"[{passwd}]" + rst)
    print(blue + "[HASHER] > "+rst, end='')
    print("Encrypted_Passwd => ", green + f"[{encrypted_passwd.decode()}]" + rst)
    print(blue + "[HASHER] > "+rst, end='')
    print("SALT => ", green + salt.decode('utf-8') + rst)

# File Encryption
def FileE(file):
    try:
        # Generate Key
        K = Fernet.generate_key()
        Fur = Fernet(K)

        # Open file and Store the content in a variable
        with open(file, 'rb') as U_fl:
            Content = U_fl.read()

        # Encrypt the Content
        Enc = Fur.encrypt(Content)

        # Rewrite the encrypted content in the file
        with open(file, 'wb') as E_fl:
            E_fl.write(Enc)

        # Printing Results
        print(blue + "[HASHER] > " + rst, end='')
        print("Encrypted => ", green + f"{file}" + rst)
        print(blue + "[HASHER] > " + rst, end='')
        print("KEY       => ", green + f"{K.decode()}" + rst)

    # If file does not exists
    except FileNotFoundError:
        print(err + f'[ERROR] > File_Not_Found ({file})' + rst)

# File Decryption
def FileD(file, key):
    try:
        # Store the Key
        DecKey = Fernet(key)

        # Open the file and save the content in a variable
        with open(file, 'rb') as E_fl:
            Cont = E_fl.read()

        # Decrypt the stored content
        Dec = DecKey.decrypt(Cont)

        # Rewrite the decrypted content to the file
        with open(file, 'wb') as FileX:
            FileX.write(Dec)

        # Print Results
        print(blue + "[HASHER] > " + rst, end='')
        print("Decrypted => ", green + f"{file}" + rst)
        print(blue + "[HASHER] > " + rst, end='')
        print("KEY       => ", green + f"{key}" + rst)

    # If file does not exists
    except FileNotFoundError:
        print(err + f'[ERROR] > File_Not_Found ({file})' + rst)

# File Encryption (AES)
def AesFl(Fnm):
    try:
        # Generate key
        K = Fernet.generate_key()

        # Read Content & Encode
        Con = Fnm.read()
        key = K.encode('utf-8')

        # Encrypt Text
        aes = pyaes.AESModeOfOperationCTR(key)
        ciphertext = aes.encrypt(Con)

        # Print Results
        print(blue + "[HASHER] > " + rst, end='')
        print("AES_ENCRYPTED => ", green + f"{Fnm}" + rst)
        print(blue + "[HASHER] > " + rst, end='')
        print("KEY_X         => ", green + f"{K}" + rst)
        print(blue + "[HASHER] > " + rst, end='')

    # If file does not exists
    except FileNotFoundError:
        print(err + f'[ERROR] > File_Not_Found ({file})' + rst)

# String Encryption
def estr(string):

    # Generate key
    K = Fernet.generate_key()
    Fur = Fernet(K)

    # Encrypt String
    Enc = Fur.encrypt(string)

    # Print results
    print(blue + "[HASHER] > " + rst, end='')
    print("Encrypted => ", green + f"{Enc.decode()}" + rst)
    print(blue + "[HASHER] > " + rst, end='')
    print("KEY       => ", green + f"{K.decode()}" + rst)

# String Encryption (AES)
def aestr(string):

    # Generate key
    K = Fernet.generate_key()
    Fur = Fernet(K)

    # Encrypt String
    Enc = Fur.encrypt(string)

    # Print results
    print(blue + "[HASHER] > " + rst, end='')
    print("Encrypted => ", green + f"{Enc.decode()}" + rst)
    print(blue + "[HASHER] > " + rst, end='')
    print("KEY       => ", green + f"{K.decode()}" + rst)

# String Decryption
def dstr(str, key):

    # Set the key & decrypt
    dk = Fernet(key)
    dstrx = dk.decrypt(str)

    # Print results
    print(blue + "[HASHER] > " + rst, end='')
    print("Decrypted => ", green + f"{dstrx.decode()}" + rst)
    print(blue + "[HASHER] > " + rst, end='')
    print("KEY       => ", green + f"{key}" + rst)

# String Decryption (AES)
def aesdstr(str, key):

    # Set the key & decrypt
    dk = Fernet(key)
    dstrx = dk.decrypt(str)

    # Print results
    print(blue + "[HASHER] > " + rst, end='')
    print("Decrypted => ", green + f"{dstrx.decode()}" + rst)
    print(blue + "[HASHER] > " + rst, end='')
    print("KEY       => ", green + f"{key}" + rst)

# Filtering Arguments and error Handling
if __name__=='__main__':
    try:
        if args.passwd:
            p = args.passwd
            password(p)

        elif args.f and args.E:
            Fl_nm = args.f
            FileE(Fl_nm)

        elif args.f and args.D and args.key or args.f and args.key and args.D:
            Fl_nm = args.f
            KEY   = args.key
            FileD(Fl_nm, KEY)

        elif args.f and args.aes and args.E or args.f and args.E and args.aes:
            FileT = args.f
            AesFl(FileT)

        elif args.f and args.aes and args.D and args.key or args.f and args.aes and args.key and args.D:
            Fl_nm = args.f
            KEY   = args.key
            FileD(Fl_nm, KEY)

        elif args.str and args.E:
            str = args.str
            estr(str.encode('utf-8'))

        elif args.str and args.E and args.aes or args.str and args.aes and args.E:
            str = args.str
            estr(str.encode('utf-8'))

        elif args.str and args.D and args.key or args.str and args.key and args.D:
            str = args.str
            kEy = args.key
            dstr(str.encode('utf-8'), kEy)

        elif args.str and args.D and args.aes and args.key or args.str and args.key and args.D and args.aes:
            str = args.str
            Gxk = args.key
            aesdstr(str.encode('utf-8'), Gxk)

        else:
            print(err + f'[ERROR] > Invalid set of arguments provided' + rst)

    except AttributeError:
        print(err + "[E] Attribute Error" + rst)

    except IsADirectoryError:
        print(err + "[E] Cannot encrypt a directory" + rst)

    except KeyboardInterrupt:
        print(err + "[INTERRUPT] Quitting" + rst)
