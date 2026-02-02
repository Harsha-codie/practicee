import requests


API_KEY = "AIzaSyBgm4_ACmNyFAFaVPMVgU--VOktTVdwpcQ"


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


response = requests.post(
    f"{url}?key={API_KEY}",
    headers=headers,
    json=payload
)

print(response.json())
