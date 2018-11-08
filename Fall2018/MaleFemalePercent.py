numMales = int(input("Enter number of males:"))
numFemales = int(input("Enter number of females:"))

whole = numMales + numFemales

perMales = numMales/whole
perFemales = numFemales/whole

print('Percent males: '+format(perMales, '.0%'))
print('Percent females: '+format(perFemales, '.0%'))
