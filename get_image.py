import requests
import json
import os
from PIL import Image
from io import BytesIO

api_key = os.getenv("MY_SECRET")
FILE_PATH = '.\generated_images\\'

    
# Define the endpoint URL
url = 'https://api.openai.com/v1/images/generations'
# Set up headers for the request
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}
# Define the payload with the prompt for image generation
data = {
    'prompt': "beautiful japanese sunset", # should integrate input() or smth similar here
    'n': 1,  # Number of images to generate (up to 10)
    'size': '1024x1024'  # Desired size of the generated image 
}
# POST request to the DALL·E API
response = requests.post(url, headers=headers, data=json.dumps(data))
# Check the response status code
if response.status_code == 200:
    # Parse the JSON response
    response_data = response.json()
    # URL of the generated image
    url = response_data['data'][0]['url']
else:
    # Print the error message
    print('Error:', response.status_code, response.text)


def save_image_from_url(url, file_path):
    try:
        print(response_data["created"])
        # Send a GET request to the URL
        response_url = requests.get(url)
        # Check if the request was successful
        response_url.raise_for_status()
        
        # Open the image from the response content
        image = Image.open(BytesIO(response_url.content))
        
        # Save the image to the specified file path
        image.save(f"{file_path}" + f"{response_data['created']}.png")
        print(f"Image saved to {file_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
    except IOError as e:
        print(f"Error saving image: {e}")


save_image_from_url(url, FILE_PATH)