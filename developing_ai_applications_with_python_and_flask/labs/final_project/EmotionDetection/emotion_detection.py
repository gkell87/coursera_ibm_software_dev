# Import appropriate libraries
import json, requests

# Create function using watson Emotion Predict

def emotion_detector(text_to_analyse):
    # Set Post Perameters
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
               "content-type" : "json"}    
                
    inputJson = { "raw_document": {"text": text_to_analyse }}

    # Return post response
    r = requests.post(url, json = inputJson, headers = headers)

    # Handle no input error
    if r.status_code == 400:
        return {"anger" : None, "disgust" : None, "fear" : None, 
        "joy" : None, "sadness" : None, "dominant_emotion" : None}

    # Get dominant emotion and reformat response
    emotions = r.json()['emotionPredictions'][0]['emotion']

    for emo in emotions.items():
        if max(emotions.values()) in emo:
            dominant_emotion = list(emo)[0]

    emotions['dominant_emotion'] = dominant_emotion
    return emotions

        