#-*- coding:utf-8 -*-

class Url:
	def __init__(self, url, url_type):
		self.url = url
		self.url_type = url_type

	def set_url_type(self, url_type):
		self.url_type = url_type