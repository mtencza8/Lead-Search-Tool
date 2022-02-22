from email.mime import application
import requests
import json
from typing import cast



with open("info.config") as f:
    contents = f.readlines()

for i in contents:
    if "skrappApiKey" in i:
        apiKey = i
        index = apiKey.index(":")
        apiKey = apiKey[index+1:].strip()





headers = {}
headers['X-Access-Key'] = apiKey
headers['content-type'] = 'application/JSON'

#used to get a list of companies that you can fetch the leads for
def accountData():
    url = "https://api.skrapp.io/api/v2/account/"
    res = requests.get(url, headers=headers)
    jsonResponse = res.json()
    leadLists = jsonResponse['lists']
    
    k = 0
    parseList(leadLists)

    company = int(input("Which company are you look for (Enter number): "))
    listID = leadLists[company-1]['id']

    return listID

        
    

def listData(listID, **options):
    url = "https://api.skrapp.io/api/v2/list/{}".format(listID)
    print(url)
    res = requests.get(url, headers=headers)
    jsonResponse = res.json()
    print(""" 
    
        Company Name:              {}
        Number of Leads:           {}
        Number of Leads w/ emails: {}
    
    """.format(jsonResponse['name'], jsonResponse['count_leads'], jsonResponse['count_leads_emails']))


def isOptions(num, id):
    print(num+id)
    return num+id

def listLeads(listID, **kwargs):
    hasOptions = 0
    
    for key, value in kwargs.items():
        
        if key == 'start':
            start = value
            hasOptions = isOptions(hasOptions,1)
        if key == 'size':
            size = value
            hasOptions = isOptions(hasOptions,4)
        if key == 'kw':
            kw = value
            hasOptions = isOptions(hasOptions,6)
        else:
           continue

    print("Num of Options: {}".format(hasOptions))
            
    if hasOptions == 0:
        url = "https://api.skrapp.io/api/v2/list/{}/leads".format(listID)
    elif hasOptions == 1:
        url = "https://api.skrapp.io/api/v2/list/{}/leads?start={}".format(listID, start)
    elif hasOptions == 4:
        url = "https://api.skrapp.io/api/v2/list/{}/leads?size={}".format(listID, size)
    elif hasOptions == 6:
        url = "https://api.skrapp.io/api/v2/list/{}/leads?kw={}".format(listID, kw)
    elif hasOptions == 5:
        url = "https://api.skrapp.io/api/v2/list/{}/leads?start={}&size={}".format(listID, start,size)
    elif hasOptions == 7:
        url = "https://api.skrapp.io/api/v2/list/{}/leads?start={}&kw={}".format(listID, start, kw)
    elif hasOptions == 10:
        url = "https://api.skrapp.io/api/v2/list/{}/leads?size={}&kw={}".format(listID, size, kw)
    elif hasOptions == 1:
        url = "https://api.skrapp.io/api/v2/list/{}/leads?start={}&size={}kw=&{}".format(listID, start, start, size, kw)


   
    res = requests.get(url, headers=headers)
    
    jsonResponse = res.json()
    parseList(jsonResponse)
    

def parseList(leadDict):
    data = leadDict['data']
    k = 0 
    
    for i in data:
        print("{}: {}".format(k+1, data[k]['name']))
        k=k+1
    


id = '4950966'


    


