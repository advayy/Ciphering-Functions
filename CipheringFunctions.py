from Helpers import *

# Shifts every single single shift up to the selected number
def print_all_shifts_to(phrase, no_of_shifts):
    x = 0
    shifted = ""
    while x < no_of_shifts:
        for letter in phrase:
            shifted += next_letter(letter)
        print(shifted)
        phrase = shifted
        shifted = ""
        x += 1

# Returns a single shift by the given number of shifts
def shift_by(phrase, no_of_shifts):
    x = 0
    shifted = ""
    while x < no_of_shifts:
        for letter in phrase:
            shifted += next_letter(letter)
        phrase = shifted
        shifted = ""
        x += 1
    return phrase

# Returns a solution to the emperors shift
def solve_emperors_shift(phrase):
    return shift_by(phrase, 5)

# Generates the emperors shift for a given phrase
def create_emperors_shift(phrase):
    return shift_by(phrase, 21)

# Generates the ROT1 shift for a given phrase
def create_rot1_shift(phrase):
    shifted = shift_by(phrase, 1)
    return shifted

# Generates the UASI shift for a given phrase
def uasi_shift(phrase):
    x = 0
    shifted = ""
    while x < 1:
        for letter in phrase:
            shifted += next_vowel(letter)
        phrase = shifted
        x += 1
    return phrase

# Generates the QWERTY shift for a given phrase
def qwerty_shift(phrase):
    qwerty_list = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z",
                   "X", "C", "V", "B", "N", "M"]
    reg_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]
    shifted = ""
    for alphabet in phrase:
        if alphabet.lower() in reg_letters:
            x = reg_letters.index(alphabet.lower())
            p = qwerty_list[x]
        else:
            p = alphabet
        if alphabet.isupper():
            p = p.upper()
        elif alphabet.islower():
            p = p.lower()
        shifted += p
    return shifted

# Inverts the QWERTY shift for a given phrase
def inv_qwerty_shift(phrase):
    qwerty_list = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z",
                   "X", "C", "V", "B", "N", "M"]
    reg_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]
    shifted = ""
    for alphabet in phrase:
        if alphabet.upper() in qwerty_list:
            x = qwerty_list.index(alphabet.upper())
            p = reg_letters[x]
        else:
            p = alphabet
        if alphabet.isupper():
            p = p.upper()
        elif alphabet.islower():
            p = p.lower()
        shifted += p
    return shifted

# Generates the Square Cipher shift for a given phrase
def square_cipher(phrase):
    trimmed_phrase = ""
    for letters in phrase:
        if letters != " ":
            trimmed_phrase += letters

    n = len(trimmed_phrase)

    factors = []
    i = 1
    while i <= n:
        if n % i == 0:
            factors.append(i)
        i += 1

    if len(factors) == 2:  # if the input is a prime number
        trimmed_phrase += "o"
        n = len(trimmed_phrase)
        factors = []
        i = 1
        while i <= n:
            if n % i == 0:
                factors.append(i)
            i += 1

    if len(factors) % 2 == 0:
        n1 = factors[int(ceil((len(factors) / 2)) - 1)]
        n2 = factors[int(ceil((len(factors) / 2)))]
    else:
        n1 = factors[int(ceil((len(factors) / 2)) - 1)]
        n2 = n1

    sq_cipher = ""
    i = 0
    while i <= n2 - 1:
        j = 0
        k = i
        while j <= n1 - 1:
            sq_cipher += trimmed_phrase[k]
            k += n2
            j += 1
        i += 1
    sq_cipher2 = ""
    c = 1
    for letters in sq_cipher:
        sq_cipher2 += letters
        if c % n1 == 0:
            sq_cipher2 += " "
        c += 1

    return sq_cipher2

# Inverts the Square Cipher shift for a given phrase (Requires its characters to be a square)
def inv_square_cipher(phrase):
    return square_cipher(phrase)
