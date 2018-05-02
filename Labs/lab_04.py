'''
CHAPTER 4 LAB - PURSUIT GAME

######################
##### BACKGROUND #####
######################

The idea for this game originally came from the Heath Users Group and was published in More BASIC Computer Games in 1979.  See the course website for more details.

The idea is to move across the desert while being chased. You need to manage your thirst, how tired your horse is, and how far ahead of the enemy you are.

You don't have to use a horse and desert.  Make yours a car chase, a bank heist, space themed, or whatever you like.  I ask that you still have the same elements described as a part of your final game.  

########################
##### INSTRUCTIONS #####
########################
Complete the following step by step instructions.  
If you get stuck on a step, ask for help.  Wandering forward without understanding will end poorly.

1) Create a new program and print the instructions to the screen. Do this with multiple print statements. Don't use one print statement and multiple \n characters to jam everything on one line.

Welcome to Camel!
You have stolen a camel to make your way across the great Mobi desert.
The natives want their camel back and are chasing you down! Survive your
desert trek and out run the natives.
Create a boolean variable called done and set to False.
Create a while loop that will keep looping while done is False.
Inside the loop, print out the following:
A. Drink from your canteen.
B. Ahead moderate speed.
C. Ahead full speed.
D. Stop for the night.
E. Status check.
Q. Quit.
Ask the user for their choice. Make sure to add a space before the quote so the user input doesn't run into your text.
If the user's choice is Q, then set done to True. By doing something like user_choice.upper() instead of just user_choice in your if statement you can make it case insensitive.
Test and make sure that you can quit out of the game.
Before your main program loop, create variables for miles traveled, thirst, camel tiredness. Set these to zero.
Create a variable for the distance the natives have traveled and set it to -20. (Twenty miles back.)
Create and set an initial number of drinks in the canteen.
Add an elif in your main program loop and see if the user is asking for status. If so, print out something like this:
Miles traveled:  0
Drinks in canteen:  3
The natives are 10 miles behind you.
Add an elif in your main program loop and handle if the user wants to stop for the night. If the user does, reset the camel's tiredness to zero. Print that the camel is happy, and move the natives up a random amount from 7 to 14 or so.
Add an elif in your main program loop and handle if the user wants to go ahead full speed. If the user does, go forward a random amount between 10 and 20 inclusive. Print how many miles the user traveled. Add 1 to thirst. Add a random 1 to 3 to camel tiredness. Move the natives up 7 to 14 miles.
Add an elif in your main program loop and handle if the user wants to go ahead moderate speed. If the user does, go forward a random amount between 5 and 12 inclusive. Print how many miles the user traveled. Add 1 to thirst. Add 1 to camel tiredness. Move the natives up 7 to 14 miles.
Add an elif in your main program loop and handle if the user wants to go ahead drink from the canteen. If the user does, make sure there are drinks in the canteen. If there are, subtract one drink and set the player's thirst to zero. Otherwise print an error.
In the loop, print “You are thirsty.” if the user's thirst is above 4.
Print “You died of thirst!” if the user's thirst is above 6. Set done to true. Make sure you create your code so that the program doesn't print both “Your are thirsty” and “You died of thirst!” Use elif as appropriate.
Print “Your camel is getting tired.” if the camel's tiredness is above 5.
Print “Your camel is dead.” if the camel's tiredness is above 8. Like the prior steps, print one or the other. It is a good idea to include a check with the done variable so t hat you don't print that your camel is getting tired after you died of thirst.
If the natives have caught up, print that they caught the player and end the game.
Else if the natives are less than 15 miles behind, print “The natives are getting close!”
If the user has traveled 200 miles across the desert, print that they won and end the game. Make sure they aren't dead before declaring them a winner.
Add a one-in-twenty chance of finding an oasis. Print that the user found it, refill the canteen, reset player thirst, and rest the camel.
Play the game and tune the numbers so it is challenging but not impossible. Fix any bugs you find.

'''
