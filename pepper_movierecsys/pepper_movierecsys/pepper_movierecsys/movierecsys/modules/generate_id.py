# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 18:45:14 2018

@author: Francesco
"""
import datetime
import socket

def generate_message_id():
    id=datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    ip = socket.gethostbyname(socket.gethostname())
    ip = 'pepper.local'
    return ip+'-'+id

def generate_message_id_cont(name, file):
    f = open(file, "r")
    id = f.read()
    f.close()
    f = open(file, "w")
    new_id = int(float(id)) + 1
    f.write(str(new_id)) 
    f.close()
    return name+'.'+id    