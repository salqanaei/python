skills = ["Research", "Presentation", "Writing", "Analytics"]
cv = {}
Name = input("Please Enter Your Name: ")
Age = input("Please Enter your Age: ")
Exp = input("Please Enter your years of experience: ")
cv['name'] = Name
cv['age'] = Age
cv['experience'] = Exp
cv["skills"] = []

print("1. " + skills[0])
print("2. " + skills[1])
print("3. " + skills[2])
print("4. " + skills[3])

s1 = input("Please choose a skill: ")
s2 = input("Please choose another skill: ")

if s1 == "1":
	cv['skills'].append(skills[0])
elif s1 == "2":
	cv['skills'].append(skills[1])
elif s1 == "3":
	cv['skills'].append(skills[2])
elif s1 == "4":
	cv['skills'].append(skills[3])

if s2 == "1" and s1!=s2:
	cv['skills'].append(skills[0])
elif s2 == "2" and s1!=s2:
	cv['skills'].append(skills[1])
elif s2 == "3" and s1!=s2:
	cv['skills'].append(skills[2])
elif s2 == "4" and s1!=s2:
	cv['skills'].append(skills[3])


if int(cv['age'])<=35 and int(cv['experience'])>=3 and len(cv['skills'])==2 and 'Presentation' in cv['skills']:
	print("Congratulation %s. You got the job"%Name)
else:
	print("You are unqualified for the position please try again later")
