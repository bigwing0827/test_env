import newspaper
import nltk
import time
import random
import re
import csv
import datetime
from tqdm import tqdm
import settings

def request(URL,max_num):
    i = 0
    article_data = []
    ##
    news_info =newspaper.build(URL, memoize_articles=False)
    for i in tqdm(range(max_num)):
        wait_time = random.uniform(5,8) # 5-8秒/１回間隔でリクエスト
        ##
        article = news_info.articles[i]
        article.download() # 記事のダウンロード
        article.parse() # 記事を解析
        #nltk.download("punkt")
        #article.nlp() # 自然言語処理を実行 日本語対応不可
        article_data.append(article)
        ##
        time.sleep(wait_time)
        i += 1
        ##
    return article_data

def Output_Print(article_data):
    for article in article_data:
        print("タイトル: ",article.title)
        print("URL: ",article.url)
        print("出版日: ",article.publish_date)
        print("内容: ",article.text[0:150]+"....")
        #print("キーワード: ",article.keywords) # キーワード (要nlp)
        #print("まとめ: ",article.summary) # サマリー (要nlp)
        print("その他: ",article.meta_data)
        print("文字数: {}字".format(len(article.text)))
        print()
    return

def Output_CSV(article_data,site_name):
    csv_date = datetime.datetime.today().strftime("%Y%m%d")
    csv_file_name = site_name + "_" + csv_date + ".csv"
    ##
    header = ["Title","Publish_date","Text","URL"]
    csvlist = []
    for article in article_data:
        body_text = article.text.replace('\n', '')
        body_text = body_text.replace('\r', '')
        ##
        article_data= []
        article_data.append(article.title)
        article_data.append(article.publish_date)
        article_data.append(body_text)
        article_data.append(article.url)
        csvlist.append(article_data)
    ##
    with open(csv_file_name, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(csvlist)
    return


if __name__ == '__main__':
    max_num = settings.max_num
    site_info = settings.site_info
    ##
    article_data = request(site_info["URL"],max_num)
    #Output_Print(article_data)
    Output_CSV(article_data,site_info["SITE_NAME"])
