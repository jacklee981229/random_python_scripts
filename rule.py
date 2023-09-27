def apply_encrypt_rule(string):
    # Replace each letter with the letter that comes two positions after it in the alphabet
    result = ''
    for char in string:
        if char.isalpha():
            shifted = chr((ord(char.lower()) - 97 + 2) % 26 + 97)
            result += shifted.upper() if char.isupper() else shifted
        else:
            result += char
    
    # Reverse the order of the resulting string
    result = result[::-1]
    
    return result


def apply_decrypt_rule(string):
    # Reverse the order of the input string
    string = string[::-1]

    # Replace each letter with the letter that comes two positions before it in the alphabet
    result = ''
    for char in string:
        if char.isalpha():
            shifted = chr((ord(char.lower()) - 97 - 2) % 26 + 97)
            result += shifted.upper() if char.isupper() else shifted
        else:
            result += char
    
    return result
