import feedparser
from flask import render_template
from flask import request
from app import app

RSS_FEEDS = {
    'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
    'cnn': 'http://rss.cnn.com/rss/edition.rss',
    'fox': 'http://feeds.foxnews.com/foxnews/latest',
    'iol': 'http://www.iol.co.za/cmlink/1.640'
    }
    

# @app.route("/")
# #@app.route("/bbc")
# def bbc():
#     return get_news('bbc')

# @app.route("/cnn")
# def cnn():
#     return get_news('cnn')

@app.route("/")
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_FEEDS:
        publication = "bbc"
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template('home.html', articles=feed['entries'])


