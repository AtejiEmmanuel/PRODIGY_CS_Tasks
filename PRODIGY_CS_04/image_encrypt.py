#!/usr/bin/env python3

from PIL import Image
import os
import hashlib
import argparse

def generate_key_from_password(password, length):
    """Generate a repeatable byte sequence from a password"""
    # Use SHA-256 to generate a secure hash from the password
    key = hashlib.sha256(password.encode()).digest()
    
    # Repeat the key to match the required length
    return (key * (length // len(key) + 1))[:length]

def encrypt_decrypt_image(input_path, output_path, password):
    """Encrypt or decrypt an image using XOR operation with a key derived from password"""
    # Open the image
    try:
        img = Image.open(input_path)
        # Convert to RGB if it's in another mode (like RGBA)
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Get image data as a sequence of pixels
        pixels = list(img.getdata())
        width, height = img.size
        
        # Generate key from password
        key_bytes = generate_key_from_password(password, len(pixels) * 3)
        
        # Process each pixel
        encrypted_pixels = []
        key_index = 0
        
        for pixel in pixels:
            r, g, b = pixel
            
            # XOR each color channel with the corresponding key byte
            encrypted_r = r ^ key_bytes[key_index]
            key_index += 1
            
            encrypted_g = g ^ key_bytes[key_index]
            key_index += 1
            
            encrypted_b = b ^ key_bytes[key_index]
            key_index += 1
            
            encrypted_pixels.append((encrypted_r, encrypted_g, encrypted_b))
        
        # Create a new image with the encrypted pixels
        encrypted_img = Image.new('RGB', (width, height))
        encrypted_img.putdata(encrypted_pixels)
        
        # Save the encrypted/decrypted image
        encrypted_img.save(output_path)
        
        return True
    except Exception as e:
        print(f"Error processing image: {e}")
        return False

def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description='Encrypt or decrypt an image using a password.')
    parser.add_argument('input', help='Input image path')
    parser.add_argument('output', help='Output image path')
    parser.add_argument('password', help='Password for encryption/decryption')
    args = parser.parse_args()
    
    # Process the image
    if encrypt_decrypt_image(args.input, args.output, args.password):
        print(f"Image successfully processed and saved to {args.output}")
    else:
        print("Failed to process the image")

if __name__ == "__main__":
    main()
