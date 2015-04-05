# coding: utf-8

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector

from hanoi.items import StockItem


class StockSpider(CrawlSpider):
    name = 'stock'
    allowed_domains = ['stocks.finance.yahoo.co.jp']
    start_urls = [
        'http://stocks.finance.yahoo.co.jp/stocks/qi/?js=%E3%81%82',
    ]
    rules = [
        # xpathに一致する条件でページ遷移
        # followがTrueだと、遷移先のページでもrulesを適応する
        Rule(SgmlLinkExtractor(restrict_xpaths =(u'//a[contains(text(), "次の20")]', )), 'parse_stock', follow=True)
    ]

    def parse_start_url(self, response):
        yield self.parse_stock(response)

    def parse_stock(self, response):
        # HTTPのレスポンスをxPathセレクタにする
        sel = Selector(response)

        # 指定クラスに一致する条件の表の列から、銘柄コードと名前を取得し保存する
        for tr in sel.xpath('//tr[@class="yjM"]'):
            # 保存する情報をインスタンス化
            item = StockItem()
            item['stock_id'] = tr.xpath('td[1]/*/text()').extract()[0]
            item['name'] = tr.xpath('td[3]/strong/a/text()').extract()[0]
            yield item