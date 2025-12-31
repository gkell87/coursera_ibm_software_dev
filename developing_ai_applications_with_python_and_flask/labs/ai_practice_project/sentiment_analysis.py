# Import the requests library to handle HTTP requests
import requests

# Define a function named sentiment_analyzer
def sentiment_analyzer(text_to_analyse): 
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    json = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json = json, header)
    return response.text

