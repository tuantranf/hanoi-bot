# -*- coding: utf-8 -*-

# Scrapy settings for hanoi project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'hanoi'

SPIDER_MODULES = ['hanoi.spiders']
NEWSPIDER_MODULE = 'hanoi.spiders'

# Store scraped item in mongodb for post-processing.
ITEM_PIPELINES = {
    'scrapy_mongodb.MongoDBPipeline': 300
}


MONGODB_URI = 'mongodb://localhost:27017'
MONGODB_DATABASE = 'hanoi_web'
MONGODB_COLLECTION = 'items'
MONGODB_UNIQUE_KEY = 'url'
# MONGODB_ADD_TIMESTAMP = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'hanoi (+http://www.google.com)'

# ダウンロードする間隔（秒）の指定
DOWNLOAD_DELAY = 3

DIR_FEED_LISTS = 'feed-lists/'