# Author:   Zavier P. Myles


# Purpose: Testing my Know knowlegde and skills with Python.
#          Creating a small little game from what I know







def start(nice=0,mean=0,name=''):
    # get user name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """checking if this is a new game or not.
        if it is, it will get the user's name.
        if it is not a new game, thank the player for
        playing again and continue with the game
    """
    #if we do not have this user's name,
    #then they are a new player and need to get their name.


    if name != '':
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>>").capitalize()
                if name != "":
                    print("\nWelcome, {}!",format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can chiise to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions")
                    stop = False
     return name

#===========================================================================
#                BREAK
#===========================================================================


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \ncoversation. Will you be nice \nor mean? (N/M) \n>>>")
        if pick == "n":
            print = ("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print ("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score{}

  














if __name__ == "__main__":
    start()
