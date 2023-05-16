# reference: https://realpython.com/python-practice-problems/

from caesarcipher import CaesarCipher

cipher = CaesarCipher('abcd xyz',
  offset=4)

print(cipher.encoded)