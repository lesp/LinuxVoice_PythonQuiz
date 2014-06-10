#!/usr/local/bin/python

#We start by importing a few libraries.
#Easygui provides our GUI for the game.
from easygui import *
#Time is a library that introduces the concept of time to the game.
import time
#Pygame is a series of multimedia tools that can create games using Python.
import pygame

#To start pygame we need to initialise it.
pygame.init()
#To use the audio facilities of Pygame we need to tell Pygame that we wish to use them.
pygame.mixer.init()

#Now we create three functions, these functions contain the code to play each audio track.
#The audio for each of these functions should be in the same folder as this code.
def intro():
    intro=pygame.mixer.music.load('intro.mp3')
    pygame.mixer.music.play(1)

def win():
    win=pygame.mixer.music.load('correct.mp3')
    pygame.mixer.music.play(1)

def lose():
    lose=pygame.mixer.music.load('wrong.mp3')
    pygame.mixer.music.play(1)

#To keep our score, we create a variable called score and set it to zero.
score = 0
#The next variable contains the location of the Linux Voice logo.
logo = "./images/masthead.gif"
#This is a list, sometimes called an array. In here I store two items.
play = ["Yes","No"]

#I start the game by calling the intro() function, and this plays the Linux Voice theme.
intro()
#Here we create a variable called game_start and it will store the answer to the question "Would you like to play the quiz?"
#To capture the answer I use the buttonbox function from easygui. This function has many options, for this I use.
#title = The text at the top of the dialog box.
#image = logo, the variable I earlier created.
#msg = This is the question that I ask the player.
#choices = play. I use this to reference the earlier created list and use the values contained as the choices for the player.
start_title = "Welcome to Linux Voice Python Quiz"
start_msg = "Would you like to play the Quiz?"
game_start = buttonbox(title=start_title,image=logo,msg=start_msg,choices=play)

#For debugging purposes I have the answer given by the player printed to the Python shell.
print(game_start)
#Here we see some conditional logic that tests to see if the answer was "Yes" If the answer is not equal to No, it proceeds.
if game_start != "No":
    #Here is another easygui dialog box, a message box. It has the same syntax as the previous box we created.
    #You can see str(score) in the line below. In order to join a string of text, our message, with the value
    #of the score we need to wrap the score, which is an integer, in a helper function that converts integers
    #and floats into strings
    msgbox(title="Let us begin",msg="Your score is "+str(score))

    #Question 1
    while True:
        msg = "What type of number is 1.4?"
        title = "Question 1"
        q1choices = ["Integer","Float","Very small"]
        q1 = choicebox(msg,title,q1choices)
        if q1 == "Float":
            win()
            score = score + 1
            msgbox(title="CORRECT",image="./images/tick.gif",msg="Well done you got it right. Your score is "+str(score))
            break
        else:
            lose()
            msgbox(title="Wrong Answer",image="./images/cross.gif",msg="I'm sorry that's the wrong answer")
            break

    #Question 2
    while True:
        msg = "In conditional logic what does != mean?"
        title = "Question 2"
        q2choices = ["Equal to","Not Equal To"]
        q2 = choicebox(msg,title,q2choices)
        if q2 == "Not Equal To":
            win()
            score = score + 1
            msgbox(title="CORRECT",image="./images/tick.gif",msg="Well done you got it right. Your score is "+str(score))
            break
        else:
            lose()
            msgbox(title="Wrong Answer",image="./images/cross.gif",msg="I'm sorry that's the wrong answer")
            break
            

    #Question 3
    while True:
        msg = "Which of these creates a variable called x with a value of 10 as an integer?"
        title = "Question 3"
        q3choices = ["x == 10","x = 10","x = str(10)"]
        q3 = choicebox(msg,title,q3choices)
        if q3 == "x = 10":
            win()
            score = score + 1
            msgbox(title="CORRECT",image="./images/tick.gif",msg="Well done you got it right. Your score is "+str(score))
            break
        else:
            lose()
            msgbox(title="Wrong Answer",image="./images/cross.gif",msg="I'm sorry that's the wrong answer")
            break

    #Question 4
    while True:
        msg = "Who created Python?"
        title = "Question 4"
        q3choices = ["Guido Van Rossum","Moff Tarkin","Linus Torvalds"]
        q3 = choicebox(msg,title,q3choices)
        if q3 == "Guido Van Rossum":
            win()
            score = score + 1
            msgbox(title="CORRECT",image="./images/tick.gif",msg="Well done you got it right. Your score is "+str(score))
            break
        else:
            lose()
            msgbox(title="Wrong Answer",image="./images/cross.gif",msg="I'm sorry that's the wrong answer")
            break
gameover = "./images/well_done.gif"
intro()
if score < 1:
    game_over = msgbox(title="Linux Voice Python Quiz",image=gameover,msg="Oh dear you scored "+str(score))
else:
    game_over = msgbox(title="Linux Voice Python Quiz",image=gameover,msg="Well done you scored "+str(score))
