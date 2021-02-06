from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta']


class Stock:
    def __init__(self, stock_numbers):
        self.stock_numbers = stock_numbers
        print(self.stock_numbers)

    def daliy(self, year, month):
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get(
            "https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY_AVG.html")

        select_year = Select(browser.find_element_by_name("yy"))
        select_year.select_by_value(year)  # 選擇傳入的年份

        select_month = Select(browser.find_element_by_name("mm"))
        select_month.select_by_value(month)  # 選擇傳入的月份

        stockno = browser.find_element_by_name("stockNo")  # 定位股票代碼輸入框

        if len(self.stock_numbers) <= 1:
            row = 1
            col = 1
        elif len(self.stock_numbers) <= 2:
            row = 1
            col = 2
        elif len(self.stock_numbers) <= 4:
            row = 2
            col = 2
        else:
            row = 2
            col = 3

        nums = ""
        j = 1
        for stock_number in self.stock_numbers:
            stockno. clear()
            stockno.send_keys(stock_number)
            stockno.submit()

            time.sleep(2)

            soup = BeautifulSoup(browser.page_source, "html.parser")

            table = soup.find("table", {"id": "report-table"})

            elements = table.find_all(
                "td", {"class": "dt-head-center dt-body-center"})

            x = []
            y = []

            print(stock_number+":")
            for index, element in enumerate(elements):
                if index % 2 == 0:    # 偶數為日期
                    date = element.getText()
                    if date != "月平均收盤價":
                        x.append(date.split("/")[2])
                    else:
                        x.append(date)
                else:
                    print(date, element.getText())
                    y.append(element.getText())

            # print(x[:-1])
            # print(y[:-1])
            yn = [float(yy) for yy in y[:-1]]
            plt.subplot(row, col, j)
            plt.xlabel("日期", loc="right")
            plt.ylabel("收盤價", loc="top")
            plt.title(stock_number)
            plt.plot(x[:-1], yn)
            nums = nums+stock_number+" "
            j += 1

        browser.quit()
        plt.suptitle(year+"年"+month+"月 收盤價走勢圖")
        plt.show()


in_nos = []
i = 0
while True:
    in_no = input("請輸入股票代碼(輸入\"e\"結束)：")
    if in_no == 'e':
        break
    else:
        in_nos.append(in_no)

stock = Stock(in_nos)

in_year = input("請輸入西元年份：")
in_month = input("請輸入月份：")
stock.daliy(in_year, in_month)

"""
可以試的代碼:
0051
0052
0053
0054
0055
0056
"""
