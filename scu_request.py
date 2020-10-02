import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


def getTable(id, passwd):
    r = requests.post('https://web.sys.scu.edu.tw/login0.asp', data={'id':id,'passwd':passwd})

    r.cookies.set('parselimit', 'Infinity')
    n = requests.get('https://web.sys.scu.edu.tw/SelectCar/selcar81.asp', cookies = r.cookies, data={'procsyear':'109',
                                                                                                     'procterm':'1'})
    n.encoding = 'big5'
    soup = BeautifulSoup(n.text,"html.parser") #將網頁資料以html.parser
    trs = soup.find_all('tr')

    df = pd.DataFrame(index=['1', '2', '3', '4', 'E', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D'], #處理Rows
                  columns=['禮拜一', '禮拜二', '禮拜三', '禮拜四', '禮拜五', '禮拜六', '禮拜日']) #處理columns
    count = 0

    for tr in trs:
        tds = tr.find_all('td')
        col_count = 0
        if count > 5:
            trName = str(count - 1)
        else:
            trName = str(count)
        if count == 5: #非輸字節數處理
            trName = "E"
        elif count == 11:
            trName = 'A'
        elif count == 12:
            trName = 'B'
        elif count == 13:
            trName = 'C'
        elif count == 14:
            trName = 'D'

        for td in tds:
            tdTxt = str(td.text)

            if col_count == 1:
                df.at[trName, '禮拜一'] = tdTxt
            elif col_count == 2:
                df.at[trName, '禮拜二'] = tdTxt
            elif col_count == 3:
                df.at[trName, '禮拜三'] = tdTxt
            elif col_count == 4:
                df.at[trName, '禮拜四'] = tdTxt
            elif col_count == 5:
                df.at[trName, '禮拜五'] = tdTxt
            elif col_count == 6:
                df.at[trName, '禮拜六'] = tdTxt
            elif col_count == 7:
                df.at[trName, '禮拜日'] = tdTxt
            col_count = col_count + 1
        count = count + 1
    return df