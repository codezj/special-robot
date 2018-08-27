class OldboyPeople:
	school='Oldboy'

	def __init__(self,name,age,sex):
		self.name=name
		self.age=age
		self.sex=sex

	def tell_info(self):
		print('<name: %s age: %s sex: %s>'  %(self.name,self.age,self.sex))


class OldboyStudent(OldboyPeople):
	def __init__(self,name,age,sex,course,stu_id):
		OldboyPeople.__init__(self,name,age,sex)
		self.course=course
		self.stu_id=stu_id

def learn(self):
	print('%s is learning' %self.name)


def tell_info(self):
	print('I am a student: ', end=' ')
	OldboyPeople.tell_info(self)


stu1=OldboyStudent('Jack',18,'male','python',1)
stu1.tell_info()