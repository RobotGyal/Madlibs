#GLOBAL VARIABLES
#a list containing the user inputs for call in the f-string of the story
madlibs = []

class colors:
    purple = '\033[30m'
    green = '\033[32m'
    yellow = '\033[93m'
    pink = '\033[95m'
    grey = '\033[37m'


#the core story which will have gaps for insertion
#a story originally written by Aesop - The Flies and the Honey
story = """%s Flies were attracted to a jar of %s which had been overturned in a housekeeper's %s,
 and placing their feet in it, ate %s. Their feet, however, became so smeared with the honey that they could not use their %s,
 nor release themselves, and were %s. Just as they were expiring, they %s, \"O %s creatures that we are,
 for the sake of a %s pleasure we have destroyed %s.\" \nMoral: Pleasure bought with pains, hurts""" 

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
    print(colors.yellow)
    new_noun = user_input("\nPlease input a noun: \n")
    #if(new_noun == 'Q' or 'q'):
        #running = False
    #else:
    add(new_noun)

# collects and adds verbs
def verbs():
    print(colors.yellow)
    new_verb = user_input("\nPlease input a verb: \n")
    #if(new_verb == 'Q' or 'q'):
        #running = False
    #else:
    add(new_verb)

# collects and adds adjectives
def adjectives():
    print(colors.yellow)
    new_adjective = user_input("\nPlease input a adjective: \n")
    #if(new_adjective == 'Q' or 'q'):
        #running = False
    #else:
    add(new_adjective)

# collects and adds number
def nums():
    print(colors.yellow)
    new_num = user_input("\nPlease input a number: \n")
    #if(new_num == 'Q' or 'q'):
        #running = False
    #else:
    add(int(new_num))

#run
def run():
    print(colors.yellow,"Welcome to Mad Libs!\nLet's begin\nPlease follow the following prompts\n")
    nums()
    nouns()
    nouns()
    adjectives()
    print(colors.grey,"\nLets make the next noun plural!")
    nouns()
    print(colors.grey,"\nLets make the next 2 verbs past tense!")
    verbs()
    verbs()
    adjectives()
    adjectives()
    print(colors.grey,"\nLets make the next noun plural!")
    nouns()

running = True
while running:
    enter = user_input("Press enter to continue: \n\n")
    running = run()

print("\n\n", colors.green, "Wonderful!\nHere is your story!\nThank you for playing\n")
print("\n\n", colors.pink, story % tuple(madlibs))

