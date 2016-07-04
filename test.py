# coding: utf-8

import feedparser

url = "http://okuzawats.com/feed"

response = feedparser.parse(url)

print response.feed.title
print response.feed.link

