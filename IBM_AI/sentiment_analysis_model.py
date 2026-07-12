import requests
import json

def sentiment_analyzer(text_to_analyse):
    # Define the URL for the sentiment analysis API
    # The URL is for the IBM Watson Sentiment Analysis model hosted on the Skills Network Labs platform.
    # can not be used for commercial purposes. It is intended for educational and research purposes only.
    url = "https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"
    
    headers = {
        "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"
    }
    
    myobj = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    
    response = requests.post(url, json=myobj, headers=headers)
    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        formatted_response = response.json()
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    # If the response status code is 500, set label and score to None
    elif response.status_code == 500:
        label = None
        score = None
    # For any other unexpected status codes, set label and score to None
    else:
        label = None
        score = None


    return {'label': label, 'score': score}

#To execute
## type python in the command line under the directory where this file is located 
# it will start a python interpreter (python cell) and then you can import 
# the function and use it like this:
# from sentiment_analysis_model import sentiment_analyzer
# call the function with a string to analyze like this:
# sentiment_analyzer("I love this product! It's amazing.")