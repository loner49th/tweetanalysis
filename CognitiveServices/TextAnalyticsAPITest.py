import tweepy
import datetime
import pandas as pd

def sentimentValue(string):
    subscription_key = "subscription_key"
    assert subscription_key
    text_analytics_base_url = "https://westus2.api.cognitive.microsoft.com/text/analytics/v2.0/"
    language_api_url = text_analytics_base_url + "sentiment"
    documents = { 'documents': [
        { 'id': '1', 'text':"" },
    ]}
    documents["documents"][0]['text'] = string
    import requests
    from pprint import pprint
    headers   = {"Ocp-Apim-Subscription-Key": subscription_key}
    response  = requests.post(language_api_url, headers=headers, json=documents)
    responseJson = response.json()
    return responseJson['documents'][0]['score']


if __name__ == '__main__':

    keyword = "テスト"
    sentimentValue(keyword)

