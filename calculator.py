#learning integers (int) and float in python


#version 1 

#  x = 1
#  y = 2
#  z = 1 + 2 
#  print(z)

#version 2

x = input('what is the first number? ')
#convert the strings that are inputted to integers 
x = int(x)

#Or nest the input in the int function
y = float(input('what is the second number?'))

#round(number [, digits])
z = round(x + y, 2) 

#number formatting use format string + :,  
print (f'{z:,}')





