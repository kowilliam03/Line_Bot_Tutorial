# Line Bot 教學

## 大綱
* [1. Line Bot 簡介](#1.-Line-Bot-簡介)
* [2. 建立 channel](#2.-建立-channel)
* [3. 建立開發環境](#3.-建立開發環境)
* [4. 程式撰寫](#4.-程式撰寫)
* [5. 圖文選單](#5.-圖文選單)
* [補充資料](#補充資料)

## 1. Line Bot 簡介
與Line Notify不同的地方是：Line Bot可以回覆用事先設定好的問題。也可以結合其他第三方手提供的API，寫出更有趣的功能。

## 2. 建立 channel
依照[官方文檔](https://developers.line.biz/zh-hant/docs/messaging-api/getting-started/)的指示，到 [Line Developers console](https://developers.line.biz/console/) 建立 channel，並取得 Access Token 及 Channel Secret 。

## 3. 建立開發環境
Line 官方提供的 Python SDK 使用 Flask ，以及我們的程式中需要用到爬蟲，因此也需要安裝 BeautifulSoup 及 Requests

```bash
pip install flask beautifulsoup4 requests line-bot-sdk
```

由於 Line 的 Webhook 要求的 Webhook URL 需要是 HTTPS ，我們在本地端開發、測試時的網址（localhost:5000）不符合要求，因此我們需要使用 [**ngrok**](https://ngrok.com/) 這項工具。

從[**ngrok**](https://ngrok.com/) 官網的右上方註冊且登入後，下載壓縮檔後解壓縮(為了方便，可以將ngrok.exe放到專案的資料中，也可以放在其他想要的位置)。

接著按照[教學](https://dashboard.ngrok.com/get-started/setup/)啟用 **ngork** 。


## 4. 程式撰寫
參考Line官方提供的Python SDK: https://github.com/line/line-bot-sdk-python
> 程式參考 app.py

## 5. 圖文選單
如果我們的機器人有幾個常用的功能，或是需要打比較長的指令時，可以試著使用圖文選單，使用者只需要點擊圖片，即可執行對應的指令。

開啟圖文選單的功能有兩種方法，我們這邊選擇不需要寫程式的方法：前往[這個網址](https://admin-official.line.me/)，登入 Line 帳號後，在網頁左邊找到**圖文選單**，這邊即可進行圖文選單的設定。

## 補充資料 
[什麼是Webhook?](https://medium.com/@justinlee_78563/line-bot-%E7%B3%BB%E5%88%97%E6%96%87-%E4%BB%80%E9%BA%BC%E6%98%AF-webhook-d0ab0bb192be)