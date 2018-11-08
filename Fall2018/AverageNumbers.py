try:
	file = open('numbers.txt', 'r')

	sum = 0
	count = 0
	for line in file:
		count+=1
		amount = int(line)
		sum = sum+amount
	average = sum/count
	print(average)
	
except ValueError:
	print("File must have only numbers. Try again.")
except IOError:
	print("Trouble opening file. Try again.")