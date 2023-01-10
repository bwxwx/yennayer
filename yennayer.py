import requests
import json
import sys
import os
import webbrowser

print("usage: -m => open maps in the location")

ip = input('ip : ')
url = "http://ip-api.com/json/"
url = url + ip
response = requests.get(url)

r = json.loads(response.text)

print("country     : " + r["country"])
print("countryCode : " + r["countryCode"])
print("region      : " + r["region"])
print("region name : " + r["regionName"])
print("location    : latitude -> " + str(r["lat"]) + "| longitude -> " + str(r["lon"]))
print("timezone    : " + r ["timezone"])
print('url => https://www.google.com/maps/@' + str(r["lat"]) + ',' + str(r["lon"]) + ',10z')
 
if len(sys.argv) > 1 and sys.argv[1] == "-m":
    webbrowser.open('https://www.google.com/maps/@' + str(r["lat"]) + ',' + str(r["lon"]) + ',10z')
    
    

    