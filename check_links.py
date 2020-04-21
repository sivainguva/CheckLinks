#!/usr/local/bin/python3
import urllib.parse
import urllib.request
import os.path
import requests
import json
from smtplib import SMTP
from email.mime.text import MIMEText
import email.utils
import smtplib
from cgi import print_directory
from datetime import datetime

def init(args):
    if os.path.isfile(args):
        get_links(args)
    else:
        print(args + "DOES NOT EXIST")

def get_links(file):
    fileData = open(file)
    brokenLinks = {}
    index = 0
    for line in fileData.readlines():
        index = index+1
        tokens = line.strip().split()
        for token in tokens:
            if (token.startswith('http') or token.startswith('https') or token.startswith('www')):
                try:
                    urllib.request.urlopen(token)
                except:
                    print(str(line.index) + " ----- " + token)
                    brokenLinks[index] = token
    
    notify(brokenLinks)

#Send a notification email
def notify(brokenLinks):
    smtpserver='smtp.gmail.com'
    FROM = 'XXXX@gmail.com'
    TO = 'XYYYYY@gmail.com'
    pwd = ''
    SUBJ = 'BrokenLinks - ' + str(datetime.now())
    EMAILBODY = brokenLinks
    server = smtplib.SMTP(smtpserver, 587)
    server.starttls()
    server.login(FROM,pwd)
    server.sendmail(FROM, TO, EMAILBODY)
    server.close()
    print(brokenLinks)
    print('Updated!')

if __name__ == "__main__":
    #Expand this to Excelsheet and to googlesheets
    init('./QuestionnaireandResponses.csv')