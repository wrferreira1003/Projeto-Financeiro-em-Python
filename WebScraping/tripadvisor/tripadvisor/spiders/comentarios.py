import scrapy

from ..items import TripadvisorItem

class ComentariosSpider(scrapy.Spider):
    name = 'comentarios'
    allowed_domains = ['tripadvisor.com.br']
    start_urls = ['https://www.tripadvisor.com.br/Attraction_Review-g303441-d553398-Reviews-Parque_Barigui-Curitiba_State_of_Parana.html']

    def parse(self, response):
        item = TripadvisorItem()
        quadro_de_comentarios = response.xpath("//*[@id="tab-data-qa-reviews-0"]/div/div[5]/div[1]/span/div")