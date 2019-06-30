# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 10:00:53 2018

@author: Francesco & Piero
"""
from config.movierecsysbot_config import require_config
import requests, json, datetime 

def getReply(chatId, messageId, text, firstname, botName):
    """
    Manda il messaggio dell'utente al server, in modo stateless.
    La richiesta è in formato HTTP GET e contiene anche le seguenti informazioni
    (potrebbero cambiare): 
    @param chatId ID dell'utente.
    @param messageId ID del messaggio.
    @param timeStamp Data del messaggio.
    @param text Testo del messaggio.
    @param firstname Nome dell'utente.
    @param botName Nome del bot.
    @return Risposta del server già json-decodificata (array); attualmente contiene
         'messages' - Testo di risposta del bot,
         'reply_markup' - (Opzionale) Possibili opzioni di risposta dell'utente.
         'auxAPI' - (Opzionale) Indica l'URL che è necessario chiamare per completare la risposta.
    """
    config = require_config()
           
    timeStamp=datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')

    payload = {'userID': chatId, 'messageID': messageId,'timeStamp': timeStamp, 'text': text, 'firstname': firstname, 'botName': botName}

    stringGetRequest = 'http://'+config['base_uri']+config['application_uri']+'/restService/getReply'
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
