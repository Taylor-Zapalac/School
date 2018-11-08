month = int(input("Enter month (numeric):"))
day = int(input("Enter day:"))
year = int(input("Enter two digit year:"))

magic = month*day

if(magic == year):
	print("This date is magic!")
else:
	print("This date is not magic.")
