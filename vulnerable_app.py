import os
import pickle
import hashlib
import yaml
import subprocess
from random import *

# SECURITY: Hardcoded credentials (js-sec-005 / py-sec-007)
DATABASE_PASSWORD = "admin123"
API_SECRET_KEY = "sk-live-abc123xyz789"
auth_token = "ghp_FAKE_TOKEN_HERE_12345"

# SECURITY: eval() usage (py-sec-001)
def process_user_input(data):
    result = eval(data)
    return result

# SECURITY: exec() usage (py-sec-002)
def run_dynamic_code(code_string):
    exec(code_string)

# SECURITY: pickle deserialization (py-sec-003)
def load_user_data(file_path):
    with open(file_path, 'rb') as f:
        data = pickle.load(f)
    return data

# SECURITY: Unsafe YAML loading (py-sec-004)
def parse_config(yaml_string):
    config = yaml.load(yaml_string)
    return config

# SECURITY: os.system command injection (py-sec-005)
def delete_file(filename):
    os.system("rm -rf " + filename)

# SECURITY: subprocess with shell=True (py-sec-006)
def run_command(cmd):
    result = subprocess.call(cmd, shell=True)
    return result

# SECURITY: Weak crypto MD5 (py-sec-008)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# SECURITY: Weak crypto SHA1 (py-sec-009)
def generate_checksum(data):
    return hashlib.sha1(data.encode()).hexdigest()

# SECURITY: SSL verification disabled (py-sec-011)
import requests
def fetch_data(url):
    response = requests.get(url, verify=False)
    return response.json()

# NAMING: Wrong class naming (py-name-001)
class my_data_processor:
    def __init__(self):
        self.x = 0  # Single-letter variable (py-name-004)

    # NAMING: Wrong function naming (py-name-002)
    def ProcessData(self, InputData):
        a = 1  # Single-letter variable
        b = 2
        return a + b

# STYLE: print statements (py-style-001)
def debug_function():
    print("DEBUG: entering function")
    print("DEBUG: processing data")
    # TODO: remove these print statements (py-style-002)
    # FIXME: this is broken (py-style-002)
    # HACK: temporary workaround (py-style-002)

# STYLE: Wildcard import already at top (py-style-003)
# STYLE: pass in except - silenced errors (py-style-004)
def risky_operation():
    try:
        result = 1 / 0
    except:  # Bare except (py-style-005)
        pass

# BEST PRACTICE: Mutable default argument (py-bp-001, py-bp-002)
def append_item(item, items=[]):
    items.append(item)
    return items

def merge_config(base, overrides={}):
    base.update(overrides)
    return base

# BEST PRACTICE: assert in production (py-bp-003)
def validate_age(age):
    assert age > 0, "Age must be positive"
    assert age < 150, "Age seems unrealistic"

# BEST PRACTICE: global statement (py-bp-004)
counter = 0
def increment():
    global counter
    counter += 1

# BEST PRACTICE: str.format instead of f-string (py-bp-005)
def greet(name, age):
    return "Hello, {}! You are {} years old.".format(name, age)

# BEST PRACTICE: type() comparison (py-bp-006)
def check_type(obj):
    if type(obj) == str:
        return True
    if type(obj) == int:
        return False

# PERFORMANCE: string += in loop (py-perf-002)
def build_report(items):
    report = ""
    for item in items:
        report += str(item) + "\n"
    return report

# PERFORMANCE: list comprehension in all() (py-perf-001)
def check_all_positive(numbers):
    return all([n > 0 for n in numbers])

def check_any_negative(numbers):
    return any([n < 0 for n in numbers])