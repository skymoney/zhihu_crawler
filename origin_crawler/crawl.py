#-*- coding:utf-8 -*-

#author cheng

import sys, re
from bs4 import BeautifulSoup
import requests

import conf

from models import Question, Answer

def get_cookie():
	#login zhihu
	username = conf.username
	passwd = conf.passwd

	login_url = 'http://www.zhihu.com/login'

	#page_res = requests.get(inti_url)
	login_res = requests.post(login_url, data={'email': username, 'password': passwd})

	if login_res.status_code == 200:
		#login ok
		#fetch cookie for more data
		#page_dom = BeautifulSoup(login_res.content)
		return login_res.cookies

	else:
		print 'status code not right ', str(login_res.status_code)
		sys.exit(1)

def crawl_explore(url, cookie, scheduler):
	#crawl explore page
	explore_res = requests.get(url, cookies=cookie)

	if explore_res.status_code == 200:
		explore_dom = BeautifulSoup(explore_res.content)

		all_current_items = explore_dom.find_all("div", class_="explore-feed feed-item")
		
		for item in all_current_items:
			href = item.find('a', class_="question_link").get('href').split('answer')[0]

			new_url = href if href.startswith('http') \
					else 'http://www.zhihu.com/' + href
			scheduler.add(new_url)



def crawl_question(url, cookie, scheduler):
	#crawl question page
	#like host: http://www.zhihu.com/question/123456
	print 'start to question'
	question_res = requests.get(url, cookies=cookie)

	if question_res.status_code == 200:
		question_dom = BeautifulSoup(question_res.content)

		#find more question
		all_related_ques = question_dom.find("div", 
			id="zh-question-related-questions").find_all("a", class_="question_link")
		print 'related question size: ', str(len(all_related_ques))
		for ques in all_related_ques:
			new_url = ques.get('href') if ques.get('href').startswith('http') \
				else 'http://www.zhihu.com/' + ques.get('href')
			scheduler.add(new_url)

		#crawl data
		print 'start to crawl question data'
		q_id = re.search(r'\d+', url).group()
		q_title = question_dom.find("div", 
			id="zh-question-title").find('h2').contents[0].encode('utf-8')
		q_detail = ''
		if question_dom.find('div', 
			id='zh-question-detail').find('textarea'):
			q_detail = question_dom.find('div', 
			id='zh-question-detail').find('textarea').get_text().encode('utf-8')
		else:
			q_detail = question_dom.find('div', 
				id='zh-question-detail').get_text().encode('utf-8')
		q_author = 'default'
		question = Question(q_id=q_id, title=q_title, author=q_author, content=q_detail)

		print "Current Question=================="
		print str(question)

		#crawl answer data
		#a_id author votes content last_modify
		answer_list = question_dom.find_all("div", class_="zm-item-answer")
		print "Current Question Answer Size: ", str(len(answer_list))
		for answer in answer_list:
			a_id = answer.get('data-aid')
			author_h3 = answer.find("h3", class_="zm-item-answer-author-wrap")
			if author_h3.find_all('a'):
				author = author_h3.find_all('a')[1].text.encode('utf-8')
			else:
				#匿名用户
				author = author_h3.text.encode('utf-8')

			votes_div = answer.find("div", class_="zm-votebar goog-scrollfloater")

			try:
				votes_span = votes_div.find_all("span")
			except:
				print votes_span
				sys.exit(1)

			votes = votes_span[1].text if len(votes_span)>1 else 0

			content = answer.find("div", 
				class_="zm-editable-content clearfix").text.encode('utf-8')

			answer_info = Answer(a_id=a_id, author=author, votes=votes, content=content)

			question.answers.append(answer_info)

			print str(answer_info)

def crawl_topics(url, cookies, scheduler):
	#crawl topics page
	pass

def crawl_user(url, cookie, scheduler):
	#crawl user info
	pass