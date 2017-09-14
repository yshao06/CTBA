# -*- coding: utf-8 -*-
"""
Created on Tue Sep 05 15:07:20 2017

@author: micsh
"""

""" XML Web Scraping Homework """
import requests
from lxml import objectify

# create a bunch
parameter = "tavg" # average temperature
periods = 6 # 6 month period
state = 44 # representing Virginia
div = 0 # all divisions
month = 8 # August
year = 2016


# designate the url with standardized wording pluscustomized criteria
# which relies on the values defined in prior block
url_fmt = ("https://www.ncdc.noaa.gov/temp-and-precip/climatological-rankings/download.xml?"
            "parameter=%s&state=%s&div=%s&month=%s&periods[]=%s&year=%s")
insertion = (parameter, state, div, month, periods, year)
# the '%s' was inserted with values
url_full = url_fmt % insertion


# extract content from the url
# objectify element names for matching & printing
url_content = requests.get(url_full).content
result = objectify.fromstring(url_content)

# printout values correspond to designated elements
print "W&M username: yshao06"
print "value: ", result.data["value"]
print "twentiethCenturyMean", result.data["twentiethCenturyMean"]
print "lowRank", result.data["lowRank"]
print "highRank",  result.data["highRank"]
