# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 16:07:52 2018

@author: Francesco & Piero
"""
def require_config(): 
    return {
        # Facebook Token Test movierecsys
        'facebook_token': 'EAAE0Lnad6ywBAGrnw7jHREnIc0CiZAuOpLV8iykP1WOFS8ykXFeoLm4340Js0ZCmZCdZAH6wwpkV6Lr5PoeWZA7b8miJP9vUjfWerd8rF9v95ORNWhdMPUFJmjZBhl4nxW0DDaCImlZBjgqYFpewFhHtVAiHkMBbgKgVVwT7E2lswZDZD',
        # Telegram Token TestMovieRecSys
        'telegram_token': '422658992:AAH1c7kkVvuAIIuVDbbek7Mo4Zd0pKSU8nM',
        # The timezone setting, Guzzle suggests having this for proper requests/responses
        'timezone': 'Europe/Rome',
        # If no response is found, this will be used as response
        'default_fallback_response': 'Sorry, could you repeat that?',
        # Greeting string
        'greeting': "I'm a movie recommender system.\n" +
                "I'm able to suggest you movies ðŸŽ¬ according to your preferences ðŸ˜‰\n" +
                "I need at least 3 preferences for generating recommendations ðŸ˜‰",
        # Facebook payload returned from "Start" button
        'getStartedPayload': "get_started",
        # Base URI (Altieri)
        #'base_uri': '90.147.102.235:8080', #MODIFICABILE
        'base_uri': '193.204.187.192:8081', #MODIFICABILE
        # Server application URI (Altieri)
        #'application_uri': '/movierecsysservice', #MODIFICABILE
        'application_uri': '/movierecsysservice_pepper', #MODIFICABILE
        # Default photo to send if the provided one is not valid
        'default_photo': 'https://bytebucket.org/lu_na/movierecsystelegram/raw/722f6bf618a3d9342c678c878ee60a593d08721b/recsysbot/images/default.jpg?token=8b07161012a8adb6134efa50aa5c98a2b0bd4ba0'
    }

