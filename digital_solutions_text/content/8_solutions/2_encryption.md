# Encryption Exercises

## Caesar Cipher

### Caesar Encryption

``` python
def encrypt_caesar(plaintext, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for character in plaintext:
        if character.isalpha():
            position = alphabet.find(character.upper())
            new_position = (position + shift) % 26
            result = result + alphabet[new_position]
        else:
            result = result + character

    return result
```

### Caesar Decryption

``` python

def decrypt_caesar(ciphertext, shift):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for character in ciphertext:
        if character.isalpha():
            position = alphabet.find(character.upper())
            new_position = (position - shift + 26) % 26
            result = result + alphabet[new_position]
        else:
            result = result + character

    return result
```

## Vigenère

### Vigenère Encryption

``` python
def encrypt_vigenere(plaintext, keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = plaintext.upper()
    keyword = keyword.upper()
    
    result = ""
    keyword_length = len(keyword)
    
    for i in range(len(plaintext)):
        character = plaintext[i]
        
        if character.isalpha():
            shift_char = keyword[i % keyword_length]
            shift = alphabet.find(shift_char) + 1
            char_position = alphabet.find(character)
            new_position = (char_position + shift) % 26
            result = result + alphabet[new_position]
        else:
            result = result + character

    return result
```

### Vigenère Decryption

``` python
def decrypt_vigenere(ciphertext, keyword):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ciphertext.upper()
    keyword = keyword.upper()
    
    result = ""
    keyword_length = len(keyword)
    
    for i in range(len(ciphertext)):
        character = ciphertext[i]
        
        if character.isalpha():
            shift_char = keyword[i % keyword_length]
            shift = alphabet.find(shift_char) + 1
            char_position = alphabet.find(character)
            new_position = (char_position - shift + 26) % 26
            result = result + alphabet[new_position]
        else:
            result = result + character

    return result
```