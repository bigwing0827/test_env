# ニュース記事のスクレイピングツール

## 概要
[参考:Newspaper3kでニュースサイトの記事を簡単スクレイピング](https://happy-shibusawake.com/newspaper3k/484/)
[参考:Pythonで初心者でも超簡単にWebスクレイピング(newspaper3kでHTMLからテキスト抽出)](https://ai-inter1.com/webscraping_newspaper_1/)

## 必要なライブラリ
- newspaper3k # スクレイピング
- tinysegmenter # newspaper3k日本語のnlp用分かち書き => 
- nltk # tinysegmenterに必要

## 構築
### 仮想環境
```
python3 -m venv .venv
source .venv/bin/activate
```
### ライブラリインストール
```
pip install newspaper3k
pip install tinysegmenter
pip install nltk
pip install tqdm
#  pip freeze > requirements.txt
```
### スクレイピング
```
python3 get_news.py
```



