import string

def apply_encrypt_rule(data):
    # Convert the input string to a list of bytes
    byte_list = bytearray(data.encode())

    # Perform encoding using chatGPT-666 rule
    for i in range(len(byte_list)):
        byte_list[i] = ((byte_list[i] << 2) & 0xFC) | ((byte_list[i] >> 6) & 0x03)
        byte_list[i] = ((byte_list[i] << 4) & 0xF0) | ((byte_list[i] >> 4) & 0x0F)
        byte_list[i] = ((byte_list[i] << 1) & 0xFE) | ((byte_list[i] >> 7) & 0x01)

    # Convert the encoded byte list to a hexadecimal string
    hex_string = byte_list.hex()

    return hex_string

def apply_decrypt_rule(data):
    # Convert the input hexadecimal string to a byte list
    byte_list = bytearray.fromhex(data)

    # Perform decoding using chatGPT-666 rule
    for i in range(len(byte_list)):
        byte_list[i] = ((byte_list[i] >> 1) & 0x7F) | ((byte_list[i] << 7) & 0x80)
        byte_list[i] = ((byte_list[i] >> 4) & 0x0F) | ((byte_list[i] << 4) & 0xF0)
        byte_list[i] = ((byte_list[i] >> 2) & 0x3F) | ((byte_list[i] << 6) & 0xC0)

    # Convert the decoded byte list to a string
    decoded_string = byte_list.decode()

    return decoded_string

def encrypt():
    """
    Get input from user and encrypt it.
    """
    print("Please enter the text to encrypt:")
    user_input = input()
    encrypted_text = apply_encrypt_rule(user_input)
    print(f"Encrypted text: {encrypted_text}")

def decrypt():
    """
    Get input from user and decrypt it.
    """
    print("Please enter the text to decrypt:")
    user_input = input()
    decrypted_text = apply_decrypt_rule(user_input)
    print(f"Decrypted text: {decrypted_text}")

def main():
    """
    Main function to provide user options.
    """
    print("Welcome to the encryption and decryption tool!")
    while True:
        print("Please select an option:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        user_input = input()
        if user_input == "1":
            encrypt()
        elif user_input == "2":
            decrypt()
        elif user_input == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid input, please try again.")

if __name__ == '__main__':
    main()
