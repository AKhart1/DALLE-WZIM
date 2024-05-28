from flask import Flask, request, jsonify, render_template
import os
import requests
from dotenv import load_dotenv
import json


# # Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

# # Get the OpenAI API key from the environment variables
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

    # Load the JSON file
    with open("./app/image_urls.json", "r") as f:
        images_data = json.load(f)

    # Create the new data block
    new_image_data = {
        "prompt": data["prompt"],
        "url": response_json['data'][0]['url']
    }

    # Append the new data to the "images" list
    images_data["images"].append(new_image_data)

    # Save the updated JSON file
    with open("./app/image_urls.json", "w") as f:
        json.dump(images_data, f, indent=4)  # Add indentation for readability
    
    if response.status_code == 200:
        image_url = response_json['data'][0]['url']
        return jsonify({'image_url': image_url})
    else:
        return jsonify({'error': response_json}), 500

if __name__ == "__main__":
    app.run()