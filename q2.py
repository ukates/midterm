# This is a very simple game of sticks. There are 21 sticks, first the user picks number of sticks between 1-4, then the computer picks sticks(1-4). Who ever will pick the last stick will lose.
# Look for the TODO blocks as an indication of when you have to add your own code.

import random
sticks = 21

def playGame():
    # you do not need to modify code in this function
    print('There are 21 sticks. You can pick from 1 to 4 sticks at a time, and the computer will then pick from 1 to 4 sticks at a time. Whoever picks the last stick loses!')
    while True:
        print('Current sticks: ' + str(sticks))
        userChoice = askUserChoice()
        if subtractSticks( userChoice ):
            print('You lost!')
            break
        
        computerChoice = determineComputerChoice()
        print('Computer picked: ' + str(computerChoice) )
        if subtractSticks( computerChoice ):
            print('Computer lost!')
            break
        

def askUserChoice():
    while True:
        print('How many sticks do you want to pick up? ( 1 - 4 )')
        userChoice = int(input()) #converts userchoice into integer
        if userChoice in range(1,5): #if the users choice or input is 1-4 the users choice will return.  
            return userChoice
        else: #if userchoice is not within the correct range, it will be invalid and loop back to the start until the correct choice is given. 
            print('Your answer is invalid, please choose an integer between 1-4 and try again!')
    
    

def subtractSticks( number ):
    global sticks
    sticks -= number # this subtracts the number paramater (user choice and computer choice ) from the global value sticks, and updates the global value. 
    
    if sticks <= 0: # if sticks is less than or equal to 0 the function will return true causing either the user or computer to lose. 
        return True
    else:
        return False #if greater than 0 function will return false continuing the game until it has ended. 
    
    
def determineComputerChoice():
    r = random.randint(1,4) 
    return r #returns random integer between 1 and 4 as computers choice. 
   
