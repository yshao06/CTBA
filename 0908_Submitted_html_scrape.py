# -*- coding: utf-8 -*-
"""
Created on Fri Sep 08 00:34:08 2017

@author: micsh
"""

# Import regular expression and BeautifulSoup package
import requests
from bs4 import BeautifulSoup as bsoup

# Request contents from the url
my_wm_username = 'yshao06'
search_url = 'http://publicinterestlegal.org/county-list/'
response = requests.get(search_url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}).content

# Parse the url content using bsoup and compile all attributes of 'tr'
parsed_url = bsoup(response, 'lxml')
target_rows = parsed_url.find_all('tr')

# Create an empty list to append all the results
result_list = []
# Go into each block of 'tr', which contains 'County', 'State' and 'Registration Rate'
# Create an empty list to compile data from each row
for row in target_rows:
    record = []
# In each block, iterate through 'td' to extract value
# The .text.encode function convert unicode into ascii to get rid of the 'u'
# Append the value to the list of row, and further append the row to the master list
    for x in row.find_all('td'):
        record.append(x.text.encode("ascii", 'ignore'))
#        for y in x.find_all('strong'):
#            record.append(y.text.encode("ascii", 'ignore'))
    result_list.append(record)

# Print out all results as required
print my_wm_username
print len(result_list)
print result_list
