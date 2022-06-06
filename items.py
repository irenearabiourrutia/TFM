# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DataspiderItem(scrapy.Item):
    Reviews(scrapy.Item):
    Comentario=scrapy.Field()
    Estrellas=scrapy.Field()
    Fecha=scrapy.Field()
    Banco=scrapy.Field()
    Producto=scrapy.Field()
    Tipo=scrapy.Field()
    Votos=scrapy.Field()
    Puntuacion=scrapy.Field()
    PorRecomendacion=scrapy.Field()
    Votos2=scrapy.Field()
    Usuario=scrapy.Field()


class Questions(scrapy.Item):
    TituloPregunta=scrapy.Field()
    NumeroRespuestas=scrapy.Field()
    TextoPregunta=scrapy.Field()
    NumeroVisitas=scrapy.Field()
    Fecha=scrapy.Field()
    Tema=scrapy.Field()


class Comments(scrapy.Item):
    Fecha=scrapy.Field()
    Comentario=scrapy.Field()
    Tema=scrapy.Field()
    Foro=scrapy.Field()
    Respuestas=scrapy.Field()
    Palabrasclave=scrapy.Field()
