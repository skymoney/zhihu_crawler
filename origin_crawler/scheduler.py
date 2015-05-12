#-*- coding:utf-8 -*-

import re
from url import Url

class Scheduler:
	urls = []

	crawled_urls = []

	def add(self, url):
		#新加url，判断是否爬取过，如果爬取过不加入
		if self._filter(url):
			url_type = 'explore'
			if re.search(r'explore', url):
				url_type = 'explore'
			if re.search(r'topics', url):
				url_type = 'topics'
			if re.search(r'/question/\d+/*$', url):
				url_type = 'question'
			if re.search(r'/question/\d+/answer/\d+/?$', url):
				url_type = 'answer'
			if re.search(r'/people/\w+/?/$', url):
				url_type = 'people'

			u_obj = Url(url=url, url_type=url_type)

			self.urls.append(u_obj)

	def pop(self):
		if self.urls:
			return self.urls.pop(0)
		return None

	def count(self):
		return len(self.urls)

	def _filter(self, url):
		#过滤已爬取url
		#True 不在
		#false 已经爬过
		if url in self.crawled_urls:			
			return False
		self.crawled_urls.append(url)
		return True

scheudler = Scheduler()
