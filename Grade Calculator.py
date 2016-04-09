# Mervin Thomas
# Mr. Kyle Batterink
# ICS3U-b
# March 7, 2016


print("Enter your grade percentage:") #This print command allows the program to display the text which is in the string.

final_grade = float(input()) #This is the x variable which is registered as fht efloat of an input the user types in.

if final_grade >100: #This command contains an if statement and will only perform if the final grade is greated than 100. 
    print("This percentage is invalid and does not have a grade corresponddence") #This is the print command that follows the if command above it. This will only print if the if command is followed.
elif final_grade  >= 90 and final_grade  <= 100: # This line of code is an elif command. It performs the commands underneath it if the command in this line happens. 
    print("Your corrsponding letter grade is: A") # The line of code prints out the text only if the command above it is followed. 
elif final_grade >= 80 and final_grade  <= 89: # This line of code is an elif command. It performs the commands underneath it if the command in this line happens. 
   print("Your corresponding letter grade is: B")# The line of code prints out the text only if the command above it is followed. 
elif final_grade >= 70 and final_grade <= 79:# This line of code is an elif command. It performs the commands underneath it if the command in this line happens. 
   print("Your corresponding letter grade is: C")# The line of code prints out the text only if the command above it is followed. 
elif final_grade >= 50 and final_grade  <= 69: # This line of code is an elif command. It performs the commands underneath it if the command in this line happens. 
    print("Your corresponding letter grade is: D")# The line of code prints out the text only if the command above it is followed. 
elif final_grade < 50: # This line of code is an elif command. It performs the commands underneath it if the command in this line happens. 
    print ("Your corresponding letter grade is: F")# The line of code prints out the text only if the command above it is followed.

# The baove programs uses the 'elif', 'if', 'print', 'and', commands to run the program. 


#This program took some time to create because i intially forgot to define the variable x.
# It took me about 7-8 tries and redos to get his program to work and to make it function properly as per the guidelines and the rubric 


   
