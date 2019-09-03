#GLOBAL VARIABLES
#a list containing the user inputs for call in the f-string of the story
madlibs = []

#the core story which will have gaps for insertion
#a story originally written by Aesop
story = """A %s was driving a wagon along a country lane, when the %s sank down deep into a rut.
 The %s driver, stupefied and aghast, stood looking at the wagon, and did nothing but utter loud cries to Hercules to come and help him.
 Hercules, it is said, appeared and thus addressed him:
 \'Put your shoulders to the wheels, my man. Goad on your bullocks, and never more pray to me for help,
until you have done your best to help yourself, or depend upon it you will henceforth pray in vain.\'""" 

#FUNCTIONS
#reads user input
def user_input(prompt):
    user_input = input(prompt)
    return user_input

# add user_input to madlibs list
def add(item):
    madlibs.append(item)

# collects and adds user nouns
def nouns():
    new_noun = user_input("Please input a noun: ")
    add(new_noun)

# collects and adds verbs
def verbs():
    new_verb = user_input("Please input a verb: ")
    add(new_verb)

# collects and adds adjectives
def adjectives():
    new_adjective = user_input("Please input a adjective: ")
    add(new_adjective)

# collects and adds number
def nums():
    new_num = user_input("Please input a number: ")
    add(int(new_num))




#TEST FUNCTION
print("Welcome to Mad Libs!\nLet's begin\nPlease follow the following prompts")
nouns()
nouns()
nouns()




#running = True
#while running:
#    enter = user_input("Press enter to continue: ")
#    running = #insert more code

print(story % tuple(madlibs))

