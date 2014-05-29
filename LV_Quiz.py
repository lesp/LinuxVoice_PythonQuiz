from easygui import *
import time

score = 0
logo = "./images/masthead.gif"
play = ["Yes","No"]
game_start = buttonbox(title="Welcome to Linux Voice Python Quiz",image=logo,msg="Play the Quiz?",choices=play)

print(game_start)

if game_start != "No":
    msgbox(title="Let us begin",msg="Your score is "+str(score))

    #Question 1
    while True:
        msg = "What type of number is 1.4?"
        title = "Question 1"
        q1choices = ["Integer","Float"]
        q1 = choicebox(msg,title,q1choices)
        if q1 == "Float":
            score = score + 1
            msgbox(title="CORRECT",image="./images/tick.gif",msg="Well done you got it right. Your score is "+str(score))
            break
        else:
            msgbox(title="Wrong Answer",image="./images/cross.gif",msg="Oh dear, try again")

    #Question 2
    while True:
        msg = "In conditional logic what does != mean?"
        title = "Question 2"
        q2choices = ["Equal to","Not Equal To"]
        q2 = choicebox(msg,title,q2choices)
        if q2 == "Not Equal To":
            score = score + 1
            msgbox(title="CORRECT",image="./images/tick.gif",msg="Well done you got it right. Your score is "+str(score))
            break
        else:
            msgbox(title="Wrong Answer",image="./images/cross.gif",msg="Oh dear, try again")

    #Question 3
    while True:
        msg = "Which of these creates a variable called x with a value of 10 as an integer?"
        title = "Question 3"
        q3choices = ["x == 10","x = 10","x = str(10)"]
        q3 = choicebox(msg,title,q3choices)
        if q3 == "x = 10":
            score = score + 1
            msgbox(title="CORRECT",image="./images/tick.gif",msg="Well done you got it right. Your score is "+str(score))
            break
        else:
            msgbox(title="Wrong Answer",image="./images/cross.gif",msg="Oh dear, try again")
gameover = "./images/well_done.gif"
game_over = msgbox(title="Linux Voice Python Quiz",image=gameover,msg="Well done you scored "+str(score))
