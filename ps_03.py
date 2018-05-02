'''
Chapter 3 Problem Set (16pts)

Instructions:  For each of the following, enter your answer below the numbered problem.

For questions asking you to fix code, just change the code to make it work as intended.

Make sure your file executes before you submit it!  

If a single problem is not working properly, please comment it out of your code. If a question is commented out, it will receive partial credit.
Non working or broken code will not receive any credit for that problem.

'''

#################################
#  Problem 1 (1pt)
#  Fix the following code. Look closely, it is a common syntax error.

temperature = float(input("Temperature: ")
if temperature > 90:
     print("It is hot outside.")

#################################
#  Problem 2 (3pts)
#  Write code that will take in a number from the user and print to tell the user if their number is positive, negative, or zero.  Your output should print exactly like the example runs below.

'''
Example runs:
Enter a number: 5.3
Your number is positive

Enter a number: 0
Your number is zero
'''



#################################
#  Problem 3 (3pts)
#  Write a python program which takes a number from the user, and prints \"Success\" if it is both greater than -10 AND less than or equal to 10.  If the number is outside this range, print Failure.")

'''
Example Run:
Enter a number greater than -10 and less than or equal to 10: -5.2
Success
'''

##################################
#  Problem 4 (2pts)
#  Fix the following code.  There are three things wrong.

x = input("Enter a number:")
if x = 3
     print("You entered 3")

###################################
#  Problem 5 (2pts)
#  There are three things wrong with this code. Fix the code.

answer = input("What is the name of Dr. Bunsen Honeydew's assistant?")
if a == "Beaker"
     print("Correct!")
else:
      print("Incorrect! It is Beaker.")

#####################################
#  Problem 6 (2pts)
#Look at the code below.  Before running the code, make a prediction of what each line will print. Put your prediction in a comment to the right of the print statement.  I am not grading you for your prediction, I simply want you to think about the code. Next, run the code and see if you are correct. One of the lines creates an error.  Fix it. Make sure you understand the reason for any incorrect guesses.  One produces an error.  Comment that one out.

print("3" == "3") #put guesses here
print(" 3" == "3") # and here
print(3 < "3") # etc
print(3 < 4)
print(3 < 10)
print("3" < "4")
print("3" < "10")
print((2 == 2) == "True" )
print((2 == 2) == True )


#####################################
#  Problem 7 (3pt)
#  Fix the following code which has multiple errors.

print("Welcome to Oregon Trail!")

print("A. Banker\nB. Carpenter\nC. Farmer")
money = 100
input = input("What is your occupation?")

if input = "A":
     occupation = "Banker"
     money += 100
else input = "B"
     occupation = "Carpenter"
     money += 50
else input = C:
     occupation = "Farmer"

print("You are a", occupation, "with", money, "dollars")