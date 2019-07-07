#!/usr/bin/python3
# -*- coding:utf8 -*-
import csv
import json
import codecs
import requests
#############################################

LINE_KEY = ''

#############################################
dictName = {}
conn_string = json.loads(open('trello.json', encoding = 'utf8').read())

f = csv.writer(open("test_trello.csv", "w", encoding="utf_8_sig",newline=""))

f.writerow(["負責人", "待辦事項", "狀態", "看板類別", "卡片網址", "建立日期"])

checklists = conn_string["checklists"]
cards = conn_string["cards"]
actions = conn_string["actions"]
_lists = conn_string["lists"]

for checklist in checklists:
        for checkItem in checklist["checkItems"]:
                cardName = ""
                cardShortUrl = ""
                # 卡片看板類別
                listName = ""
                # 卡片建立日
                createDate = ""
                # 看板名
                _list = ""
                for card in cards:
                        if(card["id"]==checklist["idCard"]):
                                cardName = card["name"]
                                cardShortUrl = card["shortUrl"]
                for action in actions:
                        if((action["type"]) == "createCard"):
                                if (checklist["idCard"]) == (action["data"]["card"]["id"]):
                                        createDate = action["date"]
                                        listName = action["data"]["list"]["name"]
                                        print(action["data"]["board"]["id"])
                if checklist["name"] in dictName:
                        dictName[checklist["name"]] += '\n - ' + checkItem["name"] + '\n[' + cardName + '] ' + cardShortUrl
                else:
                        dictName[checklist["name"]] = '\n - ' + checkItem["name"] + '\n[' + cardName + '] ' + cardShortUrl

                print('- ' + checkItem["name"] + '\n[' + cardName + '] ' + cardShortUrl)
                f.writerow([checklist["name"], checkItem["name"], checkItem["state"], cardName, cardShortUrl, createDate, listName])


for x in dictName:
        str = x + dictName[x]
        my_data = {'value1': str}
        r = requests.post('https://maker.ifttt.com/trigger/line/with/key/' + LINE_KEY, data = my_data)

print("Export OK")



