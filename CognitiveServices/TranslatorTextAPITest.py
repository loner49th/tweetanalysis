def toEnglish(string):
    # -*- coding: utf-8 -*-
    import requests, uuid, json

    trans_subscriptionKey = "TRANSLATOR_TEXT_KEY"

    base_url = 'https://api.cognitive.microsofttranslator.com'
    path = '/translate?api-version=3.0'
    params = '&to=en'
    constructed_url = base_url + path + params

    headers = {
        'Ocp-Apim-Subscription-Key': trans_subscriptionKey,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text' : ''
    }]

    body[0]['text'] = string

    request = requests.post(constructed_url, headers=headers, json=body)
    response = request.json()
     
    return response[0]['translations'][0]['text']


if __name__ == '__main__':

    keyword = "テスト"
    toEnglish(keyword)

