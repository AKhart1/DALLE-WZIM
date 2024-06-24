# Gallery Generator with DALLE-2

This project is a Flask application that allows users to generate images using the DALL-E 2 API and manage their own gallery of generated images.

## Table of Contents

- [Gallery Generator with DALL-E 2](#gallery-generator-with-dall-e-2)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Running the Application](#running-the-application)
    - [Generating Images](#generating-images)
    - [Viewing Generated Images](#viewing-generated-images)
  - [Environment Variables](#environment-variables)
  - [File Structure](#file-structure)
  - [Dependencies](#dependencies)
  - [License](#license)
 
## Features

- Generate images using the DALL-E 2 API.
- Save and manage generated images.
- View a gallery of all generated images.
- Generate descriptions for the images.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AKhart1/DALLE-WZIM.git
   cd gallery-generator

2. **Create and activate a virtual environment::**

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

Create a **'.env'** file in the root directory of the project and add your OpenAI API key:

   ```bash
   MY_SECRET=your_openai_api_key_here
   ```

5. **Create necessary directories and files:**


   ```bash
   mkdir -p app/static/generated_images
   echo '{"images": []}' > app/image_data.json
   ```

## Usage

### Running the Application

Start the Flask application by running:

   ```bash
   pyton ./app/main.py
   ```
or

   ```bash
   uvicorn app.main:app --reload
   ```

The application will be accessible at http://127.0.0.1:5000.

### Generating Images

1. Navigate to http://13.60.129.45:5000.
2. Enter a prompt in the input field and submit.
3. The generated image will be displayed on the page.

### Viewing Generated Images

- Navigate to http://13.60.129.45:5000/get_images to view the list of all generated images in JSON format.

## Environment Variables

The application uses the following environment variables:
    
- **`MY_SECRET`**: Your OpenAI API key.

## File Structure

```
gallery-generator/
├── app/
│   ├── static/
│   │   └── generated_images/
│   ├── templates/
│   │   └── index.html
│   ├── image_data.json
│   ├── __init__.py
│   ├── auto-prompt.py
│   └── main.py
├── .env
├── requirements.txt
└── README.md
```

## Dependencies

- Flask
- requests
- python-dotenv
- Pillow
- Boto3

Install the dependencies using:

```bash
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Deployment on AWS EC2 (using terraform configuration)

The application is deployed on an AWS EC2 instance, utilizing the following AWS services and configurations:
- IAM Roles: Secure access management for the EC2 instance.
- Elastic IPs: Static IP address for reliable access.
- Security Groups: Firewall rules to control traffic to the EC2 instance.
- Secret Manager: Secure sensetive data as tokens, passwords and etc.



Feel free to contribute to the project by creating pull requests or opening issues for any bugs or feature requests. Enjoy generating your own gallery of images!
