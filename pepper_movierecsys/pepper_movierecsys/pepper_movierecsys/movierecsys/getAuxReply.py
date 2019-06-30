# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 10:31:24 2018

@author: Francesco
"""
import requests, json 

def getAuxReply(auxAPI):
   #file_put_contents("php://stderr", "auxAPI: \n" . print_r($auxAPI, true) . PHP_EOL);

   apiURL = auxAPI['apiURL']
   if(auxAPI['parameters'] == None): 
       # E' una richiesta GET
       #file_put_contents("php://stderr", '[auxAPI GET] ' . $baseUrl . $stringGetRequest . PHP_EOL);
       s = requests.Session()    
       request = requests.Request('GET',apiURL)
       prepared_request = s.prepare_request(request)
       settings = s.merge_environment_settings (prepared_request.url, None , None , None , None )
        
   else: 
       #E' una richiesta POST
       #le_put_contents("php://stderr", '[auxAPI POST] ' . $baseUrl . $stringGetRequest . PHP_EOL);
       
       #data_json = json.dumps(auxAPI['parameters'])
        
       s = requests.Session()
       request = requests.Request ('POST',apiURL,json=auxAPI['parameters'])
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
    
msg = {u'auxAPI': {u'apiURL': u'http://90.147.102.235:8080/movierecsysservice/restService/getFirstRecommendation?userID=108949456', u'parameters': {u'userID': 108949456, u'filters': [], u'messageID': u'pepper.local-20190129160802852000'}, u'messageID': u'pepper.local-20190129160802852000'}, u'messages': [{u'text': u"Ok, let me think of something... (please don't send messages!)"}]}

print(getAuxReply(msg['auxAPI']))