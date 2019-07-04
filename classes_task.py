from datetime import date

class Employee:
	def __init__(self, name, age, salary, year):
		self.name = name
		self.age = age
		self.salary = salary
		self.year = year
		self.employment_date = year
	def get_working_years(self):
		return (date.today().year) - int(self.employment_date)
	def __str__(self):
		return "name: {}, age: {}, salary: {}, working years: {}".format(self.name, self.age, self.salary, self.get_working_years())

class Manager(Employee):
	def __init__(self, name, age, salary, year, bonus_percentage):
		super().__init__(name, age, salary, year)
		self.bonus_percentage = bonus_percentage
	def get_bonus(self):
		return float(self.salary) * float(self.bonus_percentage)
	def __str__(self):
		return "name: {}, age: {}, salary: {}, working years: {}, bonus: {}".format(self.name, self.age, self.salary, self.get_working_years(), self.get_bonus())

E = []
M = []

while True:
	print("Choose an action to do: ")
	print("1. show employees ")
	print("2. show managers ")
	print("3. add an employee ")
	print("4. add a manager ")
	print("5. exit ")

	choice = input("what would you like to do? ")
	print("-----------------")

	if choice == "3":
		name = input("name: ")
		E.append(name)
		age = input("age: ")
		E.append(age)
		salary = input("salary: ")
		E.append(salary)
		year = input("employment year: ")
		E.append(year)
		print("Employee added succesfully")

	if choice == "1": 
		E_1 = Employee(E[0], E[1], E[2], E[3])
		print(E_1.__str__())
		print("-----------------")

	if choice =="4":
		name = input("name: ")
		M.append(name)
		age = input("age: ")
		M.append(age)
		salary = input("salary: ")
		M.append(salary)
		year = input("employment year: ")
		M.append(year)
		bonus_percentage = input("Bonus Percentage: ")
		M.append(bonus_percentage)
		print("Employee added succesfully")

	if choice == "2":
		M_1=Manager(M[0], M[1], M[2], M[3], M[4])
		print(M_1.__str__())
		print("-----------------")

	if choice == "5":
		break
		