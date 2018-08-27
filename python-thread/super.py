class OldboyPeople:
	school='Oldboy'

	def __init__(self,name,age,sex):
		self.name=name
		self.age=age
		self.sex=sex

	def tell_info(self):
		print('<name:%s  age: %s  sex:%s>'  %(self.name,self.age,self.sex))

class OldboyStudent(OldboyPeople):
	def __init__(self,name,age,sex,course):
		super(OldboyStudent,self).__init__(name,age,sex)
		self.course=course


	def tell_info(self):
		print('I am a student: ',end='')
		super(OldboyStudent,self).tell_info()
		# OldboyPeople.tell_info(self)


stu1=OldboyStudent('egon',18,'male','python')
stu1.tell_info()