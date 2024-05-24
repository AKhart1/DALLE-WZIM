import requests
import json
import os
from PIL import Image
from io import BytesIO

api_key = os.getenv("MY_SECRET")
FILE_PATH = r'./generated_images/'

print(f"API Key: {api_key}")

if not api_key:
    raise ValueError("No API key provided. Please set the MY_SECRET environment variable.")


def image_gen():
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
        # url = response_data['data'][0]['url']
        return response_data
    else:
        # Print the error message
        print(f"Error: {response.status_code}, {response.text}")
        return None


def save_image_from_url(file_path):
    # try:
        # api_response = image_gen()
        # url = api_response['data'][0]['url']
        # print(url)
        # print(type(url))
        ert = 'ioejrfioerf'
        print(type(ert))
        print(api_key)
        print(type(api_key))

#         # Send a GET request to the URL
#         response_url = requests.get(url)
#         # Check if the request was successful
#         response_url.raise_for_status()
        
#         # Open the image from the response content
#         image = Image.open(BytesIO(response_url.content))
        
#         # Save the image to the specified file path
#         image.save(f"{file_path}" + f"{api_response['created']}.png")
#         print(f"Image saved to {file_path}")
#     except AttributeError:
#         if api_response is None:
#             print("api_response variable is None. Cannot perform operation.")
#         else:
#             print("AttributeError occurred.")
#     except requests.exceptions.RequestException as e:
#         print(f"Error downloading image: {e}")
#     except IOError as e:
#         print(f"Error saving image: {e}")

# def run():
#     save_image_from_url(FILE_PATH)

# run()

save_image_from_url(FILE_PATH)