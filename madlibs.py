#GLOBAL VARIABLES
#a list containing the user inputs for call in the f-string of the story
madlibs = []

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

#run
def run():
    print("Welcome to Mad Libs!\nLet's begin\nPlease follow the following prompts")
    nums()
    nouns()
    nouns()
    adjectives()
    print("Lets make the next noun plural!")
    nouns()
    print("Lets make the next 2 verbs past tense!")
    verbs()
    verbs()
    adjectives()
    adjectives()
    print("Lets make the next noun plural!")
    nouns()

#running = True
#while running:
#    enter = user_input("Press enter to continue: ")
#    running = #insert more code

print(story % tuple(madlibs))

