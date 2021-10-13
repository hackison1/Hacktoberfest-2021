Skip to content
 
Search…
All gists
Back to GitHub
@KabishDahal 
@wynand1004
wynand1004/snake_game.py
Created 3 years ago • Report abuse
54
20
Tip
 Code
 Revisions 1
 Stars 54
 Forks 20
<script src="https://gist.github.com/wynand1004/ec105fd2f457b10d971c09586ec44900.js"></script>
A Simple Snake Game made in Python 3
snake_game.py
# Simple Snake Game in Python 3 for Beginners
# By @TokyoEdTech

import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @TokyoEdTech")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
        
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()
@xxabdoslimexx
Tip
xxabdoslimexx commented on Aug 10, 2019
Is there any way to make this 2 player?

@wynand1004
Tip
Owner
Author
wynand1004 commented on Aug 11, 2019
@xxabdoslimexx Sure. The easiest way is to basically double everything. For example:

head2, go_up2, etc.

This will make the code longer of course. The alternative is to use lists and loops, or even better to rewrite this in object-oriented fashion.

@abscorpy
Tip
abscorpy commented on Oct 1, 2019
Hi, about the snake game

Where can i find 'turtle.py' or why are you importting that file, thanks for the support

@wynand1004
Tip
Owner
Author
wynand1004 commented on Oct 1, 2019
@abscorpy The turtle module comes with python so there is no file to find. Enjoy!

@ChrisZhang1002
Tip
ChrisZhang1002 commented on Oct 2, 2019
@wynand1004
thanks for your code , it was fine on running.
i suggest to add "penup()" into move() function as below to avoid drawing a line when the snake head moving

if head.direction == "up":
y = head.ycor()
head.penup()
head.sety(y + 20)
head.penup()

and also merge them into "down" , "left" and "right"
i think it should be better

thanks so much

@wynand1004
Tip
Owner
Author
wynand1004 commented on Oct 7, 2019
Adding penup to the move method is not a good choice - you only need to call penup once, when you create the snake head or the segments. See lines 26, 35, and 130.

@Tylergcantrell
Tip
Tylergcantrell commented on Oct 22, 2019
Could you make this run smoother? I changed a few values around and it made it smoother, but it wouldn't work with the rest of the code. Thank you in advance.

@HarunResit-cyber
Tip
HarunResit-cyber commented on Oct 27, 2019
Hello , how can i change the speed of snake . I tried to change head.speed(0) but it didn't work

@CrimsonCat
Tip
CrimsonCat commented on Nov 15, 2019
sorry to bother, but while trying to learn to code on python i found this every time i try to copy the script it gives me an "unexpected indent"error.Help would be appreciated!

@XandorRoyal
Tip
XandorRoyal commented on Nov 25, 2019
@HarunResit-cyber
Hello, I am not the owner/Author, but can answer this question for him. head.speed(0) quite literally does nothing. If you care to know why, keep reading. Otherwise, the answer you're looking for is change the "delay" value on both line 8 and 112. And you can also make it change more by changing the change val on line 134. (Wow a lot of change, no?)
Why:
The reason you can't change the turtle's speed from the turtle.speed function is quite simple. We aren't using the pen to draw. i.e. you can see when the turtle is spawned the author did penup(). We are using the pen to alternatively act as a marker. This makes you wonder how the marker moves. The author does this in a function (move): Line 67.

@XandorRoyal
Tip
XandorRoyal commented on Nov 25, 2019
@CrimsonCat
Hello, Same as last message, I am. Anyways, when I pasted it into PyCharms for me it was good. If you care to know why you got that message read on, otherwise just go back up to the top of the script and click raw and do command+a and command+c and paste it into whatever you use to run python.
Why:
The Indent Error is a pretty common error even for experts. Unlike a language like Lua, where whitespace(the empty space in between functions, strings, etc) really doesn't matter much. Python puts up a fit. Part of python's syntax is the whitespace, and so it makes sure that everything is in the right order. Lets say you make a function. You have to indent everything you want in that function. And unless it is in an if statement in that function they all have to be on the same line of indent. Otherwise you get said error.

@Talha-ai
Tip
Talha-ai commented on Dec 25, 2019
Hello, I am getting this error :
AttributeError: 'Turtle' object has no attribute 'penup'
Please help.

