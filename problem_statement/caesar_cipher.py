# reference: https://realpython.com/python-practice-problems/

# from caesarcipher import CaesarCipher

# cipher = CaesarCipher('abcd xyz',
#   offset=4)

# print(cipher.encoded)

def caesar(str , offset):

    for i in str:
        # need to refactor the code
        char = chr(ord(i)+offset)
        print(char, end='')

caesar("abcd xyz", 4)        


