import randval
import storytext

#Define variables to prevent crashes, and for future reference
plr_name = "Placeholder" #The player's name
food_good = storytext.food_good #List of good foods provided by the innkeeper.
food_bad = storytext.food_bad #List of bad (fatal) foods provided by the innkeeper. Changes cause of death.
choicelist = ('1','2','3','4','5','6','7','8','9','10') #Global option list to prevent crashes, probably.
innkeeper_angered = False

#Random Variables
#These are set in randval.py, but we use a shorthand or easily referrable
#version
plr_quote_yum = randval.player_quote_yummy #Variance of the phrase the player says when eating a good food
npc_inn_name = randval.innkeeper_name #Name of the innkeeper.

#inputs for common answers
yes = storytext.yes
no = storytext.no
#yesiam = storytext.yesiam

#Unspecific Functions
    #Simple print statement
def death(deathCause):
    print("You have died of "+deathCause)
    end()
    #Prints a loss, then exits the program
def end():
    print("OH NO! Your story is over. Go home. Now. We are closed")
    print ("You should start over again.")
    exit()

#Example: I want to list off the tuple, tup = ('a','b','c')
###listoff(tup,"These are my letters: ")
###output: These are my letters: a, b, and c.
def listoff(tupleName,prefix):
    x = len(tupleName)
    for i in range(x):
        if (i < x):
            if (i != x-1):
                prefix = prefix+tupleName[i]+", "
            else:
                prefix = prefix+"and "+tupleName[i]
        elif i == x:
            prefix = prefix+tupleName[i]+"."
    return prefix
    
#2) Asks a question, if the answer is in yes or no list, then output true or false
def askQ(question):
    x = input(question+"\n")
    if x.lower() in yes: #If they say a variant of yes, then return true
        x = True
    elif x.lower() in no: #if they say a variant of no, then return no
        x = False
    else: #if neither is said, then question the player.
        x = False
        print("Failed")
        x = askQ(question)
    return x

#1) Asks the player for their name.
def askName():
    x = input("You introduce yourself, saying your name was ") 
    return x
    
def checkName(name):
    x = True
    if name == "": #If the name is blank
        print("Hard to pronounce.")
        x = False
    return x

def eat(foodType):
    if foodType in food_good:
        print("Me: "+plr_quote_yum+"! This "+foodType+" is good!")
    elif foodType in food_bad:
        death("indigestion.")
        
def nestedaskFood(timer):
    choicelist = storytext.choicelist_food
    innangered = False
    
    playerchosenfood = input("You decide to order: ")

    if timer < len(choicelist):
        if playerchosenfood != "":
            if (playerchosenfood not in food_good and playerchosenfood not in food_bad):
                if (playerchosenfood.lower not in no):
                    print(npc_inn_name+": "+choicelist[timer])
                    timer += 1
                    nestedaskFood(timer)
                elif (playerchosenfood.lower in no):
                    print(npc_inn_name+": Alright, hold on a minute then.")
            elif (playerchosenfood in food_good or playerchosenfood in food_bad):
                eat(playerchosenfood)
        elif playerchosenfood == "":
            print("Saying nothing gets you nowhere.")
            nestedaskFood(timer)
            
    elif timer >= len(choicelist):
        print(npc_inn_name+": No more, that's it. I'll give you courtesy of a drink, but you can get your own food.")
        innangered = True
    return innangered

def askFood():
    
    x = input(plr_name + ", do you want some food?\n")
    if (x.lower() in yes):
        print("\n"+npc_inn_name+" pulls out a menu.")
        print(listoff(food_good,"The menu lists "))
        print(listoff(food_bad,"Strangely, on the other side it lists "))
        nestedaskFood(0)
    elif (x.lower() in no):
        print("Alright, hold on a minute.")
    else:
        print("I can't read that.")
        askFood()
        
def Drink():
    x= input("What would you like to quench your thirst? \"Water\", \"milk\", or \"supreme cocktail\"? ")
    if (x.lower() == "milk"):
        print("Let us hope you aren't lactose intolerant")
    elif (x.lower() == "water"):
        print("You feel refreshed and hydrated.")
    elif (x.lower() == "supreme cocktail"):
        death("poison.")
    else: 
        print ("I'm sorry I don't understand.")
        Drink()
def Convo():
    print("There seems to be an intimidating figure across the way!")
    x = input("Would you like to speak to him? attack him? or buy him a tasty suprise? ")
    if (x== "speak" or x== "speak to him"):
        death("of an intense hug.")
    elif(x=="attack"or x=="attack him"):
        death("being flicked in the head.")
        
    elif(x=="tasty suprise" or x=="buy him a tasty suprise"):
        print("You guys are now best friends and he gives you a hug that almost kills you.")
    
def dog():
    print("you see a dog outside")
    x=input("do you want to feed it or pet it or leave it alone? ")
    if (x== "feed it"):
        print("You two are now bffs. How cute.")
    elif(x=="pet it"):
        print('He likes it and you two are now inseperable')
    elif(x=="leave it alone"):
        print("I don't like that answer. Redo")
        dog()
    
    
storytext.read(storytext.intro_enter,2)
storytext.read(storytext.intro_inn,2)
print("Innkeeper: The name's "+npc_inn_name)
plr_name = askName()

print("\n"+npc_inn_name+": Well then, welcome, " + plr_name+".")
storytext.read(storytext.intro_inn_askadventurer,2)

if askQ('You answer: '+randval.player_answerAdventure):
    print("\n"+npc_inn_name+": "+randval.intro_14_true)
    askFood()
    Drink()
    Convo()
    dog()
    print("just be glad that it wasn't a pitbull ;)")
else:
    print(npc_inn_name+": "+randval.intro_14_false)
#ask food

#what type?