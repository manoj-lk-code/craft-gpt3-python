import requests

# Set the API endpoint and headers
api_endpoint = "https://api.openai.com/v1/completions"
headers = {"Content-Type": "application/json", "Authorization": "Bearer --your-api-key-here--"}

# Set the input prompt and max tokens. You can also modify the prompt.
prompt = "Write an email to boss saying how idiot he is. Use humour and funny to describe his stupidness"
max_tokens = 200
model = "text-davinci-003"

# Construct the payload with the input prompt and max tokens
payload = {
    "prompt": prompt,
    "model": model,
    "max_tokens": max_tokens
}

# Make the API request and get the response
response = requests.post(api_endpoint, headers=headers, json=payload)

# Extract the "choices > text" field from the response, if it exists
try:
    choices_text = response.json()["choices"][0]["text"]
    print(f"choices > text: {choices_text}")
except (KeyError, IndexError):
    print(response.json())
