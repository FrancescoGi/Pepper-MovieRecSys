# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 10:00:53 2018

@author: Francesco & Piero
"""
from config.movierecsysbot_config import require_config
import requests, json, calendar 
from datetime import datetime

def getUserDetails(userid):
    """
    Manda il messaggio dell'utente al server, in modo stateless.
    La richiesta è in formato HTTP GET e contiene anche le seguenti informazioni
    (potrebbero cambiare): 
    """
    config = require_config()

    payload = {'userID': userid}

    stringGetRequest = 'http://'+config['base_uri']+config['application_uri']+'/restService/users/userDetail'
    print(stringGetRequest)
    #stringGetRequest = getApiBaseURL()
    #file_put_contents ( "php://stderr", '[sendMessageToServer]' . $base_uri . $stringGetRequest . PHP_EOL );

    s = requests.Session()    
    request = requests.Request('GET',stringGetRequest, params=payload)
    prepared_request = s.prepare_request(request)
    settings = s.merge_environment_settings (prepared_request.url, None , None , None , None )
    
    try:
        response = s.send(prepared_request, ** settings)
    except:
        print("Non è possibile inviare la richiesta")
    
    print(response.status_code)
    
    if(response.status_code != 200):
        print('Errore')
        
    return response.json()    

#print(getUserDetails('1552393521'))