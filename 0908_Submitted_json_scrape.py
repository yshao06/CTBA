# -*- coding: utf-8 -*-
"""
Created on Fri Sep 08 08:40:05 2017

@author: micsh
"""

""" JSON Web Scraping Assignment"""

import requests

my_wm_username = "yshao06"
# Extract data from the link
search_url = 'http://buckets.peterbeshai.com/api/?player=201939&season=2015'
response = requests.get(search_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})

numJumpShotsAttempt = 0
numJumpShotsMade = 0
percJumpShotMade = 0.0

# For each record, count if the action_type is "Jump Shot", and if the shot was successfully made
for shot in response.json():
    if shot['ACTION_TYPE'] == "Jump Shot":
        numJumpShotsAttempt = numJumpShotsAttempt + 1
        if shot['EVENT_TYPE'] == "Made Shot":
            numJumpShotsMade = numJumpShotsMade + 1

# Calculate the rate of jump shot made successfully
percJumpShotMade = float(numJumpShotsMade) / numJumpShotsAttempt
            
print my_wm_username
print numJumpShotsAttempt
print numJumpShotsMade
print percJumpShotMade