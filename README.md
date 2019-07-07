# TrelloTodoExport 

TrelloTodoExport 是使用python撰寫的一個小程式，可以幫助我們更迅速整理 Trello 中的待辦清單。
透過 Trello 匯出 .JSON 功能，整理此看板中待辦清單如下圖，使看板管理者清楚知道有 TodoList 狀態以及所負責的人。
![alt text](https://github.com/dt9250810/TrelloTodoExport/blob/master/1.png)
亦提供 LINE Notifier 針對不同人員的待辦清單分類，傳送至 LINE，格式可參考：
![alt text](https://github.com/dt9250810/TrelloTodoExport/blob/master/2.png)

## 使用方法

1. 先將需要整理的看板匯出 .json 並置放於與 TrelloTodoExport 相同目錄，檔案命名為：trello.json
2. 執行 TrelloTodoExport.py ， test_trello.csv 即會產生於此目錄下
3. 若需使用 LINE Notifier，需搭配 IFTTT 服務並在程式中的 LINE_KEY 填入相關 Key 字串(詳可參見
https://notify-bot.line.me/zh_TW/
、https://ifttt.com/)。


