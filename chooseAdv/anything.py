import random
def functionNoom ():
    a = 0
for x in range (10):
    x=random.randint(1,100)
    print (x)
    if ((x%2) == 1):
        print ("this number is odd")
    if ((x%2) == 0):
        a += 1
        print  ('this number is even')
        
print( "is " + str(a) + " the sum of the evens")
def greetin ():
    name = input ('Hello, what is your name?')
    print ('Hello '+ str(name))
def age ():
    age= int(input('How old are you?'))
    return age 