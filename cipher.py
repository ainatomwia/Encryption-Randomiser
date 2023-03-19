import random
import string

def selectionMenu():
    # Show welcome message and show available options
    print('\nWelcome to the phrase encrypter/decrypter')

    response = input('Do you want to encrpy or decrypt? [e/D] ').lower()
    if response == 'e':
        word_enc = input('What is the word you want to encrypt?: ').lower()
        encryption_func(word_enc)
    elif response == 'd':
        word_dec = input('What is the word you want to decrypt?: ')
        key = input("What is the decryption key? ")
        decryption_func(word_dec, key)

    else:
        print("Please enter 'e' or 'd'.")
        selectionMenu()

def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

def encryption_func(word_enc):
    split_enc = list(word_enc)

    empty_enc = ""
    de_randomiser = ""
    for x in range(0, len(split_enc)):
         enc_random = random.randint(0,9)
         de_randomiser += str(enc_random)

         empty_enc += random_char(enc_random).lower()
         empty_enc += word_enc[x]

    print('This is your encrypted string:', empty_enc)
    print('This is your decryption code:', de_randomiser)     

def decryption_func(word_dec, key):
    true_key = -1
    dec_word_output = ''
    for x in range(0,len(key)):
        true_key = true_key + int(key[x]) + 1
        dec_word_output += word_dec[true_key]

    print(dec_word_output)

          

selectionMenu()