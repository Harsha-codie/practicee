import requests

# ❌ API key hardcoded in source code
API_KEY = "AIzaSyBgm4_ACmNyFAFaVPMVgU--VOktTVdwpcQ"

# ❌ Direct API endpoint exposed
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

headers = {
    "Content-Type": "application/json"
}

payload = {
    "contents": [
        {
            "parts": [
                {"text": "Explain what an API key is"}
            ]
        }
    ]
}

# ❌ API key sent directly in URL
response = requests.post(
    f"{url}?key={API_KEY}",
    headers=headers,
    json=payload
)

print(response.json())
