import scrapy
import re
from items import Reviews
from scrapy.linkextractors import LinkExtractor


class OpiSpider(scrapy.Spider):
    name = 'OpiSpider'
    allowed_domains = ['helpmycash.com']
    start_urls=["https://www.helpmycash.com/opiniones"]
    for i in range(2,3844):
        start_urls.append("https://www.helpmycash.com/opiniones?page="+str(i))

    def parse(self, response):
        
        nuopinion=len(response.xpath(".//div[@class='card card-review-list mb-4 ']"))
        for i in range (1, nuopinion):
            opinion=response.xpath("//div[@class='card card-review-list mb-4 ']"+str([i]))
            for opi in opinion:
                item=Reviews()
                item['Comentario']=opi.xpath(".//div[@class='card-text my-3']/text()").extract()
                item['Estrellas']=len(opi.xpath(".//i[@class='fa fa-star active']"))
                item['Fecha']=opi.xpath(".//span[@class='small text-muted']/text()").extract()
                item['Banco']=opi.xpath(".//img[@class='img-thumbnail']/@alt").extract()
                item['Producto']=opi.xpath(".//a[@class='pr-3']/text()").extract()
                item['Usuario']=opi.xpath(".//span[@class='small text-muted']//strong/text()").extract()
                url = opi.xpath(".//div[@class='text-center text-md-left d-md-flex justify-content-md-between']//a/@href").extract_first()
                yield scrapy.Request(url, meta={"item": item}, callback=self.parse_details,dont_filter=True)
                
    def parse_details(self, response):

        item = response.meta["item"]
        item['Votos']=response.xpath(".//span[@class='ml-2']//@data-count").extract()
        item['Votos2']=response.xpath(".//span[@class='ml-2']/text()").extract()
        item['Puntuacion']=response.xpath(".//span[@class='font-weight-bold']/text()").extract()
        item['PorRecomendacion']=response.xpath(".//p[@class='lead mt-2']/text()").extract()
        item['Tipo']=response.xpath(".//li[@class='breadcrumb-item']//a//span/text()").extract()
        yield item
