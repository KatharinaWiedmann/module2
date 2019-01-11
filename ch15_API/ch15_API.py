# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 14:00:43 2019

@author: Katharina
"""

#to make this work, items in CAPITALS need to be inserted 

import requests

def send_simple_message():
    return requests.post(
        "API-KEY",
        auth=("api", "API-KEY"),
        data={"from": "Excited User <E-Mail ADDRESS>",
              "to": ["E-Mail ADDRESS"],
              "subject": "Let's see what's going to happen",
              "text": "It will probably show if it works"})
    
send_simple_message()