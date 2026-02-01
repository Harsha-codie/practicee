# Python file with intentional security violations
# This file should trigger multiple CodeGuard rules

import hashlib
import random
import pickle

# VIOLATION 1: Hardcoded API keys and secrets
API_KEY = "sk-1234567890abcdefghijklmnop"
PASSWORD = "supersecret123"
TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz123456"
secret = "my-super-secret-key"

# VIOLATION 2: Hardcoded URLs
api_url = "https://api.example.com/v1/users"
backend_url = "https://production.myapp.com/api/data"

# VIOLATION 3: Weak cryptographic algorithms (MD5/SHA1)
def hash_password_weak(password):
    # Using weak MD5
    md5_hash = hashlib.md5(password.encode()).hexdigest()
    # Using weak SHA1
    sha1_hash = hashlib.sha1(password.encode()).hexdigest()
    return md5_hash, sha1_hash

# VIOLATION 4: Insecure random number generation
def generate_token():
    # Using insecure random
    return random.random()

def generate_code():
    # Also insecure
    return random.randint(100000, 999999)

# VIOLATION 5: Dangerous eval() and exec()
def execute_user_input(user_input):
    # DANGEROUS: eval can execute arbitrary code
    result = eval(user_input)
    return result

def run_dynamic_code(code_string):
    # DANGEROUS: exec can execute arbitrary code
    exec(code_string)

# VIOLATION 6: Insecure pickle usage
def load_untrusted_data(file_path):
    with open(file_path, 'rb') as f:
        # DANGEROUS: pickle.load on untrusted data
        data = pickle.load(f)
    return data

def parse_data(data_bytes):
    # Also dangerous
    return pickle.loads(data_bytes)

# More hardcoded credentials
auth_token = "Bearer xyz123456789"
database_password = "db_password_123"

print("Loaded config with API_KEY:", API_KEY)
