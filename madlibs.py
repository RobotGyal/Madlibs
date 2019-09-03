#GLOBAL VARIABLES



#FUNCTIONS
#reads user input
def user_input(prompt):
    user_input = input(prompt)
    return user_input

# add user_input to madlibs list
def add(item):
    madlibs.append(item)


#STORY
#the core story which will have gaps for insertion
story = ""


#MADLIBS
#a list containing the user inputs for call in the f-string of the story
madlibs = []


#TEST FUNCTION