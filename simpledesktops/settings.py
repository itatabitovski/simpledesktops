# -*- coding: utf-8 -*-

# Scrapy settings for simpledesktops project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import os
print os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

BOT_NAME = 'simpledesktops'

SPIDER_MODULES = ['simpledesktops.spiders']
NEWSPIDER_MODULE = 'simpledesktops.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'simpledesktops (+http://www.yourdomain.com)'

CONCURRENT_REQUESTS = 1
DOWNLOAD_DELAY = 0.50

ITEM_PIPELINES = {
    'simpledesktops.pipelines.SimpledesktopsPipeline',
}
