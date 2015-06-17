#-*- coding:utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, create_engine

from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Question(Base):
	__tablename__ = 'question'
	answers = []

	id = Column(Integer, primary_key=True)
	q_id = Column(String(20))
	title = Column(String(100))
	author = Column(String(50))
	content = Column(Text)

	answers = relationship("Answer")

	def __repr__(self):
		return "Question Id: " + self.q_id + \
			" \n By author: " + self.author + \
			" \n Title: " + self.title + \
			" \n Content: " + self.content + \
			" \n Total answers: " + str(len(self.answers))

class Answer(Base):
	__tablename__ = 'answer'

	id = Column(Integer, primary_key=True)
	a_id = Column(String(20))
	author = Column(String(50))
	votes = Column(Integer)
	content = Column(Text)
	last_modify = Column(DateTime)

	question_id = Column(Integer, ForeignKey('question.id'))


	def __repr__(self):
		return "Answer ID: " + str(self.a_id) + \
			" \n By Author: " + str(self.author) + \
			" \n Total Votes " + str(self.votes)

engine = create_engine("mysql+mysqlconnector://root:123456@localhost:3306/zhihu_crawler")

#Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)