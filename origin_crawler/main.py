#-*- coding:utf-8 -*-

import pickle

from bs4 import BeautifulSoup

from scheduler import Scheduler
from crawl import crawl_explore, crawl_question
from crawl import get_cookie

scheduler = Scheduler()


def start():
	
	seedUrl = "http://www.zhihu.com/explore"
	#cookie = get_cookie()
	cookie = cookie_read()

	#cookie_persistance(cookie)
	#as first init
	scheduler.add(seedUrl)

	print 'start to crawl....'

	while scheduler.count() > 0:
		next_crawl = scheduler.pop()

		if next_crawl.url_type == 'explore':
			crawl_explore(next_crawl.url, cookie, scheduler)

		if next_crawl.url_type == 'question':
			crawl_question(next_crawl.url, cookie, scheduler)
			#break

def dom_ana():
	explore_data = []
	with open('index.html', 'rb') as index_file:
		
		for line in index_file.readlines():
			explore_data += line
	explore_data = ''.join(explore_data)

	explore_dom = BeautifulSoup(explore_data)

	print explore_dom.title
	#get explore item
	items = explore_dom.find_all("div", class_="explore-feed feed-item")
	print 'This page total: ', str(len(items))

	for item in items:
		href = item.find('a', class_="question_link").get('href')
		question_link = href.split('answer')[0]

		scheduler.add()

def question_deal():
	question_data = []
	with open('question27830729.html') as question_file:
		question_data = question_file.readlines()
		'''
		for line in question_file.readlines():
			question_data += line
		'''
	question_data = ''.join(question_data)

	question_dom = BeautifulSoup(question_data)

	print question_dom.title

	#get question info
	question_title_div = question_dom.find("div", id="zh-question-title")

	#print question_title_div.find('h2').contents[0].encode('utf-8')

	question_detail_div = question_dom.find('div', id='zh-question-detail')

	#print question_detail_div.find('textarea').get_text().encode('utf-8')

	all_answers = question_dom.find_all("div", class_="zm-item-answer")

	for answer in all_answers:
		#crawl current page all answer
		author_h3 = answer.find("h3", class_="zm-item-answer-author-wrap")
		if author_h3.find_all('a') and len(author_h3.find_all('a'))>1:
			author = author_h3.find_all('a')[1].text.encode('utf-8')
		else:
			#匿名用户
			author = author_h3.text.encode('utf-8')
		#print author
		print '============'
		
		content = answer.find("div", 
				class_="zm-editable-content").get_text().encode('utf-8')
		print content
		

def cookie_persistance(cookie):
	#cookie持久化，避免频繁请求cookie
	with open('cookie.pickle', 'wb') as cookie_file:
		pickle.dump(cookie, cookie_file)


def cookie_read():
	#读取cookie
	with open('cookie.pickle', 'rb') as cookie_file:
		cookie = pickle.load(cookie_file)

	return cookie


if __name__ == '__main__':
	#dom_ana()
	#question_deal()
	start()