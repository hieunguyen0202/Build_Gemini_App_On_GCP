import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import vertexai
from google.cloud import storage
from google.oauth2 import service_account
from vertexai.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models

app = Flask(__name__)

# Initialize Vertex AI
vertexai.init(project="test-demo-423606", location="us-central1")
model = GenerativeModel("gemini-1.5-flash-preview-0514")

# Configuration for the generation
generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

# Google Cloud Storage configuration
GCS_BUCKET_NAME = 'test-bucket-111111111'
SERVICE_ACCOUNT_KEY_PATH = 'test-demo-key.json'
storage_credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_KEY_PATH)
storage_client = storage.Client(credentials=storage_credentials)

def upload_to_gcs(file, bucket_name, destination_blob_name):
    """Uploads a file to Google Cloud Storage."""
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_file(file)
    return f"gs://{bucket_name}/{destination_blob_name}"

def get_public_url(bucket_name, blob_name):
    """Generates a signed URL for a blob in Google Cloud Storage."""
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    return blob.public_url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    if 'image' not in request.files:
        return "No image provided", 400
    
    file = request.files['image']
    if file.filename == '':
        return "No image selected", 400
    
    if file:
        filename = secure_filename(file.filename)
        gcs_uri = upload_to_gcs(file, GCS_BUCKET_NAME, filename)

        image_part = Part.from_uri(gcs_uri, mime_type=file.mimetype)
        prompt = request.form['prompt']
        
        responses = model.generate_content(
            [image_part, prompt],
            generation_config=generation_config,
            safety_settings=safety_settings,
            stream=True,
        )
        
        result_text = ""
        for response in responses:
            result_text += response.text
        
        public_url = get_public_url(GCS_BUCKET_NAME, filename)
        print(public_url)
        return render_template('index.html', result=result_text, uploaded_image=public_url)

if __name__ == '__main__':
    app.run(debug=True)
