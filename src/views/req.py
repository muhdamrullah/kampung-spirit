import requests
import json

def getResponse(input_message):
    url = 'http://localhost:8080/chatbot'
    payload = {"message":input_message}
    r = requests.post(url, json=payload)
    return r.text


