def askFood():
     x = input(name + ", do you fancy some food?")
     if (x=="yes"):
         food = eat(foodtype)
     if (x=="no"):
         cont= input("continue?")