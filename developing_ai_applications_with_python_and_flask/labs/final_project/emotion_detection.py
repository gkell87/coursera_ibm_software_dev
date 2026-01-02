# Import appropriate libraries
import json, requests

# Create function using watson Emotion Predict

def emotion_detector(text_to_analyse):
    # Set Post Perameters
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputJson = { "raw_document": {"text": text_to_analyse }}

    # Return post response
    return requests.post(url, json = inputJson, headers = headers).text