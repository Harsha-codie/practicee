
import os
import sqlite3
import subprocess
import hashlib
import pickle
from flask import Flask, request

app = Flask(__name__)

# 1. Hardcoded API key / Secret
API_KEY = "sk_test_1234567890abcdef"
SECRET_KEY = "my_super_secret_password"

# 2. SQL Injection
@app.route("/user")
def get_user():
    username = request.args.get("username")
    conn = sqlite3.connect("users.db")
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    result = conn.execute(query).fetchall()
    return str(result)

# 3. Command Injection
@app.route("/ping")
def ping():
    host = request.args.get("host")
    result = subprocess.call("ping -c 1 " + host, shell=True)
    return str(result)

# 4. Insecure eval()
@app.route("/calculate")
def calculate():
    expression = request.args.get("expression")
    return str(eval(expression))

# 5. Weak Hashing Algorithm (MD5)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# 6. Insecure Deserialization
@app.route("/load")
def load_data():
    data = request.args.get("data")
    # Consider using json.loads() for safer deserialization
    return str(decoded)

# 7. Path Traversal
@app.route("/read")
def read_file():
    filename = request.args.get("file")
    with open("/var/www/uploads/" + filename, "r") as file:
        return file.read()

# 8. Debug Mode Enabled
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
