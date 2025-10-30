# Python Cryptographic Program

This Python script implements a simple two-step cryptographic process to encrypt and decrypt text. It combines a vowel substitution cipher with a monoalphabetic substitution cipher to transform plaintext into ciphertext and vice-versa.

## Features

*   **Vowel Substitution:** Replaces vowels in the input text with other vowels in a cyclic manner (a->e, e->i, i->o, o->u, u->a), preserving the original casing.
*   **Monoalphabetic Substitution Cipher:** After vowel substitution, the text is further encrypted using a randomly generated monoalphabetic substitution key. Each letter of the alphabet is consistently mapped to another unique letter, preserving the original casing of non-vowel characters.
*   **Encryption & Decryption:** The script demonstrates both the encryption process (plaintext to ciphertext) and the decryption process (ciphertext back to plaintext), showing intermediate steps.
*   **Interactive CLI:** Easy to use via the command line, prompting the user for input text.

## Technologies Used

*   Python 3.x
*   Standard Python libraries: `random`, `string`

## How to Use

### Prerequisites

*   Python 3.x installed on your system.

### Running the Script

1.  Save the script as `cryptography.py`.
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the script.
4.  Run the script using the following command:

    ```bash
    python3 cryptography.py
    ```

5.  The script will then prompt you to "Enter the text to encrypt:". Type your desired text and press Enter.
6.  The script will output the intermediate and final encrypted text, followed by the decryption steps to show the original text.

## Example

```
$ python3 cryptography.py
Enter the text to encrypt: Hello World

--- Encryption Process ---

Step 1: After vowel substitution
Result: Helle Werld

Step 2: Applying monoalphabetic cipher

Final Encrypted Text: Jgxxg Ygpxf

==============================

--- Decryption Process ---

Step 1: After monoalphabetic decryption
Result: Helle Werld

Step 2: After vowel decryption (Original Text)
Result: Hello World
```

## License

This project is open-source.