import scrapy


class QuotespiderSpider(scrapy.Spider):
    name = "quotespider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        quotes=response.css('div.quote')
        '''for quote in quotes:
            yield{
                'quote':quote.css('span.text::text').get(),
                'author':quote.css('small.author::text').get()
                
            }'''
        for quote in quotes:
            relative_quote_url=quote.css('span a').attrib['href']
            quote_url='https://quotes.toscrape.com/'+relative_quote_url
            yield response.follow(quote_url,callback=self.parse_quote_page)
        next_page= response.css('li.next a').attrib['href']
        if next_page is not None:
            next_page_url='https://quotes.toscrape.com/'+next_page
            yield response.follow(next_page_url, callback=self.parse)


    def parse_quote_page(self,response):
        author=response.css('div.author-details')
        yield{
            'born':author.css('span.author-born-date::text').get(),
            'born_loc':author.css('span.author-born-location::text').get(),
            'desc':author.css('div.author-description::text').get()


        }