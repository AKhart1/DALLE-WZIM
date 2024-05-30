from flask import Flask, request, jsonify, render_template, send_from_directory
import os
import requests
from dotenv import load_dotenv
import json
from PIL import Image
from io import BytesIO


SAVE_PATH = "./app/static/generated_images/"
# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__, static_folder='static')

# Get the OpenAI API key from the environment variables
OPENAI_API_KEY = os.getenv("MY_SECRET", None)
if not OPENAI_API_KEY:
    raise ValueError("No API key found in environment variables.")

OPENAI_API_URL = 'https://api.openai.com/v1/images/generations'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_image', methods=['POST'])
def generate_image():
    prompt = request.form.get('prompt')
    headers = {
        'Authorization': f'Bearer {OPENAI_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'prompt': prompt,
        'n': 1,
        'size': '512x512'
    }

    response = requests.post(OPENAI_API_URL, headers=headers, json=data)
    response_json = response.json()
    save_image(response_json, data['prompt'])

    if response.status_code == 200:
        image_url = response_json['data'][0]['url']
        return jsonify({'image_url': image_url})
    else:
        return jsonify({'error': response_json}), 500
    
@app.route('/get_images')
def get_images():
    # Get all file paths and names of PNG images in the .json file
    # Load the JSON file
    with open("./app/image_data.json", "r") as f:
        images_data = json.load(f)['images']
    return jsonify(images_data)
    
def save_image(response, prompt):
    # Load the JSON file
    with open("./app/image_data.json", "r") as f:
        images_data = json.load(f)
    # Create new data block
    new_image_data = {
        "prompt": prompt,
        "name": f"{response['created']}.png"
    }
    print("It's okay")

    # Append the new data to the "images" list
    images_data["images"].append(new_image_data)

    # Save the updated JSON file
    with open("./app/image_data.json", "w") as f:
        json.dump(images_data, f, indent=4)  # Add indentation for readability

    url = response['data'][0]['url']
    # Send a GET request to the URL
    response_url = requests.get(url)
    # Check if the request was successful
    response_url.raise_for_status()
    
    # Open the image from the response content
    image = Image.open(BytesIO(response_url.content))
    # Save the image to the specified file path
    image.save(f"{SAVE_PATH}" + f"{response['created']}.png")
    print(f"Image saved to {SAVE_PATH}")

if __name__ == "__main__":
    app.run()
