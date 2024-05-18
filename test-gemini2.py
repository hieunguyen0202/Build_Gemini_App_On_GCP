import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models

def generate():
    vertexai.init(project="test-demo-423606", location="us-central1")
    model = GenerativeModel(
        "gemini-1.5-flash-preview-0514",
    )
    
    # Interactive input for the prompt
    prompt = input("Enter your prompt: ")
    
    responses = model.generate_content(
        [image1, prompt],
        generation_config=generation_config,
        safety_settings=safety_settings,
        stream=True,
    )

    for response in responses:
        print(response.text, end="")

image1 = Part.from_uri(
    "gs://test-bucket-111111111/field_mr_nick_500w2.jpg",
    mime_type="image/jpeg"
)

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

generate()

    # <h1>Welcome to Gemini AI on GCP !</h1>
    # <h4>Upload Image and Enter Prompt</h4>