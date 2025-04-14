def encrypt(text, shift):
    """
    Encrypts text using Caesar Cipher with the specified shift.
    
    Args:
        text (str): The text to encrypt
        shift (int): The shift value (1-25)
        
    Returns:
        str: The encrypted text
    """
    result = ""
    
    # Traverse the plain text
    for char in text:
        # Check if character is an uppercase letter
        if char.isupper():
            # Convert to ASCII, apply shift, and convert back to character
            # The modulo operation (% 26) ensures the value wraps around if it exceeds 'Z'
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        
        # Check if character is a lowercase letter
        elif char.islower():
            # Convert to ASCII, apply shift, and convert back to character
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        
        # If character is not a letter (space, number, symbol), leave it as is
        else:
            result += char
            
    return result

def decrypt(text, shift):
    """
    Decrypts text using Caesar Cipher with the specified shift.
    
    Args:
        text (str): The encrypted text
        shift (int): The shift value (1-25)
        
    Returns:
        str: The decrypted text
    """
    # Decryption is just encryption with the negative shift
    return encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Tool ===")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    
    # Get user choice
    choice = input("Enter your choice (1 or 2): ")
    
    # Get the message from the user
    message = input("Enter your message: ")
    
    # Get the shift value from the user
    shift = int(input("Enter the shift value (1-25): "))
    
    # Ensure shift is within the valid range (1-25)
    shift = shift % 26
    
    if choice == '1':
        # Encrypt the message
        result = encrypt(message, shift)
        print(f"Encrypted message: {result}")
    elif choice == '2':
        # Decrypt the message
        result = decrypt(message, shift)
        print(f"Decrypted message: {result}")
    else:
        print("Invalid choice!")

# This condition checks if the script is being run directly (not imported)
if __name__ == "__main__":
    main()
