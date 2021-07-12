# -*- coding: utf-8 -*-
import requests
import datetime
import sys
import codecs
from bs4 import BeautifulSoup
#引数チェック
if len(sys.argv) == 2:
    key_word = sys.argv[1]
else:    
    print('第一引数をチェックしてください')
    exit(1)

url_base = 'https://news.yahoo.co.jp/'
url = url_base+'search?p='+key_word+'&ei=utf-8&aq=0'
#requestsを使って、webからURLの情報を取得
r = requests.get(url)
#BeautifulSoupを使って、BeautifulSoupオブジェクトを生成
soup = BeautifulSoup(r.content, 'html.parser')
#BeautifulSoupオブジェクトのうち、タグがaのものをピックアップ
extract_data = soup.find_all('a')
#スクリプト実行日を取得
getday = datetime.date.today()
today = getday.strftime('%Y%m%d')
#csvファイルの名前
csvfile = 'news_pick_up'+'_'+key_word+'_'+today+'.csv'
#csvファイルに情報出力 utf-8でエンコード
with open(csvfile, 'w', encoding='utf-8') as f:
    #ヘッダ情報を出力
    header = 'TITLE'+','+'URL'+'\n'
    f.write(header)
#ピックアップしたaタグデータを一行ずつ出力
for line in extract_data:
    #タグがdivで、classがnewsFeed_item_titleの情報がある場合
    #タイトルと、URLを出力
    newstitle = line.find('div',class_='newsFeed_item_title')
    if newstitle is not None:
        newsurl = line.get('href')
        with open(csvfile, 'a', encoding='utf-8') as f:
            newsinfo = newstitle.text+','+newsurl+'\n'
            f.write(newsinfo)

exit(0)