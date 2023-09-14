import scrapy
from scrapy.loader import ItemLoader
from quotes_scraper.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["toscrape.com"]
    start_urls = ['http://quotes.toscrape.com/']
    pages_crawled: int = 0
    max_pages: int = 6


    def parse(self, response):
        self.logger.info('Parse function called on {}'.format(response.url))
        quotes = response.css('div.quote')

        if self.pages_crawled <= self.max_pages:
            self.pages_crawled += 1
            for quote in quotes:
                loader = ItemLoader(item=QuoteItem(), selector=quote)
                loader.add_css('quote_content', '.text::text')
                loader.add_css('tags', '.tag::text')
                loader.add_value('page', response.url)
                quote_item = loader.load_item()
                author_url = quote.css('.author + a::attr(href)').get()
                # go to the author page and pass the current collected quote info
                yield response.follow(author_url, self.parse_author, meta={'quote_item': quote_item})

            # go to Next page
            for a in response.css('li.next a'):
                yield response.follow(a, self.parse)

    def parse_author(self, response):
        quote_item = response.meta['quote_item']
        loader = ItemLoader(item=quote_item, response=response)
        loader.add_css('author_name', '.author-title::text')
        loader.add_css('author_birthday', '.author-born-date::text')
        loader.add_css('author_bornlocation', '.author-born-location::text')
        loader.add_css('author_bio', '.author-description::text')
        yield loader.load_item()