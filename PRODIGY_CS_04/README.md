# Image Encryption Tool

A simple Python-based image encryption and decryption tool that manipulates pixels using XOR operations with a key derived from a password.

## Project Overview

This project implements a basic image encryption system using pixel manipulation techniques. The tool:

- Takes an input image and encrypts it using a password-based key
- Transforms each pixel using XOR operations
- Produces an encrypted image that appears as random noise
- Can decrypt the image using the same password

## Prerequisites

- Python 3.x
- PIL (Python Imaging Library) / Pillow

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/image-encryption-tool.git
cd image-encryption-tool
```

### 2. Install dependencies

In Kali Linux (or other Debian-based systems), you can install the required PIL/Pillow library using:

```bash
sudo apt update
sudo apt install python3-pil
```

If you encounter an "externally-managed-environment" error with pip, use one of these alternative approaches:

#### Option 1: System-wide installation (recommended)
```bash
sudo apt install python3-pil
```

#### Option 2: Virtual environment
```bash
sudo apt install python3-venv
python3 -m venv ~/image_encrypt_env
source ~/image_encrypt_env/bin/activate
pip install pillow
```

#### Option 3: Using pipx
```bash
sudo apt install pipx
pipx install pillow
```

### 3. Make the script executable

```bash
chmod +x image_encrypt.py
```

## Usage

The basic syntax for using the tool is:

```bash
./image_encrypt.py input_image output_image "your_secret_password"
```

### Example: Encrypting an image

```bash
./image_encrypt.py original.png encrypted.png "secret123"
```

### Example: Decrypting an image

```bash
./image_encrypt.py encrypted.png decrypted.png "secret123"
```

> **Note:** You must use the same password for decryption as was used for encryption.

## How It Works

1. **Password Processing**: The password is hashed using SHA-256 to generate a secure key.
2. **Pixel Manipulation**: Each RGB channel of every pixel is XORed with corresponding bytes from the key.
3. **Symmetric Operation**: XOR has the property that applying it twice with the same key restores the original value, making encryption and decryption identical operations.

## Implementation Details

The encryption/decryption process follows these steps:

1. Read the input image using PIL
2. Convert the image to RGB mode if necessary
3. Generate a key from the provided password using SHA-256
4. Process each pixel by applying XOR between RGB values and key bytes
5. Create a new image with the processed pixels
6. Save the result to the output file

## Security Considerations

- This is a basic implementation suitable for educational purposes
- The security strength depends entirely on the password complexity
- The encrypted image will appear as random noise but professional cryptanalysis might reveal patterns
- Not recommended for highly sensitive data without additional security measures

## Troubleshooting

- **File Not Found Error**: Ensure the input image exists and the path is correct
- **Permission Denied**: Make sure the script is executable (`chmod +x image_encrypt.py`)
- **Corrupted Decryption**: Verify you're using the same password as for encryption
- **PIL Import Error**: Install the Pillow library using apt as shown in the installation section

## Future Improvements

- Add additional encryption algorithms
- Implement key stretching for enhanced security
- Add a GUI interface
- Support for additional image formats
- Add integrity verification

## License

This project is licensed under the MIT License - see the LICENSE file for details.
