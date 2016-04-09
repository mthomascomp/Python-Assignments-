# Mervin Thomas
# Mr. Kyle Batterink
# ICS3U - b
# March 7, 2016


                                                                                # THE USERNAME IS "kings" AND THE PASSWORD IS "computerscience". 

username = "kings" # This line assigns the variable username and defines the username as kings.
# The above line of code contains a string which is attached to the variable

username_input = input('Please enter your username: ') # This allows the program to pick up the users input for the username the user has typed in, as this information will be used in the follwoing steps. 
# The above line of code contains an input command which allows the user to enter in a value or in this case the username for the program.

password = "computerscience" # This line assigns the password to the program, and it does it by assiging the variable 'password' to computer science.
# The above line contains a string which is assigned to the password which is computer science.

password_input = input('Please enter your password: ') # This is the variable that allows the user to type in the inout which is the password the user will type in as it will be needed in the following steps. 
# The above line contains an input command which allows the username to enter the password in this case.

if username_input == username and password_input == password:
# The above line contains an if command, conditional command, and an 'and' command
    # The if command is a conditonal control command, that allows the program to work if the inputed username matches with the udername registered in the program.
    # The and command above is a boolean operation that allows to make the program perform the if statement if both functions are correct. (i.e. if the username and the password the user input match with the programs username and password then only it will print welcome which follows the command.
    # The and command also allows the program to make the decison once both the commands are followed not just one command, and this is done by inserting an 'and' command in between the command you are telling the program to do.
    print('Welcome') # This command allows the program to print the sentence if the if command has been followed by the user. 
    
elif username_input == username and password_input != password: # This is an elif command that allows the program to check alternate conditons if the condition(s) above are or is false. This is very hand because it makes programming very efficent and easier to use.
    # The above line of code tells us that if the inputed username is = the username on the computer, but the passwords don't match, it will print out that the passwors are invalid. 
    print('Password is invalid') #This line of code prints out that the password is invalid based on the above line of code. 

elif username_input != username and password_input == password:
    # The above line of code tells us that if the inputed username does not eual to the username stored in the program, but the passwords match, then it will print out ans say that the password is invalid.
    print('Username is invalid') # This line of code prints the statement that the password is invalid. This will only occur if the above line of code functions, because it falls under the elif command.

elif username_input != username and password_input != password:
    # The above line of code basically tells us that if the inputed username and the inputed passwords don't equal each other then it will perform the function undernath it. 
    print('Username and Password invalid') # Theis line of code basically tells the program to print out the username and password is invalid. This will only happen if the above line of code is correct, else it will do the other jobs.
    
# This program took about 3-4 tries to figure it out and to meet the requirement and the rubric.


                                                                                 # THE USERNAME IS "kings" AND THE PASSWORD IS "computerscience".








    

