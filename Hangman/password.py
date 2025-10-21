import random
import string

def generate_password(length: int = 10) -> str:
    """Generate a random password using letters, digits, and punctuation."""
    characters: str = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


