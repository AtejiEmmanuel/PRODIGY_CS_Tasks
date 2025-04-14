# Caesar Cipher

A simple Python implementation of the Caesar Cipher encryption and decryption algorithm.

## Description

The Caesar Cipher is one of the earliest and simplest forms of encryption. It works by shifting each letter in the plaintext by a fixed number of positions down the alphabet. This implementation allows users to encrypt and decrypt messages using a specified shift value.

## Demo



*Terminal demonstration showing encryption of "Yomi" with shift 5 resulting in "Dtrn", and decryption of "Dtrn" with shift 5 returning to "Yomi"*

## Features

- Encrypt messages using the Caesar Cipher algorithm
- Decrypt encrypted messages with the correct shift value
- Preserves non-alphabetic characters (spaces, numbers, symbols)
- Handles both uppercase and lowercase letters

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/caesar-cipher.git
   cd caesar-cipher
   ```

2. No additional packages are required as the program uses only Python's built-in functions.

## Usage

Run the program using Python 3:

```
python3 caesar_cipher.py
```

Follow the interactive prompts:
1. Choose whether to encrypt (1) or decrypt (2) a message
2. Enter the message you want to process
3. Enter the shift value (between 1-25)

The program will output the processed message.

## Example

```
=== Caesar Cipher Tool ===
1. Encrypt a message
2. Decrypt a message
Enter your choice (1 or 2): 1
Enter your message: Hello World
Enter the shift value (1-25): 3
Encrypted message: Khoor Zruog
```

And to decrypt:

```
=== Caesar Cipher Tool ===
1. Encrypt a message
2. Decrypt a message
Enter your choice (1 or 2): 2
Enter your message: Khoor Zruog
Enter the shift value (1-25): 3
Decrypted message: Hello World
```

## How It Works

The Caesar Cipher works by shifting each letter in the message by a fixed amount:

- For encryption: Each letter is shifted forward in the alphabet by the shift value.
- For decryption: Each letter is shifted backward in the alphabet by the shift value.

The algorithm handles alphabet wrapping (e.g., 'Z' shifted by 1 becomes 'A').

## Code Structure

- `encrypt(text, shift)`: Encrypts the input text using the specified shift value
- `decrypt(text, shift)`: Decrypts the input text using the specified shift value
- `main()`: Handles user interaction and program flow

## Limitations

- Only works with ASCII characters
- Does not handle non-Latin alphabets
