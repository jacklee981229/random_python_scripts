from rule import apply_encrypt_rule

user_input = input("Enter text to encrypt: ")
encrypted = apply_encrypt_rule(user_input)
print("Encrypted text:", encrypted)
