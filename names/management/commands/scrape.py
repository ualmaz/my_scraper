from django.core.management.base import BaseCommand, CommandError
from scrapy.crawler import CrawlerProcess

from scraper_project.tutorial.spiders.quotes_spider import QuotesSpider

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        process = CrawlerProcess()
        process.crawl(QuotesSpider)
        process.start()
