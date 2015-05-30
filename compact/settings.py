# -*- coding: utf-8 -*-

# Scrapy settings for compact project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'compact'

SPIDER_MODULES = ['compact.spiders']
NEWSPIDER_MODULE = 'compact.spiders'
ITEM_PIPELINES = {
    'compact.pipelines.JsonWriterPipeline'
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'compact (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36'

