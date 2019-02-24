# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BtcItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	height = scrapy.Field()
	hash_ = scrapy.Field()
	time = scrapy.Field()
	receive_time = scrapy.Field()
	relayed_by = scrapy.Field()
	difficulty = scrapy.Field()
	bits = scrapy.Field()
	transations = scrapy.Field()
	output = scrapy.Field()
	volume = scrapy.Field()
	fees = scrapy.Field()
	size = scrapy.Field()
	version = scrapy.Field()
	merkle_root = scrapy.Field()
	nonce = scrapy.Field()
	reward = scrapy.Field()
