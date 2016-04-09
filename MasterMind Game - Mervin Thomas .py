# Mervin Thomas
# Mr. Kyle Batterink
# ICS3U-b 
# April 8, 2016

import random # This line of code imports the random command from the computer

gameon=True # This variable is assigned to game on, and contains the command true, to verify it. 
while gameon: # This line of code contains the while loop of game on
        print ("The MasterMind Game") # This line of code prints out the line the mastermind game at te top of the program.0
        print ("Please, guess the code.You can use red(R), green(G), blue(B), and yellow(Y)") # The line of code gives the directions, on how to use the code and the colors 
        colors = ["R", "G", "B", "Y"] # THis variable is assigned to colors where each color has a string value 
        attempts = 0 # This variable is attemtps where it will count the number of attempts each time and will be added to one each time the game is played later on in the game.
        game = True # This line of variable verifies if the game is true, adn then will continue 
        
#  The below code; computer randomly picks four-color code
        color_code = random.sample(colors,4)	
        print (color_code)

# player guesses the colour
        while game: # This line of code contains a while loop which will loop everything underneath it
                correct_color = "" # This line of code contains variabe correct_color with a string value 
                guessed_color = "" # The line of code contains the variable guessed_color with a string value 
                player_guess = input().upper() # This line of code contains the variable player_guess, where we can input and converts it to upper case. 
                attempts += 1 # This added the attempts each time the game is played. 
	
	
 # checking if player's input is correct
                if len(player_guess) != len(color_code): # This line of code calculates the length of the code and matches it. 
                # The above line of code contains an if command and checks if the player guess length is equal to the length of the colour code. 
                        print ("\nThe secret code should have four colors only. Try again!") # This prints out the text in the string
                        continue # This continue variable allows the program to contine to the next set of commands 
                for i in range(4): #This line of code contains the variable i and calculated the range from 0-4
                        if player_guess[i] not in colors: # Indexes the variable i from the player_guess
                                print ("\nUse only one of the following four colors: red(R), green(G), blue(B), and yellow(Y)") # Prints out the text if the colors are not followed correctly 
                                continue # This allows the program to continue 
			
# comparison between player's input and secret code
                if correct_color != "XXXX": # THis variable contains the correct_color which is assigned to a four word string which is XXXX
                        for i in range(4): # This variable will calculate the range of the 4 colors which was assigned above
                                if player_guess[i] == color_code[i]:
#This line of code contains the variable playerguess and the color code of i 
                                        correct_color +="X"		
                                if  player_guess[i] != color_code[i] and player_guess[i] in color_code:
                                        guessed_color += "O"
                        print (len(correct_color), "Correct", " and" , len(guessed_color),"of the Correct Colors in Wrong Spots") # This line of the code the length of the color and the length of the guessed color to display what is in the wrong spots and what is in the right spots	
                if correct_color == "XXXX":# This line of code contains the if var
                        print ("Congratulations ! thats the correct code. You needed " + str(attempts) + " attempts to guess.")
# This line of code contains the print variable if the the 'if' command above is followed
                        game = False
# If all the functions above are false 
                        gameon=False # If all the functions above are false 
                if correct_color != "XXXX":
# The 'if' statement contains the correct_color variable and will follow if the variable is not equal to the string "XXXX"
                        print ("Please Guess the code Again: ")
# This line contains the print command which contains the text in the string.
                        if attempts >= 1 and attempts < 10 and correct_color != "XXXX":
# This contains the if command attempts which will range from 1 - 10
                        # The above line of code contains an 'and' command 
                                print ("Next attempt: ")
# This will print out if the correct_colour is not equal to the random colours which the computer assigns 
                        elif attempts >= 10:
# This is an elif command which will be follows if the if command was not followed.
                                print ("You didn't guess! The secret color code was: " + str(color_code))
# This line of code contains the print command which prints the text and the string of the color code if the guessed color was wrong
                        continue
# This line of code contains the continue command which will continue the program
                    
# Commands which will ask the user to play or not play
                while gameon == False: # If the gameon variable is false then it will follow the code
                # The above lines and the following lines of code fall under the while loop. 
                        finish_game = input("\nDo you want to play again (Y/N)?").upper() # This Line of code contains the variable finish game and allows the user to input if they want to play it again or not. 
                        attempts = 0 # Resets the atempts to 0 
                        if finish_game == "Y": # This line of code will only follow if the answer is yes
                                gameon = True # This line of code will allow the program to return to the start
                                continue #This allows the program to continue the command in the program
                        elif finish_game =="N": # This is a elif command which will happen if no is answered 
                                print ("Thanks for the game! Bye!") # This print command will follow if the elif command above is followed.
                                break # This line of code allows the program to brak and finish the command. 


# This game took abour 9 - 10 tries to make it perfect and correct according to the rubrics.                                 
              
