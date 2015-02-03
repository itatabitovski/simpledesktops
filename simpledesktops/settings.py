# -*- coding: utf-8 -*-

# Scrapy settings for simpledesktops project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import os

BOT_NAME = 'simpledesktops'

SPIDER_MODULES = ['simpledesktops.spiders']
NEWSPIDER_MODULE = 'simpledesktops.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'simpledesktops (+http://www.yourdomain.com)'

CONCURRENT_REQUESTS = 1
DOWNLOAD_DELAY = 0.50

ITEM_PIPELINES = {
        'scrapy.contrib.pipeline.images.ImagesPipeline': 1
}

IMAGES_STORE = os.getenv('SCRAPY_IMAGES_STORE', '../wallpapers')

if not os.path.exists(IMAGES_STORE):
        os.makedirs(IMAGES_STORE)


