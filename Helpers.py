from math import *

def next_vowel(inp):
    vowels = ["a", "e", "i", "o", "u"]
    if inp.lower() in "aeiou":
        if inp.islower():
            x = vowels.index(inp)
            x += 1
            x = (x % 5)
            return vowels[x]
        elif inp.isupper():
            x = vowels.index(inp.lower())
            x += 1
            x = (x % 5)
            return vowels[x].upper()
    else:
        return inp


def next_letter(char):
    int_val = ord(char)
    if int_val in range(65, 91):
        int_val += 1
        chr_val = chr(65 + ((int_val - 65) % 26))
        return chr_val
    elif int_val in range(97, 123):
        int_val += 1
        chr_val = chr(97 + ((int_val - 97) % 26))
        return chr_val
    else:
        return chr(int_val)
