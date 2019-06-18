# Author:   Zavier P. Myles


# Purpose: Testing my Know knowlegde and skills with Python.
#          Creating a small little game from what I know





def start(nice=0,mean=0,name=""):
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


    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>>").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
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
        pick = input("\nA stranger approaches you for a \ncoversation. Will you be nice \nor mean? (N/M) \n>>>").lower()
        if pick == "n":
            print = ("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print ("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score{}

#==================================================
# SHOWS THE SCORE
#==================================================

def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))

  

def score(nice,mean,name):
          # score function is beging passed the vaules of stored within the 3 variables
    if nice > 2:
          win(nice,mean,name)
    if mean > 2:
          lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)

#=======================================
# WINS & LOSES
#=======================================
def win(nice,mean,name):
      print("\nNice Job {}, \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
      again(nice,mean,name)



def lose(nice,mean,name):
        print("\nAhhhh too bad, game over! \n{}, you live in a dirty beat up \nvan by the river".format(name))
        again(nice,mean,name)


#============================================
# WANNA PLAY AGAIN?
#============================================

def again(nice,mean,name):
    stop = True
    while stop:
          choice = input ("\nDo you want to play again? (y/n): \n>>>").lower()
          if choice == "y":
              stop = False
              reset(nice,mean,name)
          if choice == "n":
              print("\nOh, so sad, sorry to see you go!")
              stop = False
              quit()
          else:
              print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>>")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    #NOTE, this does not reset the name variable as that same user has elected to play again
    start(nice,mean,name)








if __name__ == "__main__":
    start()
