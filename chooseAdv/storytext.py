import randval
import time

#I made this! :)
#Reads off each value in a tuple with n seconds between each line
def read(readTupleName,waitTime):
    for i in range(len(readTupleName)):
            print(readTupleName[i])
            time.sleep(waitTime)

#Valid Statements
food_good = ('soup','cheese')
food_bad = ('poison','death','House Special', 'leftovers', 'supreme cocktail')
yes = ('y','yes','sure','yup','positive','correct','of course','course','duh')
#yesiam = ('yes i am','yes i am.','you bet i am','i definitely am','what else could i be','yup i am','i am')
no = ('no','nah','nope','negative','incorrect','no way','wrong','n')


intro_enter = (
    ('You '+randval.intro_1+' the '+randval.intro_2+", "+randval.intro_3+" on your body."),
    ('Heading '+randval.intro_4+'ward, you come across a '+randval.intro_5+' '+randval.intro_6+'.'),
    (randval.intro_7+' an inn, you '+randval.intro_8+' towards it.')
)

intro_inn = (
    ('You '+randval.intro_9+' a '+randval.intro_10+' at the counter, close to the innkeeper.'),
    ('He\'s '+randval.intro_11+'.'),
    ('He '+randval.intro_12+' at you, stopping and approaches you')
)

intro_inn_askadventurer = (
    (randval.intro_13+' '+randval.intro_3+'.'),
    (randval.innkeeper_name+': '+randval.intro_14)
)

#nestedaskFood choicelist
choicelist_food = (
    'Huh? It\'s not on my menu, check again',
    'Uh, wrong again. Look more closely',
    'If you\'ve got glasses, you should put them on now.',
    'It\'s not that hard, you order what\'s on the menu and you get it.',
    'I don\'t know if you\'ve been hit in the wrong spot, but you oughta choose something on the list.',
    '...',
    'Alright, enough feining ignorance. You either order something to eat, or you don\'t get anything',
    'Alright.')