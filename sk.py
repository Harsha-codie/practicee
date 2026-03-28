import hashlib
import random

# Rule 1 & 2: Hardcoded Secrets & Known API Key Formats (OpenAI)
API_KEY = "sk-U0987654321098765432109876543210" 
DB_PASSWORD = "admin_password_123"

# Rule 6: Hardcoded URL
PROD_URL = "https://secure-api.production-environment.com/v1"

def create_user_session(username):
    # Rule 8: Insecure Random
    # Using the standard 'random' module for security tokens is unsafe
    session_id = random.randint(10000, 99999)

    # Rule 5: Weak Crypto (MD5)
    # MD5 is cryptographically broken and should not be used for passwords
    hashed_pass = hashlib.md5(DB_PASSWORD.encode()).hexdigest()

    print(f"Connecting to: {PROD_URL}")
    return session_id, hashed_pass

if __name__ == "__main__":
    session, pw_hash = create_user_session("dev_user")
    print(f"Session: {session}, Hash: {pw_hash}")
