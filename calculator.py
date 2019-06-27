x = input("Please enter a number: ")
y = input("Please enter a number: ")
z = input("Please enter an operation: ")
if x.isdigit()==True and y.isdigit()==True:
    if z == "+":
	    print(x+y)
    elif z=="-":
	    print(int(x)-int(y))
    elif z=="*":
	    print(int(x)*int(y))
    elif z=="/":
	    print(int(x)/int(y))
    else:
	    print("invalid operation, please enter\n+ for addition\n- for substraction\n* for multiplication\n/ for division")
else:
    print("Please choose #")

	
