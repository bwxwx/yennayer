import requests
import json
import sys
import os
import webbrowser
import sys, getopt




print("\033[1;31m     )          )     )              )       (     ")
print("  ( /(       ( /(  ( /(   (       ( /(       )\ )  ")
print("  )\()) (    )\()) )\())  )\      )\()) (   (()/(  ")
print(" ((_)\  )\  ((_)\ ((_)\((((_)(   ((_)\  )\   /(_)) ")
print("__ ((_)((_)  _((_) _((_))\ _ )\ __ ((_)((_) (_))   ")
print("\ \ / /| __|| \| || \| |(_)_\(_)\ \ / /| __|| _ \  ")
print(" \ V / | _| | .` || .` | / _ \   \ V / | _| |   /  ")
print("  |_|  |___||_|\_||_|\_|/_/ \_\   |_|  |___||_|_\  ")
print("                            \033[1;32mcoded by guendouz aimed")
print("                            aimedguendouz@gmail.com\033[0;37m")

                        #get arguments
opts, args = getopt.getopt(sys.argv[1:],"hi:")
for opt, arg in opts:
    if opt == '-h' or opt == '--help':
         print('-m    open maps in the location')
         print('-i    target-ip')
         sys.exit()
    elif opt == '-i' or opt == '--ip':
        ip = arg



url = "http://ip-api.com/json/"
url = url + ip
response = requests.get(url)

r = json.loads(response.text)

for key in r:
        value = r[key]
        print("\033[0;37m" + str(key) + " => \033[0;32m" + str(value))

print('\033[0;37murl => \033[0;32mhttps://www.google.com/maps/@' + str(r["lat"]) + ',' + str(r["lon"]) + ',10z')

if len(sys.argv) > 1 and sys.argv[1] == "-m":
    webbrowser.open('https://www.google.com/maps/@' + str(r["lat"]) + ',' + str(r["lon"]) + ',10z')
