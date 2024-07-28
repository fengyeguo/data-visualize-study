import scrapy
from scrapy.exceptions import CloseSpider
from bookscraper.items import BookItem

class BookspiderSpider(scrapy.Spider):
    name = 'bookspider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    item_count = 0

    def parse(self, response):
        books = response.css('article.product_pod')

        self.item_count +=1
        if self.item_count > 2:
            raise CloseSpider('item_count达到2，停止爬虫')

        for idx,book in enumerate(books):
            if idx > 2 : break

            relative_url = book.css('h3 a::attr(href)').get()

            if relative_url is not None :
                if 'catalogue/' in relative_url:
                    book_detail_url = 'http://books.toscrape.com/' + relative_url
                else:
                    book_detail_url = 'http://books.toscrape.com/catalogue/' + relative_url
                yield response.follow(book_detail_url, callback = self.parse_book_page)

        next = response.css(".next a::attr(href)").get()
        if next is not None:
            if 'catalogue/' in next:
                next_page_url = 'http://books.toscrape.com/' + next 
            else:
                next_page_url = 'http://books.toscrape.com/catalogue/' + next 
            yield response.follow(next_page_url, callback = self.parse)

    def parse_book_page(self,response):
        table_rows =  response.css("table tr")
        book_item = BookItem()

        book_item['url'] = response.url
        book_item['title'] = response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get()
        book_item['product_type'] = table_rows[1].css("td ::text").get()
        book_item['price_exl_tax'] = table_rows[2].css("td ::text").get()
        book_item['price_inc_tax'] = table_rows[3].css("td ::text").get()
        book_item['tax'] = table_rows[4].css("td ::text").get()
        book_item['availability'] = table_rows[5].css("td ::text").get()
        book_item['number_reviews'] = table_rows[6].css("td ::text").get()
        book_item['stars'] = response.css("p.star-rating").attrib["class"]
        book_item['category'] = response.xpath("//ul[@class='breadcrumb']//li[@class='active']/preceding-sibling::li[1]/a/text()").get()
        book_item['description'] = response.xpath("//div[@id='product_description']/following-sibling::p/text()").get()
        book_item['price'] = response.xpath("//div[@class='col-sm-6 product_main']/p[@class='price_color']/text()").get()

        yield book_item

