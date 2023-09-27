from rule import apply_decrypt_rule

user_input = input("Enter text to decrypt: ")
decrypted = apply_decrypt_rule(user_input)
print("Decrypted text:", decrypted)
