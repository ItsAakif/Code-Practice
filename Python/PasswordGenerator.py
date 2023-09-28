# Random Password  Generator by Aakif Mudel
import random
import string

def generate_password(length=12):
    # Define the characters to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password by selecting 'length' characters from 'characters'
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Example usage:
password = generate_password()
print("Generated Password:", password)