@afafafafafadf
Tip
afafafafafadf commented on Feb 18, 2020
Is it possible to keep the snake constantly moving and adding a segment when it colldies with the food??

@Pytheprogram
Tip
Pytheprogram commented on Feb 20, 2020
Traceback (most recent call last):
File "./prog.py", line 1, in
File "/usr/lib/python3.7/turtle.py", line 107, in
import Tkinter as TK
ModuleNotFoundError: No module named 'Tkinter'

I get this error

@afafafafafadf
Tip
afafafafafadf commented on Feb 20, 2020
Traceback (most recent call last):
File "./prog.py", line 1, in
File "/usr/lib/python3.7/turtle.py", line 107, in
import Tkinter as TK
ModuleNotFoundError: No module named 'Tkinter'

I get this error
i have a suggestion try writing import Tkinter at the start

@Idk-What-My-Name-Is
Tip
Idk-What-My-Name-Is commented on Mar 29, 2020
what is move() exactly?

@HarunResit-cyber
Tip
HarunResit-cyber commented on Apr 1, 2020
Hello can you help me ? I want to change the delay when the score > 50 i tried but i doesnt worked on me Please help!Thanks

@Ronnelandleo
Tip
Ronnelandleo commented on Apr 15, 2020
why is it 290?

@XandorRoyal
Tip
XandorRoyal commented on Apr 26, 2020
@Talha-ai
Hello, make sure you are doing turtle.penup() the parenthesis are needed.

@XandorRoyal
Tip
XandorRoyal commented on Apr 26, 2020
@Idk-What-My-Name-Is
Kind of self explanatory my friend.

@XandorRoyal
Tip
XandorRoyal commented on Apr 26, 2020
@HarunResit-cyber
https://pastebin.com/ZN67UY22 This should work.

@Vallerinho
Tip
Vallerinho commented on May 2, 2020
How do apply lines on the screen so it looks like a board with alot of black squares?

@AnnieDaughterOfHades
Tip
AnnieDaughterOfHades commented on May 6, 2020
uh is there an easier way to make this 2 player

@wynand1004
Tip
Owner
Author
wynand1004 commented on May 12, 2020
Yes, but you'd have to use classes and objects. I wrote this tutorial with beginners in mind and wanted to avoid complicated structures like classes and objects.

@maintzer
Tip
maintzer commented on May 12, 2020
having tested this code (being too lazy to make my own!) i noticed that the collision logic with the food isn't ideal, the food often vanished when not touching the snake. the problem stems from the fact that the food spawns in on a random point within turtle's built-in coordinate system, rather than the 30-by-30 grid the snake moves through (given the screen width is 600 and the snake width is 20).
on lines 121 and 122, try using random.randint(-14, 14) for the random coordinates x and y, then moving the food to (x20, y20). this ought to ensure it moves to a point in the snake's grid. then, on line 119, the distance can be set as low as 1 and the collision logic should be perfect.

@BenRed06
Tip
BenRed06 commented on May 19, 2020
what are the dependencies?

@wynand1004
Tip
Owner
Author
wynand1004 commented on May 19, 2020
@maintzer Good point. You can also align everything using random.randrange(-280, 280, 20).

@wynand1004
Tip
Owner
Author
wynand1004 commented on May 19, 2020
@benslayer12 You need Python 3.x which normally comes with the necessary modules (turtle, time, and random). The turtle module relies on tkinter which may need to be installed separately, at least on Linux.

@ZacABOT
Tip
ZacABOT commented on Jun 1, 2020 • 
Hello,
when i run the code it does not let me move the snake. Were would my error most likely be

@V0618-tech
Tip
V0618-tech commented on Jun 2, 2020
Thanks for the code

@ghoshdipan
Tip
ghoshdipan commented on Jun 3, 2020 • 
Traceback (most recent call last):
File "F:/Linux/Programs/Python/snake_game.py", line 170, in
if segment.distance(head)<20:
File "C:\Users\DIPAN GHOSH\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 1858, in distance
return abs(pos - self._position)
File "C:\Users\DIPAN GHOSH\AppData\Local\Programs\Python\Python38\lib\turtle.py", line 262, in sub
return Vec2D(self[0]-other[0], self[1]-other[1])
TypeError: unsupported operand type(s) for -: 'int' and 'method'
.
.
.
.
.
.
Can you explain this error?

