'''
CREATE A QUIZ LAB (25pts)

######################
##### BACKGROUND #####
######################

Now is your chance to write your own quiz. Use these quizzes to filter job applicants, weed out potential mates, or just plain have a chance to sit on the other side of the desk and make, rather than take, the quiz.

This lab applies the material used in Chapter 3 on using if statements. It also requires a bit of Chapter 1 because the program must calculate a percentage.


########################
##### INSTRUCTIONS #####
########################

This is the list of features your quiz needs to have:

Create your own quiz with five or more questions. 

You can ask questions that require:
    a number as an answer (e.g., What is 1+1?)
    text (e.g. What is Harry Potter's last name?)
    a selection (Which of these choices are correct? A, B, or C? True or False?

Your quiz will use at least two DIFFERENT question types from above.  

If you have the user enter non-numeric answers, think and cover the different ways a user could enter a correct answer. For example, if the answer is “a”, would “A” also be acceptable? See Section 3.6 for a reminder on how to do this.

Let the user know if he or she gets the question correct. Print a message depending on the user's answer.

You need to keep track of how many questions they get correct.
At the end of the program print the percentage of questions the user gets right.



Keep the following in mind when creating the program:

Variable names should start with a lower case letter. Upper case letters work, but it is not considered proper.

To create a running total of the number correct, create a variable to store this score. Set it to zero. With an if statement, add one to the variable each time the user gets a correct answer. (How do you know if they got it correct? Remember that if you are printing out “correct” then you have already done that part. Just add a line there to add one to the number correct.) If you don't remember how to add one to a variable, go back and review Section 1.5.

Treat true/false questions like multiple choice questions, just compare to “True” or “False.” Don't try to do if a: we'll implement if statements like that later on in the class, but this isn't the place.

Calculate the percentage by using a formula at the end of the game. Don't just add 20% for each question the user gets correct. If you add 20% each time, then you have to change the program 5 places if you add a 6th question. With a formula, you only need 1 change.

To print a blank line so that all the questions don't run into each other, use the following code: print()

Remember the program can print multiple items on one line. This can be useful when printing the user's score at the end.  print("The value of x is", x)

Separate out your code by using blank lines to group sections together. For example, put a blank line between the code for each question.

Sometimes it makes sense to re-use variables. Rather than having a different variable to hold the user's answer for each question, you could reuse the same one.

Use descriptive variable names. x is a terrible variable name. Instead use something like number_correct.

Don't make super-long lines. Chances are you don't need to use \n at all. Just use multiple print statements.

Your final quiz should look similar to the example run below.  It does not have to be exactly like this, but please notice the consistent spacing, style, and feedback provided.  


#######################
##### EXAMPLE RUN #####
#######################

Here's an example from my program. Please create your own original questions. I like to be entertained while I check these programs.

Quiz time!

How many books are there in the Harry Potter series? 7
Correct!

What is 3*(2-1)? 3
Correct!

What is 3*2-1? 5
Correct!

Who sings Black Horse and the Cherry Tree?
1. Kelly Clarkson
2. K.T. Tunstall
3. Hillary Duff
4. Bon Jovi
? 2
Correct!

Who is on the front of a one dollar bill
1. George Washington
2. Abraham Lincoln
3. John Adams
4. Thomas Jefferson
? 2
No.

Congratulations, you got 4 answers right.
That is a score of 80.0 percent.
'''

#####################################
# COMPLETE YOUR LAB BELOW THIS LINE #
#####################################



# WHEN YOU COMPLETE THIS LAB, DO NOT FORGET TO COMMIT AND PUSH
# YOUR FILE BACK TO THE REPOSITORY.
