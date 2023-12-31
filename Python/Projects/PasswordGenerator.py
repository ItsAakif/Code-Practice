import secrets
import string

def generate_password(min_length=8, max_length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True):
    # Define character sets based on user preferences
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    # Ensure at least one character from each selected set
    if use_uppercase:
        characters += secrets.choice(string.ascii_uppercase)
    if use_lowercase:
        characters += secrets.choice(string.ascii_lowercase)
    if use_digits:
        characters += secrets.choice(string.digits)
    if use_special_chars:
        characters += secrets.choice(string.punctuation)

    # Randomly choose the length within the specified range
    length = secrets.randbelow(max_length - min_length + 1) + min_length

    # Shuffle the characters and generate the password
    password = ''.join(secrets.choice(characters) for _ in range(length))

    return password

# Example usage:
password = generate_password(min_length=10, max_length=16, use_special_chars=True)
print("Generated Password:", password)
