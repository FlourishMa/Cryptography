
import random
import string

# --- Vowel Substitution Cipher ---

VOWEL_MAP_ENCRYPT = str.maketrans("aeiouAEIOU", "eiouaEIOUA")
VOWEL_MAP_DECRYPT = str.maketrans("eiouaEIOUA", "aeiouAEIOU")

def vowel_substitute(text, decrypt=False):
    """
    Substitutes vowels in the text.
    a -> e, e -> i, i -> o, o -> u, u -> a
    """
    if decrypt:
        return text.translate(VOWEL_MAP_DECRYPT)
    else:
        return text.translate(VOWEL_MAP_ENCRYPT)

# --- Monoalphabetic Substitution Cipher ---

def generate_monoalphabetic_key():
    """
    Generates a random key for monoalphabetic substitution.
    """
    alphabet = list(string.ascii_lowercase)
    shuffled_alphabet = list(string.ascii_lowercase)
    random.shuffle(shuffled_alphabet)
    key = dict(zip(alphabet, shuffled_alphabet))
    return key

def generate_inverse_key(key):
    """
    Generates the inverse key for decryption.
    """
    return {v: k for k, v in key.items()}

def monoalphabetic_cipher(text, key, decrypt=False):
    """
    Encrypts or decrypts text using a monoalphabetic substitution cipher.
    """
    if decrypt:
        key = generate_inverse_key(key)
    
    result = []
    for char in text:
        if char.lower() in key:
            substitution_char = key[char.lower()]
            if char.isupper():
                result.append(substitution_char.upper())
            else:
                result.append(substitution_char)
        else:
            result.append(char)
    return "".join(result)

# --- Main Program ---

def main():
    """
    Main function to run the cryptographic program.
    """
    plain_text = input("Enter the text to encrypt: ")

    print("\n--- Encryption Process ---")
    
    # Step 1: Vowel Substitution
    vowel_substituted_text = vowel_substitute(plain_text)
    print("\nStep 1: After vowel substitution")
    print("Result: {}".format(vowel_substituted_text))

    # Step 2: Monoalphabetic Substitution
    mono_key = generate_monoalphabetic_key()
    print("\nStep 2: Applying monoalphabetic cipher")
    # print(f"Monoalphabetic Key: {mono_key}")

    final_encrypted_text = monoalphabetic_cipher(vowel_substituted_text, mono_key)
    print("\nFinal Encrypted Text: {}".format(final_encrypted_text))

    print("\n" + "="*30)

    print("\n--- Decryption Process ---")
    
    # Step 1: Monoalphabetic Decryption
    mono_decrypted_text = monoalphabetic_cipher(final_encrypted_text, mono_key, decrypt=True)
    print("\nStep 1: After monoalphabetic decryption")
    print("Result: {}".format(mono_decrypted_text))

    # Step 2: Vowel Decryption
    final_decrypted_text = vowel_substitute(mono_decrypted_text, decrypt=True)
    print("\nStep 2: After vowel decryption (Original Text)")
    print("Result: {}".format(final_decrypted_text))

if __name__ == "__main__":
    main()
