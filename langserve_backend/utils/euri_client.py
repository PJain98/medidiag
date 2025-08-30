import requests

API_KEY = "euri-e5719dffa373bc778e744a1f9958dd4b5541b0ce5b518514b6da39dfb132acf7"
BASE_URL = "https://api.euron.one/api/v1/euri"

def euri_chat_completion(messages, model="gpt-4.1-nano", temperature=0.7, max_tokens=200):
    url = f"{BASE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"]
