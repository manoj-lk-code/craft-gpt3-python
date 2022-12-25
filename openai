import requests

# Set the API endpoint and headers
api_endpoint = "https://api.openai.com/v1/completions"
headers = {"Content-Type": "application/json", "Authorization": "Bearer ---api-token-here---"}

# Set the input prompt and max tokens
prompt = "Write an email to boss saying how idiot he is. Use humour and funny to describe his stupidness"
max_tokens = 200
model = "text-davinci-003"

# Construct the payload with the input prompt and max tokens
payload = {
    "prompt": prompt,
    "max_tokens": max_tokens,
    "model": model
}

# Make the API request
response = requests.post(api_endpoint, headers=headers, json=payload)

# Extract the "choices" field from the JSON response
choices = response.json()["choices"]

# Iterate through the choices and print the "text" field for each choice
for choice in choices:
    print(f"choices > text: {choice['text']}")
