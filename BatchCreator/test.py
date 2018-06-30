class javad():
	a = 0
	def j(self):
		self.a += 1
	def p(self):
		print self.a




javad = javad()


i = 1
while i < 10:
	javad.j()
	javad.p()
	i += 1