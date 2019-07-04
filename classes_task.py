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

print("\tWelcome to HR Pro 2019")
while True:
	print("\tChoose an action to do: ")
	print("\t\t1. show employees ")
	print("\t\t2. show managers ")
	print("\t\t3. add an employee ")
	print("\t\t4. add a manager ")
	print("\t\t5. exit ")
	print()

	choice = input("what would you like to do? ")
	print("-----------------")

	if choice == "3":
		name = input("name: ")
		age = input("age: ")
		salary = input("salary: ")
		year = input("employment year: ")
		
		print("Employee added succesfully")
		
		employee = Employee(name, age, salary, year)
		E.append(employee)


	if choice == "1":
		if len(E) == 0:
			print("No Employee was added")

			print("-----------------")
		else:	
			for employee in E:
				print(employee.__str__())
			print("-----------------")

	if choice =="4":
		name = input("name: ")
		age = input("age: ")
		salary = input("salary: ")
		year = input("employment year: ")
		bonus_percentage = input("Bonus Percentage: ")
	
		print("Employee added succesfully")

		manager = Manager(name, age, salary, year, bonus_percentage)
		M.append(manager)

	if choice == "2":
		if len(M) == 0:
			print("No Employee was added")

			print("-----------------")
		else:
			for manager in M:
				print(manager.__str__())
			print("-----------------")

	if choice == "5":
		break
		