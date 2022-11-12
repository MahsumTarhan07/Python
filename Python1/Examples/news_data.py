
import feedparser
"""
    cnn'den son dakika haberlerini çekme.
    Terminalde  pip install feedparser  yapıp çalıştırsanız yeterli olacaktır
"""

url = "http://www.cnnturk.com/feed/rss/news"
news = feedparser.parse(url)

i=0

for news in news.entries:
    i+=1
    print(i)
    print(news.title)
    print(news.link)
    print(news.summary)
    print("\n")