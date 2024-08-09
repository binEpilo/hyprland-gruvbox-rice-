#!/bin/python

# code zum testen der icons:

'''
import os

for i in range(2000):
    os.system(f"wget https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_{i}.svg")
    os.system(f"wget https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_{i}.svg")
'''

import requests
from bs4 import BeautifulSoup
import sys

html = requests.get("https://www.wetter.com/deutschland/wemding/DE0011401.html")
soup = BeautifulSoup(html.content, 'html.parser')
temperature = soup.find(class_="delta rtw_temp").get_text()
soup = soup.find(class_="rtw_icon")

# icons

bewölkt = "󰖐"
hazy = "󰼰"
nebel = "󰖑"
hagel = "󰖒"
blitz = "󰖓"
nacht = "󰖔"
starkregen = "󰖖"
regen = "󰖗"
schnee = "󰖘"
sonne = "󰖙"
sonnenaufgang = "󰖚"
windig = "󰖝"
wolkenwarnung = "󰼯"
wolkenuhr = "󱣶"
sturm = "󰙾"
leichtbewölkt = "󰖕"
teilblitz = "󰼲"
teilregnerisch = "󰼳"
teilschnee = "󰼴"
starkschnee = "󰼶"
schneeregen = "󰙿"
sonnenwarnung = "󰼷"
nachtbewölkt = "󰼱"
teilschneeregen = "󰼵"

# vorsorge für klimawandel

hurricane = "󰢘"
tornado = "󰼸"
alieninvasion = "󰢚"

if soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_0.svg"):
    icon = sonne
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_1.svg"):
    icon = leichtbewölkt 
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_2.svg"):
    icon = leichtbewölkt
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_3.svg"):
    icon = bewölkt
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_4.svg"):
    icon = hazy
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_5.svg"):
    icon = teilregnerisch
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_6.svg"):
    icon = regen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_7.svg"):
    icon = schnee
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_8.svg"):
    icon = teilregnerisch
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_9.svg"):
    icon = blitz
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_10.svg"):
    icon = leichtbewölkt
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_14.svg"):
    icon = teilregnerisch
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_20.svg"):
    icon = leichtbewölkt
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_21.svg"):
    icon = leichtbewölkt
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_30.svg"):
    icon = bewölkt
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_40.svg"):
    icon = hazy
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_45.svg"):
    icon = hazy
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_48.svg"):
    icon = hazy
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_49.svg"):
    icon = hazy
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_50.svg"):
    icon = teilregnerisch
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_51.svg"):
    icon = teilregnerisch
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_53.svg"):
    icon = teilregnerisch
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_55.svg"):
    icon = teilregnerisch
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_56.svg"):
    icon = teilregnerisch
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_57.svg"):
    icon = teilregnerisch
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_60.svg"):
    icon = regen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_61.svg"):
    icon = regen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_63.svg"):
    icon = starkregen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_65.svg"):
    icon = starkregen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_66.svg"):
    icon = regen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_67.svg"):
    icon = starkregen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_68.svg"):
    icon = schneeregen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_69.svg"):
    icon = schneeregen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_70.svg"):
    icon = schnee
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_71.svg"):
    icon = schnee
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_73.svg"):
    icon = starkschnee
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_75.svg"):
    icon = starkschnee
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_77.svg"):
    icon = starkschnee
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_80.svg"):
    icon = teilregnerisch
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_81.svg"):
    icon = teilregnerisch
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_82.svg"):
    icon = teilregnerisch
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_83.svg"):
    icon = teilschneeregen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_84.svg"):
    icon = teilschneeregen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_85.svg"):
    icon = teilschnee
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_86.svg"):
    icon = teilschnee
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_90.svg"):
    icon = blitz
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_95.svg"):
    icon = blitz
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/d_96.svg"):
    icon = blitz
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_0.svg"):
    icon = nacht
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_1.svg"):
    icon = nachtbewölkt
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_2.svg"):
    icon = nachtbewölkt
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_3.svg"):
    icon = bewölkt
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_4.svg"):
    icon = nacht
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_5.svg"):
    icon = regen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_6.svg"):
    icon = regen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_7.svg"):
    icon = schnee
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_8.svg"):
    icon = regen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_9.svg"):
    icon = blitz
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_10.svg"):
    icon = nachtbewölkt
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_20.svg"):
    icon = nachtbewölkt
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_21.svg"):
    icon = nachtbewölkt
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_30.svg"):
    icon = bewölkt
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_40.svg"):
    icon = nacht
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_45.svg"):
    icon = nacht
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_48.svg"):
    icon = nacht
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_49.svg"):
    icon = nacht
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_50.svg"):
    icon = regen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_51.svg"):
    icon = regen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_53.svg"):
    icon = regen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_55.svg"):
    icon = starkregen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_56.svg"):
    icon = regen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_57.svg"):
    icon = starkregen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_60.svg"):
    icon = regen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_61.svg"):
    icon = regen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_63.svg"):
    icon = regen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_65.svg"):
    icon = starkregen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_66.svg"):
    icon = regen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_67.svg"):
    icon = starkregen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_68.svg"):
    icon = schneeregen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_69.svg"):
    icon = schneeregen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_70.svg"):
    icon = schnee
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_71.svg"):
    icon = schnee
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_73.svg"):
    icon = schnee
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_75.svg"):
    icon = starkschnee
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_77.svg"):
    icon = schnee
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_80.svg"):
    icon = regen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_81.svg"):
    icon = regen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_82.svg"):
    icon = starkregen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_83.svg"):
    icon = schneeregen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_84.svg"):
    icon = schneeregen
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_85.svg"):
    icon = schnee
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_86.svg"):
    icon = starkschnee
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_90.svg"):
    icon = blitz
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_95.svg"):
    icon = blitz
elif soup.find(src=f"https://cs3.wettercomassets.com/wcomv5/images/icons/weather/n_96.svg"):
    icon = blitz
else:
    icon = alieninvasion


try:
    if sys.argv[1] == "i":
        print(icon)
    elif sys.argv[1] == "t":
        print(temperature)
except IndexError:
    print(f"{temperature} {icon}")
