
item = " "
B = {}
while item != 'done':
	item = input("Please enter an item: ")
	if item == 'done':
		break
	price = input("Please enter price: ")
	quantity = input("Please enter quantity: ")
	B[item] = [price, quantity]

print("--------------------")
print("receipt")
print("--------------------")

for item in B:
	print(B[item][0], item, float(B[item][1]))	
print("------------------------")

total = 0
for item in B:
	total = total+(float(B[item][0])*float(B[item][1]))
	
print(total)
