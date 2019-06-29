from datetime import date
def check_birthdate(y,m,d):
    if date.today()>=date(y,m,d):
	    return "True"
    else:
	    return "False"

def calculate_age(y,m,d):
    return date.today().year - y - ((date.today().month, date.today().day)<(m,d))

y = int(input("Please Enter Year: "))
m = int(input("Please Enter Day: "))
d = int(input("Please Enter Month: "))
if check_birthdate(y,m,d)=="True":
    print("You are %s years old"%calculate_age(y,m,d))
else:
    print("Invalid Birthdate")