@edilgin
Tip
edilgin commented on Jun 3, 2020
im trying to code this in oop style but struggling. Imo a video would be really helpful for seeing how useful oop is compared to this code

@helpmeplz15
Tip
helpmeplz15 commented on Jun 6, 2020
i have the same problem as zacbot

@aliya-rahmani
Tip
aliya-rahmani commented on Jun 6, 2020
import turtle
import time
import random

delay = 0.1

screen set up
wn = turtle.Screen()
wn.title("Snake game by @AliyA Rahmani")
wn.bgcolor("green")
wn.setup(width=650, height=650)
wn.tracer(0)

head of snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

Snake's food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

functions for movement
def go_up():
head.direction = "up"
def go_down():
head.direction = "down"
def go_right():
head.direction = "right"
def go_left():
head.direction = "left"

function
def move():
if head.direction == "up":
y = head.ycor()
head.sety(y + 20)
if head.direction == "down":
y = head.ycor()
head.sety(y - 20)
if head.direction == "right":
x = head.xcor()
head.setx(x + 20)
if head.direction == "left":
x = head.xcor()
head.setx(x - 20)

connect to keyboard
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_left, "a")

main game loop
while True:
wn.update()
#check for the collision of the food
if head.distance(food) < 20:
# move the food through random
x = random.randint(-300,300)
y = random.randint(-300,300)
food.goto(x, y)
#adding new segments
new_segment = turtle.Turtle()
new_segment.speed(0)
new_segment.shape("square")
new_segment.color("grey")
new_segment.penup()
segments.append(new_segment)

# Move the end segments first in reverse order
for index in range(len(segments) - 1, 0, -1):
    x = segments[index-1].xcor()
    y = segments[index-1].ycor()
    segments[index].goto(x, y)

# Move segment 0 to where the head is
if len(segments) > 0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x, y)
move()

time.sleep(delay)
wn.mainloop()
Plzz tell me the problem in the code

@sameerchemmi
Tip
sameerchemmi commented on Jun 7, 2020
sir, I am your youtube subsciber, can you make this game playable on touchscreen

by alternating onkeypress(),is that possible

@LumicMirror
Tip
LumicMirror commented on Jun 20, 2020
`import turtle
import time
import random

delay = 0.1

Score
score = 0
high_score = 0

Set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @TokyoEdTech")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) # Turns off the screen updates

Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

Functions
def go_up():
if head.direction != "down":
head.direction = "up"

def go_down():
if head.direction != "up":
head.direction = "down"

def go_left():
if head.direction != "right":
head.direction = "left"

def go_right():
if head.direction != "left":
head.direction = "right"

def move():
if head.direction == "up":
y = head.ycor()
head.sety(y + 20)

if head.direction == "down":
    y = head.ycor()
    head.sety(y - 20)

if head.direction == "left":
    x = head.xcor()
    head.setx(x - 20)

if head.direction == "right":
    x = head.xcor()
    head.setx(x + 20)
Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

Main game loop
while True:
wn.update()

# Check for a collision with the border
if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    food.goto(0, 100)

    # Hide the segments
    for segment in segments:
        segment.goto(1000, 1000)

    # Clear the segments list
    segments.clear()

    # Reset the score
    score = 0

    # Reset the delay
    delay = 0.1

    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Check for a collision with the food
if head.distance(food) < 20:
    # Move the food to a random spot
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    food.goto(x, y)




    # Add a segment
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("grey")
    new_segment.penup()
    segments.append(new_segment)

    # Shorten the delay
    delay -= 0.001

    # Increase the score
    score += 10

    if score > high_score:
        high_score = score

    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
for index in range(len(segments) - 1, 0, -1):
    x = segments[index - 1].xcor()
    y = segments[index - 1].ycor()
    segments[index].goto(x, y)

# Move segment 0 to where the head is
if len(segments) > 0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x, y)

move()

# Check for head collision with the body segments
for segment in segments:
    if segment.distance(head) < 20:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        food.goto(0, 100)

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        # Update the score display
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                  font=("Courier", 24, "normal"))

time.sleep(delay)
wn.mainloop()
`
