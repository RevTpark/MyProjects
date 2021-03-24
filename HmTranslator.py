import re
# h stands for . and m stands for -
translations = {'A': 'hm', 'B': 'mhhh', 'C': 'mhmh', 'D': 'mhh', 'E': 'h', 'F': 'hhmh', 'G': 'mmh', 'H': 'hhhh',
                'I': 'hh', 'J': 'hmmm', 'K': 'mhm', 'L': 'hmhh', 'M': 'mm', 'N': 'mh', 'O': 'mmm', 'P': 'hmmh',
                'Q': 'mmhm', 'R': 'hmh', 'S': 'hhh', 'T': 'm', 'U': 'hhm', 'V': 'hhhm', 'W': 'hmm', 'X': 'mhhm',
                'Y': 'mhmm', 'Z': 'mmhh', '0': 'mmmmm', '1': 'hmmmm', '2': 'hhmmm', '3': 'hhhmm', '4': 'hhhhm', '5': 'hhhhh',
                '6': 'mhhhh', '7': 'mmhhh', '8': 'mmmhh', '9': 'mmmmh', '&': 'hmhhh', "'": 'hmmmh', '@': 'hmmhmh', ')': 'mhmmhm',
                '(': 'mhmmh', ':': 'mmmhhh', ',': 'mmhhmm', '=': 'mhhhm', '!': 'mhmhmm', '.': 'hmhmhm', '-': 'mhhhhm', '+': 'hmhmh',
                '"': 'hmhhmh', '?': 'hhmmhh', '/': 'mhhmh'}

# Converts English to 'hm'
def encrypter(string_encrypt):
    # Encrypt string variable
    translated = ''

    for letters in string_encrypt:
        # Search the dict for encrypts of the cipher
        if letters == ' ':
            # Adding / instead of spaces
            translated += '/'
        else:
            # Encoding the words
            translated += translations[letters.upper()] + ' '
    return translated


# Converts 'hm' to English
def cipher(string_cipher):
    raw_text = ''
    # Split text at / for spaces
    not_spaced = string_cipher.lower().split('/')
    for i in range(len(not_spaced)):
        # Capture each word from the sentence by splitting at spaces
        indiv_alpha = not_spaced[i].split()
        for alpha in range(len(indiv_alpha)):
            # Access the dit to reverse search the keys
            for key, values in translations.items():
                # Converting each letter to English
                if indiv_alpha[alpha] == values:
                    # Appending the string with correct English Alphabet
                    raw_text += key
        # Adding spaces after each word
        raw_text += ' '
    return raw_text


def converter(string):
    print("The translated string is: ")
    if (string[0] == 'h' or string[0] == 'h') and (string[-1] == 'm' or string[-1] == 'h'):
        print(cipher(string))
    else:
        print(encrypter(string))


string = input("Enter a code or sentence: ")
converter(string)

