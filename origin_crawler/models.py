#-*- coding:utf-8 -*-

class Question:
	answers = []
	def __init__(self, q_id, title, author, content):
		self.q_id = q_id
		self.title = title
		self.author = author
		self.content = content
		self.answers = []

	def set_title(self, title):
		self.title = title

	def add_answer(self, answer):
		#add an answer(Answer)
		self.answers.add(answer)

	def __str__(self):
		return "Question Id: " + self.q_id + \
			" \n By author: " + self.author + \
			" \n Title: " + self.title + \
			" \n Content: " + self.content + \
			" \n Total answers: " + str(len(self.answers))

class Answer:
	def __init__(self, a_id, author, votes, content, last_modify=None):
		self.a_id = a_id
		self.author = author
		self.votes = votes
		self.content = content
		self.last_modify = last_modify

	def __str__(self):
		return "Answer ID: " + str(self.a_id) + \
			" \n By Author: " + str(self.author) + \
			" \n Total Votes " + str(self.votes)