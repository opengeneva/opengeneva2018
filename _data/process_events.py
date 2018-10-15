''' this script is aimed at processing event pages from the .csv export'''
# modules
import urllib2
import csv
import re
import os, shutil

# functions

def clean_events():
    folder = '../_events'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)
        print file_path

# retrieve data

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQKDxZ6WmIs3cI-wp0No87fzcyVU_hkv40x-Ts5yA6TmCfU1ZrvoalXzhCRFaHgCBLd3AgksTWlyvQD/pub?gid=1001063161&single=true&output=csv"
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQKDxZ6WmIs3cI-wp0No87fzcyVU_hkv40x-Ts5yA6TmCfU1ZrvoalXzhCRFaHgCBLd3AgksTWlyvQD/pub?gid=1001063161&single=true&output=tsv"
response = urllib2.urlopen(url)
csvFile = response.read()

lines = csvFile.split("\r\n")

clean_events()

for i,line in enumerate(lines):

    if i==0:
        headers = line.split("\t")
        continue

    cells = line.split("\t")

    if cells[1] == "FALSE":
        continue

    file = open("../_events/%s_%s.md"%(cells[2],re.sub("[\s:,#'\"&]","_",cells[5])),'wb')

    file.write("---\nlayout: events\n")
    file.write("fileroot : %s_%s\n"%(cells[2],re.sub("[\s:,#'\"&]","_",cells[5])))
    for j,header in enumerate(headers):
        try:
            file.write("%s : %s\n"%(header,cells[j]))
        except:
            continue

    file.write("---")

file.close()

'''
title:  "Open Geneva Acceleration Partnerships"
date:   2018-03-14 00:00:00 +0200
categories: news
lang: en
published: true
permalink: /acceleration/
---
'''
