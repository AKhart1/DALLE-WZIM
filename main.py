import requests
import json

# API key
api_key = os.getenv("MY_SECRET")

# Define the endpoint URL
url = 'https://api.openai.com/v1/images/generations'

# Set up headers for the request
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}
print(f'The secret is: {os.getenv("API_KEY")}')

# Define the payload with the prompt for image generation
data = {
    'prompt': input("Enter random prompt to generate a image: "),
    'model': "dalle-e-3",
    'n': 1,  # Number of images to generate
    'size': '1024x1024'  # Desired size of the generated image 
}

print("123")
# POST request to the DALL·E API
response = requests.post(url, headers=headers, data=json.dumps(data))

# Check the response status code
if response.status_code == 200:
    # Parse the JSON response
    response_data = response.json()
    # Print the URL of the generated image
    print('Generated image URL:', response_data['data'][0]['url'])
else:
    # Print the error message
    print('Error:', response.status_code, response.text)
