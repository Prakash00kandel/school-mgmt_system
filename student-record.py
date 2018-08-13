from books import book 
studentLIst = []
class Student:
	def __init__(self,name,address):
		self.name = name
		self.address = address
	def getName(self):
		return self.name
	def getAddress(self):
		return self.address
count = int(input("Enter the number of student : "))
for i in range(count):
	name = input("Enter student name : ")
	address = input("Enter the address of student :  ")
	student = Student(name,address)
	studentLIst.append(student)

studentmap = map(lambda stud: stud.getName()+"" + stud.getAddress(),studentLIst)
print(list(studentmap))

book = Book(1,"yuvaraj paudel", "python programming", "2014")
book.showAuthorName()
