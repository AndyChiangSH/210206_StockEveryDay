# 210206_stockEveryDay

###### tags: `Python` `爬蟲`

> [name=AndyChiang][time=Sat, Feb 6, 2021 9:33 AM][color=#00CDAF]

[![hackmd-github-sync-badge](https://hackmd.io/WaqSJuPXTqCbrnbdiZ0_fA/badge)](https://hackmd.io/WaqSJuPXTqCbrnbdiZ0_fA)

## 功能
這是爬取 ==台灣證券交易所== 的 [個股日收盤價及月平均價](https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY_AVG.html) 的程式。

因為此網站是檔名html，加上查詢系統，很適合拿來練習==查詢式網頁爬蟲==。

**此程式可以幫抓出指定股票在指定年月的當月收盤價，並製成圖表方便使用者比較。**

## 使用步驟
1. 使用前請先安裝好必要的套件：
在windows搜尋 **"命令提示字元"**，打開後檢查一下路徑是否為 **C:\Users\<你的電腦名稱>>** ，如果不是請輸入 `cd C:\Users\<你的電腦名稱>>`，移動到該位置。
接著在指令框輸入以下指令，我順便提一下每個套件的功能：
* Beautiful Soup：美化排版以及分析網站。
```
pip install beautifulsoup4
```
* Selenium：模擬使用者行為。
```
pip install selenium
```
* Webdriver-manager：在執行程式間，自動下載瀏覽器的驅動程式。
```
pip install webdriver-manager
```
* Matplotlib：畫出美美的圖~
```
pip install matplotlib
```

2. 在 VScode 打開 `scraper.py` ，接著執行。
3. 然後在 terminal 輸入你要查詢的==股票代碼==，可以輸入多個，但因為繪圖的排版問題，**盡量在6筆資料以內**，輸入完後輸入 `e` 結束。
4. 接著輸入==年份==，以及==月份==。這邊我沒做防呆，輸入錯誤的話就直接重新執行吧XD。
5. 放著等電腦跑，你會看到程式自動開啟Chrome(預設都是用Chrome，但也可以改)，瀏覽器上會顯示"目前被自動控制..."，此時麻煩不要亂點，抓完資料會自動關閉瀏覽器。
6. 然後，神奇的事就發生了!
7. 電腦會出現==當月收盤價的走勢圖==，而 terminal 則會顯示==文字資料==以及==當月平均收盤價==，恭喜你成功囉!

* 走勢圖：

![](https://i.imgur.com/tOdY2ct.png)
* 文字資料：

![](https://i.imgur.com/ghfo69X.png)


## 教學
> 有空一定寫XD

![](https://i.imgur.com/YMDLKaq.png)

## 相關文章
* [Python 靜態網頁爬蟲](/ZAdxgQ5aR6mhJ6KWEdll1g)

## 參考網址
* [[Python爬蟲教學]學會使用Selenium及BeautifulSoup套件爬取查詢式網頁](https://www.learncodewithmike.com/2020/08/python-integrate-selenium-and-beautifulsoup.html)
* [Selenium 使用 CSS locator 定位 HTML element](https://jzchangmark.wordpress.com/2015/03/16/selenium-%E4%BD%BF%E7%94%A8-css-locator-%E5%AE%9A%E4%BD%8D%E5%85%83%E4%BB%B6/)
