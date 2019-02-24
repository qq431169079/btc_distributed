# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from btc.items import *
from lxml import etree

class BtcSpider(scrapy.Spider):
	name = 'Btc'
	allowed_domains = ['www.blockchain.com']
	start_urls = ['https://www.blockchain.com/btc/blocks/1541039032694']

	def parse(self, response):
		doc = etree.HTML(response.text)
		trs = doc.xpath('//table[@class="table table-striped"]/tr')
		for tr in trs[1:]:
			url = 'https://www.blockchain.com' + tr.xpath('td/a/@href')[0]
			yield Request(url, callback=self.parse_page)

		next_page = doc.xpath('//h2[@align="center"]/a[2]/@href')
		if next_page:
			next_url = 'https://www.blockchain.com' + next_page[0]
			if next_url != 'https://www.blockchain.com/btc/blocks/1555899832694':
				yield Request(next_url, callback=self.parse)


	def parse_page(self, response):
		doc = etree.HTML(response.text)
		item = BtcItem()
		try:
			item['time'] = doc.xpath('//table[@class="table table-striped"]/tr[6]/td[2]/text()')[0]
		except:
			item['time'] = ''
		try:
			item['height'] = doc.xpath('//table[@class="table table-striped"]/tr[2]/td[2]/a/text()')[0]
		except:
			item['height'] = ''
		try:
			item['hash_'] = doc.xpath('//table[@class="table table-striped"]/tr[3]/td[2]/a/text()')[0]
		except:
			item['hash_'] = ''
		try:
			item['receive_time'] = doc.xpath('//table[@class="table table-striped"]/tr[7]/td[2]/text()')[0]
		except:
			item['receive_time'] = ''
		try:
			item['relayed_by'] = doc.xpath('//table[@class="table table-striped"]/tr[8]/td[2]/a/text()')[0]
		except:
			item['relayed_by'] = ''
		try:
			item['difficulty'] = doc.xpath('//table[@class="table table-striped"]/tr[9]/td[2]/text()')[0]
		except:
			item['difficulty'] = ''
		try:
			item['bits'] = doc.xpath('//table[@class="table table-striped"]/tr[10]/td[2]/text()')[0]
		except:
			item['bits'] = ''
		try:
			item['transations'] = doc.xpath('//table[@class="table table-striped"]/tr[11]/td[2]/text()')[0]
		except:
			item['transations'] = ''
		try:
			item['output'] = doc.xpath('//table[@class="table table-striped"]/tr[12]/td[2]/span/text()')[0]
		except:
			item['output'] = ''
		try:
			item['volume'] = doc.xpath('//table[@class="table table-striped"]/tr[13]/td[2]/span/text()')[0]
		except:
			item['volume'] = ''
		try:
			item['size'] = doc.xpath('//table[@class="table table-striped"]/tr[14]/td[2]/text()')[0]
		except:
			item['size'] = ''
		try:
			item['version'] = doc.xpath('//table[@class="table table-striped"]/tr[15]/td[2]/text()')[0]
		except:
			item['version'] = ''
		try:
			item['merkle_root'] = doc.xpath('//table[@class="table table-striped"]/tr[16]/td[2]/text()')[0]
		except:
			item['merkle_root'] = ''
		try:
			item['nonce'] = doc.xpath('//table[@class="table table-striped"]/tr[17]/td[2]/text()')[0]
		except:
			item['nonce'] = ''
		try:
			item['reward'] = doc.xpath('//table[@class="table table-striped"]/tr[18]/td[2]/span/text()')[0]
		except:
			item['reward'] = ''
		try:
			item['fees'] = doc.xpath('//table[@class="table table-striped"]/tr[19]/td[2]/span/text()')[0]
		except:
			item['fees'] = ''
		yield item 

