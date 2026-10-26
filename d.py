import random
import hashlib
import requests

# Error 1: Hardcoded URL (Avoid hardcoding URLs)
API_URL = "http://example.com/api/users"

# Error 2: Insecure random number generation
def generate_token():
    return str(random.randint(100000, 999999))

# Error 3: Deprecated cryptography (MD5)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def fetch_users():
    response = requests.get(API_URL)
    return response.json()

if __name__ == "__main__":
    token = generate_token()
    password_hash = hash_password("admin123")
    users = fetch_users()

    print("Token:", token)
    print("Password hash:", password_hash)
    print("Users:", users)
