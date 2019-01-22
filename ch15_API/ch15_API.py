# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:19:08 2019

@author: Katharina
"""
import requests
import config


def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox490bc5ef18e6418ba66ef94868d3191c.mailgun.org/messages",
        auth=("api", "config.api_key_mailgun"),
        data={"from": "Excited User <mailgun@sandbox490bc5ef18e6418ba66ef94868d3191c.mailgun.org>",
              "to": ["katie.wiedmann@gmx.de"],
              "subject": "Let's see what's going to happen",
              "text": "It will probably show if it works"})
    
send_simple_message()



