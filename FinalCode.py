import requests, uuid, json

key = "bd68af0c7b8a44568a07549cf48bf694"
endpoint = "https://api.cognitive.microsofttranslator.com"


location = "southeastasia";

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'kn',
    'to': 'en'
}
headers = {
    'Ocp-Apim-Subscription-Key': key,
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}
body = [{
    'text': "ಹಲೋ ನೀವು ಹೇಗಿದ್ದೀರಿ"
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))