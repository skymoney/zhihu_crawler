#-*- coding:utf-8 -*-

class BasePipe:
	def __init__(self):
		pass

	def process(self, Obj):
		pass

class QuestionPipe(BasePipe):
	def __init__(self):
		pass

	def process(self, Obj):
		pass

def process_question(question):
	with open('question/' + question.q_id + '.dat', 'wb') as question_file:
		to_write_info = "Question Title: " + question.title \
			+ " Author: " + question.author \
			+ " Content: " + question.content
		question_file.write(to_write_info)
		question_file.write("===========")

		for ans in question.answers:
			single_ans_info = "author: " + str(ans.author) + "\n" \
				+ "votes: " + str(ans.votes) + "\n" \
				+ "last modify: "  + str(ans.last_modify) + "\n" \
				+ "content: " + str(ans.content) + "\n"

			question_file.write(single_ans_info)
			question_file.write("--------------------------------\n")