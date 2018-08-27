class OldboyPeople:
	school='Oldboy'

	def __init__(self,name,age,sex,date_obj):
		self.name=name
		self.age=age
		self.sex=sex
		self.birth=date_obj

	def tell_info(self):
		print('<name:%s age:%s gender:%s >' % (self.name, self.age, self.sex))

class OldboyStudent(OldboyPeople):

	def __init__(self,name,age,sex,stu_id,date_obj):

		OldboyPeople.__init__(self,name,age,sex,date_obj)

		self.courses=[]
		self.stu_id=stu_id

	def learn(self):
		print('%s is learning' % self.name)


	def tell_info(self):
		print('I am a student: ', end=' ')
		OldboyPeople.tell_info(self)


class OldboyTeacher(OldboyPeople):

	def __init__(self, name, age, sex, level, salary, date_obj):
		OldboyPeople.__init__(self,name,age,sex,date_obj)
		self.level=level
		self.salary=salary
		self.courses=[]

	def teach(self):
		print('%s is teaching' % self.name)

	def tell_info(self):
		print('I am a teacher: ', end=' ')
		OldboyPeople.tell_info(self)


class OldboySale(OldboyPeople):

	def __init__(self,name,age,sex,kpi,date_obj):
		OldboyPeople.__init__(self,name,age,sex,date_obj)
		self.kpi=kpi

	def tell_info(self):
		print('I am sales man: ', end='')
		OldboyPeople.tell_info(self)


class Date:

	def __init__(self,year,mon,day):
		self.year=year
		self.mon=mon
		self.day=day

	def tell_birth(self):
		print('birthday is: <%s-%s-%s>' % (self.year,self.mon,self.day))


class Course:

	def __init__(self,name,price,period):
		self.name=name
		self.price=price
		self.period=period

	def tell_info(self):
		print('detail info for courses: <%s,%s,%s>' %(self.name,self.price,self.period))




Python=Course('python automation book',3000,'3mon')
Linux=Course('bigDataAnalysis',3000,'3mon')
date_obj=Date(1993,3,13)


stu1=OldboyStudent('xxxx',28,'female',1,date_obj)

stu1.courses.append(Python)
stu1.courses.append(Linux)

print(stu1.courses[0].tell_info())







