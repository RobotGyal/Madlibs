#GLOBAL VARIABLES
#a list containing the user inputs for call in the f-string of the story
madlibs = ['one', 'two', 'three']

#the core story which will have gaps for insertion
#a story originally written by Aesop
story = """A %s was driving a wagon along a country lane, when the %s sank down deep into a rut.
 The %s driver, stupefied and aghast, stood looking at the wagon, and did nothing but utter loud cries to Hercules to come and help him.
 Hercules, it is said, appeared and thus addressed him:
 \'Put your shoulders to the wheels, my man. Goad on your bullocks, and never more pray to me for help,
until you have done your best to help yourself, or depend upon it you will henceforth pray in vain.\'""" 

#FOR LOOPING THOUGH LIST
print(story % tuple(madlibs))

#FUNCTIONS
#reads user input
def user_input(prompt):
    user_input = input(prompt)
    return user_input

# add user_input to madlibs list
def add(item):
    madlibs.append(item)

# collects and adds user nouns
def nouns(item):
    new_noun = user_input("Please input a noun: ")
    add(new_noun)

# collects and adds verbs
def verbs(item):
    new_verb = user_input("Please input a verb: ")
    add(new_verb)

# collects and adds adjectives
def adjectives(new_adjective):
    new_adjective = user_input("Please input a adjective: ")
    add(new_adjective)

# collects and adds number
def num(new_num):
    new_num = user_input("Please input a number: ")
    add(int(new_num))


#TEST FUNCTION