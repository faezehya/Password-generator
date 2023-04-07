import random
import string

def generate_password(length):
    # Define the pool of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Use random.choices to generate a list of characters of the desired length
    password = ''.join(random.choices(characters, k=length))
    
    return password
