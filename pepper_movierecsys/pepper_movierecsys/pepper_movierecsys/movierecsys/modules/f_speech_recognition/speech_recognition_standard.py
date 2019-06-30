# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 20:15:16 2018

@author: Francesco
"""
import speech_recognition as sr

def speech_recognition(path):

    # NOTE: this requires PyAudio because it uses the Microphone class
    r = sr.Recognizer()
    with sr.WavFile(path) as source:              # use "test.wav" as the audio source
        audio = r.record(source)                        # extract audio data from the file

        try:
            text = r.recognize_google(audio)
            print("Transcription: " + text )   # recognize speech using Google Speech Recognition
        except LookupError:  
                                               # speech is unintelligible
            text = 'I did not understand well!'
            print(text)
    
    return text

#speech_recognition("../test.wav")