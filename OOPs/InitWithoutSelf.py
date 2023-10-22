class GFG:
	def __init__(somename, name, company):
		somename.name = name
		somename.company = company

	def show(somename):
		print("Hello my name is " + somename.name +
			" and I work in "+somename.company+".")


obj = GFG("John", "GeeksForGeeks")
obj.show()
