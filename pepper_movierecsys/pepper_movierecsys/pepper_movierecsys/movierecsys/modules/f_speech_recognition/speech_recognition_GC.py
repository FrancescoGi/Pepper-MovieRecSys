# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 15:25:20 2019

@author: Francesco & Piero
"""

import os
import requests, base64, json

def speech_recognition(path,credentials_path):

    with open(credentials_path) as json_data:
        data = json.load(json_data) 

        APIKEY = data['apikey']
        GOOGLE_SPEECH_URL = data['google_speech_url'] 
        
        GOOGLE_SPEECH_URL = GOOGLE_SPEECH_URL+"?key={0}".format(APIKEY)

        f = open(path, 'rb')
        audio = f.read()
        base64_data = base64.b64encode(audio)
        f.close()

        body = {
            'config': {
                "enableAutomaticPunctuation": True,
                'encoding':'LINEAR16',
                'languageCode':'en-GB',

            },
            'audio': {
                'content': base64_data
            }
        }
        try:

            res = requests.post(GOOGLE_SPEECH_URL, data=json.dumps(body))
            data = res.json()
            result = data['results']
        except:
            return -1
        if res.status_code == 200:
            if len(result) > 0:
                if len(result[0]['alternatives']) > 0:
                    text = result[0]['alternatives'][0]['transcript'].encode('utf')
                    print(str(text))
        else:
            print('Connection error.')
            
    return  str(text)      