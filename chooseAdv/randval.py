import random

#storytext.py
#intro_enter
intro_1 = ('exit','leave','get out of')[random.randint(0,2)]
intro_2 = ('plains','fields','forests','wildlands')[random.randint(0,3)]
intro_3 = ('scratches','bruises','cuts')[random.randint(0,2)]
intro_4 = ('north','east','west','south')[random.randint(0,3)]
intro_5 = ('little','small','delightful')[random.randint(0,2)]
intro_6 = ('village','town','place')[random.randint(0,2)]
intro_7 = ('Spotting','Noticing','Seeing')[random.randint(0,2)]
intro_8 = ('walk','make your way','travel','hobble')[random.randint(0,3)]
#intro_inn
intro_9 = ('grab','take','hop onto')[random.randint(0,2)]
intro_10 = ('seat','stool','chair','barstool')[random.randint(0,3)]
intro_11 = ('polishing a glass','handing a dish off to his staff','counting his money','writing memos','eating some food')[random.randint(0,4)]
intro_12 = ('takes notice','notices','spots','looks at')[random.randint(0,2)]
#intro_inn_adventurer, also uses intro_3
intro_13 = ('He looks down at your','He notices your','He looks at your')[random.randint(0,2)]
intro_14 = ('Are you one of those adventurers?','Are ya an adventurer?','You seem like an adventurer, are you?')[random.randint(0,2)]

intro_14_true = ('An adventurer? Well, well.','Oh? Thought so.','Looks like my eyes haven\'t failed me just yet.')[random.randint(0,2)]
intro_14_false = ('Huh you\'re not?','Oh?','That\'s not good.')[random.randint(0,2)]

intro_askDrink = ('What would you like to drink?','What drink would you like?')
intro_askDrink_mad = ('What drink?','Drink, name it.','Name the drink.','Name your drink.')
#
player_answerAdventure = ('Well, ','You see, ','Actually, ','Truth be told, ')[random.randint(0,3)]
player_quote_yummy = ('Yummy in my tummy','Delicious','Mmm mmm mmm!','Hey, that\'s pretty good','Scrumpdiliumptious')[random.randint(0,4)]
#
innkeeper_name = ('Joseph','John','Jan')[random.randint(0,2)]
innkeeper_greeting = ('Welcome','Hey there','Hello','Welcome to my inn','Greetings')[random.randint(0,4)]
innkeeper_askfood_1 = ('fancy','want','wanna ')
innkeeper_askfood_2 = ('')