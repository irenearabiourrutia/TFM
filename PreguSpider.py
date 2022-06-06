# -*- coding: utf-8 -*-
import scrapy
import re
from items import Questions
from scrapy.linkextractors import LinkExtractor


class PreguspiderSpider(scrapy.Spider):
    name = 'PreguSpider'
    allowed_domains = ['helpmycash.com']
    start_urls = ["http://helpmycash.com/preguntas/"]

    for i in range(2,1065):
        start_urls.append("https://www.helpmycash.com/preguntas?page="+str(i))

    def parse(self, response):
        
        numpregunta=len(response.xpath(".//div[@class='card card-forum-list mb-4']"))
        for i in range (1, numpregunta):
            pregunta=response.xpath("//div[@class='card card-forum-list mb-4']"+str([i]))
            for pre in pregunta:
                item=Questions()
                item['TituloPregunta']=pre.xpath(".//a[@class='d-block']/text()").extract()
                item['NumeroRespuestas']=pre.xpath(".//li[@class='list-inline-item text-center text-success']/text()").extract()               
                item['NumeroVisitas']=pre.xpath(".//li[@class='list-inline-item text-center text-warning']/text()").extract()
                item['Fecha']=pre.xpath(".//span[@class='d-block small text-muted']/text()").extract()
                item['Tema']=pre.xpath(".//a[@class='tagged']/@title").extract()
                url = pre.xpath(".//a[@class='d-block']/@href").extract_first()
                yield scrapy.Request(url, meta={"item": item}, callback=self.parse_details,dont_filter=True)
                
    def parse_details(self, response):

        item = response.meta["item"]
        item['TextoPregunta']=response.xpath(".//div[@class='card-text speakable-headline']//text()").extract()
        yield item

