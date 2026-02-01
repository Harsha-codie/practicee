// Test file with intentional security violations
// This file should trigger multiple CodeGuard rules

// VIOLATION 1: Hardcoded API key
const API_KEY = "sk-1234567890abcdefghijklmnop";
const password = "supersecret123";
const token = "ghp_abcdefghijklmnopqrstuvwxyz123456";

// VIOLATION 2: Hardcoded URLs
const apiUrl = "https://api.example.com/v1/users";
const backendUrl = "http://localhost:3000/api/data";

// VIOLATION 3: Weak cryptographic algorithm
const crypto = require('crypto');
const hash = crypto.createHash('md5').update('data').digest('hex');
const weakHash = crypto.createHash('sha1').update('password').digest('hex');

// VIOLATION 4: Insecure random number
function generateToken() {
    return Math.random().toString(36).substring(2);
}

// VIOLATION 5: SSL certificate verification disabled
const https = require('https');
const agent = new https.Agent({
    rejectUnauthorized: false  // DANGEROUS!
});

// VIOLATION 6: document.write (XSS risk)
function updatePage(content) {
    document.write(content);
}

// More violations
const secret = "my-super-secret-key";
const auth_token = "Bearer xyz123456789";

console.log("Debug: API Key is", API_KEY);
