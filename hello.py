#how to make comments

#print and input functions and some simple string methods

# print (*objects, sep = ' ', end = '\n, file = sys.stdout, flush = false')
firstName = input ("whats your first name? ")

#removing white space from the strings 
firstName = firstName.strip()

# capitalize first letter of a string
firstName = firstName.capitalize()

#chaining methods
secondName = input ("whats your surname name? ").capitalize().strip()


# capitalize every word in a sting var.title()
# split strings str.split('seperator') eg, first, last = name.split(' ')

#differnt ways to output the result. 

#v1 args seperated by comma
print ("hello,",firstName,secondName)
#v2 string concat
print ("hello, " + firstName + ' ' + secondName)
#v3 mega weirdness
print ('hello, ' + firstName, end=" ")
print (secondName)
#4 format strings 
print (f'hello, {firstName} {secondName}')

def hello():
    print('hello')

