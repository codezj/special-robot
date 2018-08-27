class Foo:
	def f1(self):
		print('Foo.f1')
	def f2(self):
		print('Foo.f2')
		self.f1()

class Bar(Foo):
	def f1(self):
		print('Bar.f1')



obj=Bar()
print(obj.__dict__)
obj.f2()

###first is to find the method in its own class, if not, try to find the method in his father class