food_good = ('a','b','c','d') #List of good foods provided by the innkeeper.
food_bad = ('poison','death','House Special', 'leftovers') #List of bad (fatal) foods provided by the innkeeper. Changes cause of death.

#print('The menu shows a list containing '+str(food_good)[1:-1])
#print('The other half shows a list of {0}'.format(food_bad))

#lista = "The menu shows a list containing: "
#print(lista+', '.join(food_good))


fglen = len(food_good)
a = "List: "
b = "Not a tuple"

a = ('boy','girl')

def listoff(tupleName,prefix):
    x = len(tupleName)
    for i in range(x):
        if (i < x):
            if (i != x-1):
                prefix = prefix+tupleName[i]+", "
            else:
                prefix = prefix+"and "+tupleName[i]
        else:
            prefix = prefix+tupleName[i]+"."
    return prefix

print(listoff(a,"We have: "))