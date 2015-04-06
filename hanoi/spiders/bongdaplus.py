# coding: utf-8
import glob

from datetime import datetime
from scrapy.contrib.spiders import XMLFeedSpider
from hanoi.items import NewsItem
from hanoi.settings import DIR_FEED_LISTS

# get the list of feeds from the 'feeds' directory in the same directory with this script


arr = [
    # 'http://www.24h.com.vn/upload/rss/bongda.rss',
    # 'http://www.24h.com.vn/upload/rss/thoitrang.rss'
]
tag = []

try:
    # feedLists = glob.glob(DIR_FEED_LISTS + '*')
    feedLists = glob.glob(DIR_FEED_LISTS + 'bongdaplus_*')
    # goes through feeds
    for feedList in feedLists:
        feedFile = open(feedList, 'r')
        feedUrls = feedFile.read().strip().split('\n')
        feedFile.close()

        for feedUrl in feedUrls:
            feedUrlParts = feedUrl.split(' ')
            # start_url
            arr.append(feedUrlParts[0])
            # tag
            tag.append(feedUrlParts[1])
except:
    print "Error: unable to fetch the data"

#use XmlPathSelector (other one is HtmlXPathSelector - for HTML data)
class BongdaplusSpider(XMLFeedSpider):
    name = 'bongdaplus'
    start_urls = arr
    iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
    itertag = 'item'

    def parse_node(self, response, node):
        if node is None :
            return None

        item = NewsItem()
        #extract() - returns a unicode string with the data selected by the XPath selector.
        try:
            item['title'] = node.xpath('//item/title/text()').extract()[0]
            item['desc'] = node.xpath('//item/description/text()').extract()[0]
            item['url'] = node.xpath('//item/link/text()').extract()[0]
            # item['pub_date'] = node.xpath('//item/pubdate/text()').extract()[0]
            # item['image'] = node.xpath('//item/media:content/@url/text()').extract()[0]
            item['tag'] = 'sport'
            item['created_at'] = datetime.now()
        except:
            print item
            print "Error: unable to parse the node"
            return None

        return item