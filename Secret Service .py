# Mervin Thomas
# Mr. Kyle Batterink
# ICS3u - b
# March 28, 2016


# Project Name - Secret Service Program

# Instructions - Create a program that will allow the user to type in five words which will take the middle letter from each word and combine those middle letters to form a secret message.


print("Secret Service Program")

word_1 = input("Please enter the first word: ") # This is the variable sword_1, which allows the user to input the first word, or the culminating secret message. 
if (len(word_1)% 2) == 0: # This line of code enables the program to determine if the length of the word is divisible by two and if it has a remainder. 
# The above line of code contains an 'if' statement and an 'else' statement. The 'if' and the 'else' staments is a conditional control statment that operates if the condition has been met.
    print('Please enter an odd letter word' ) # This line of command prints out the word in the string, only if the 'if' command is followed. 
else: # This line of code contains the else command, this will only be followed if the 
    code_letter_number_1 = int(round((len(word_1)/2),1)) # this is a variable 'code_letter_number_1' and this variable also has calculations attached to it.
    # The above line of code contains calculations that allow the program to find the length of the word. It also contains a round function, which rounds it 1 place up so that it is suitable for odd numbers. 
    middle_letter_1 = (word_1[(code_letter_number_1)]) # This line of code contains the variable middle_letter_1. This variable allows the program to choose the middle letter of the number which will lead to the culminating, secret word. 
    # The above line of code contains the method for calculating the middle letter of the word inputed, by finding the code letter number of the word_1
    
word_2 = input("Please enter the second word: ") # This is the variable word_2, which allows the user to input the second word, of the culminating secret message. 
if (len(word_2)% 2) == 0:# This line of code enables the program to determine if the length of the word is divisible by two and if it has a ramiander.
    # The above line of code contains an 'if' statement and an 'else' statement. The 'if' and the 'else' staments is a conditional control statment that operates if the condition has been met.
    print('Please enter an odd letter word' ) # This line of command prints out the word in the string, only if the 'if' command is followed. 
else: # This line of code contains the else command, this will only be followed if the 'if' command above is followed. 
    code_letter_number_2 = int(round((len(word_2)/2),1)) # This is code letter number 2 variable. This allows the program to calculate the length of the odd letter word and round it appropriately.
     # The above line of code contains calculations that allow the program to find the length of the word. It also contains a round function, which rounds it 1 place up so that it is suitable for odd numbers. 
    middle_letter_2 = (word_2[(code_letter_number_2)]) # This line of code contains the variable middle_letter_2. This variable allows the program to choose the middle letter of the number which will lead to the culminating, secret word. 
    # The above line of code contains the method for calculating the middle letter of the word inputed, by finding the code letter number of the word_2

word_3 = input("Please enter the third word: ") # This is the variable word_3, which allows the user to input the third word, of the culminating secret message. 
if (len(word_3)% 2) == 0: # This line of code enables the program to determine if the length of the word is divisible by two and if it has a ramiander.
    # The above line of code contains an 'if' statement and an 'else' statement. The 'if' and the 'else' staments is a conditional control statment that operates if the condition has been met.
    print('Please enter an odd letter word' ) # This line of command prints out the word in the string, only if the 'if' command is followed. 
else: # This line of code contains the else command, this will only be followed if the 'if' command above is followed. 
    code_letter_number_3 = int(round((len(word_3)/2),1)) # This is code letter number 3 variable. This allows the program to calculate the length of the odd letter word and round it appropriately.
     # The above line of code contains calculations that allow the program to find the length of the word. It also contains a round function, which rounds it 1 place up so that it is suitable for odd numbers. 
    middle_letter_3 = (word_3[(code_letter_number_3)]) # This line of code contains the variable middle_letter_3. This variable allows the program to choose the middle letter of the number which will lead to the culminating, secret word. 
    # The above line of code contains the method for calculating the middle letter of the word inputed, by finding the code letter number of the word_3

word_4 = input("Please enter the fourth word: ") # This is the variable word_4, which allows the user to input the fourth word, of the culminating secret message. 
if (len(word_4)% 2) == 0:# This line of code enables the program to determine if the length of the word is divisible by two and if it has a ramiander.
    # The above line of code contains an 'if' statement and an 'else' statement. The 'if' and the 'else' staments is a conditional control statment that operates if the condition has been met.
    print('Please enter an odd letter word' ) # This line of command prints out the word in the string, only if the 'if' command is followed. 
else: # This line of code contains the else command, this will only be followed if the 'if' command above is followed. 
    code_letter_number_4 = int(round((len(word_4)/2),1))# This is code letter number 4 variable. This allows the program to calculate the length of the odd letter word and round it appropriately.
    # The above line of code contains calculations that allow the program to find the length of the word. It also contains a round function, which rounds it 1 place up so that it is suitable for odd numbers. 
    middle_letter_4 = (word_4[(code_letter_number_4)]) # This line of code contains the variable middle_letter_4. This variable allows the program to choose the middle letter of the number which will lead to the culminating, secret word. 
    # The above line of code contains the method for calculating the middle letter of the word inputed, by finding the code letter number of the word_4
    
word_5 = input("Please enter the fifth word: ") # This is the variable word_4, which allows the user to input the fifth word, of the culminating secret message. 
if (len(word_5)% 2) == 0: # This line of code enables the program to determine if the length of the word is divisible by two and if it has a ramiander.
    print('Please enter an odd letter word' ) # This line of command prints out the word in the string, only if the 'if' command is followed. 
else: # This line of code contains the else command, this will only be followed if the 'if' command above is followed. 
    code_letter_number_5 = int(round((len(word_5)/2),1)) # This is code letter number 5 variable. This allows the program to calculate the length of the odd letter word and round it appropriately.
    # The above line of code contains calculations that allow the program to find the length of the word. It also contains a round function, which rounds it 1 place up so that it is suitable for odd numbers. 
    middle_letter_5 = (word_5[(code_letter_number_5)]) # This line of code contains the variable middle_letter_4. This variable allows the program to choose the middle letter of the number which will lead to the culminating, secret word. 
    # The above line of code contains the method for calculating the middle letter of the word inputed, by finding the code letter number of the word_5

    
if (len(word_1)% 2) == 0 or  (len(word_2)% 2) == 0 or  (len(word_3)% 2) == 0 or (len(word_4)% 2) == 0 or (len(word_5)% 2) == 0: # This line of code contains all of the word inputed and has a conditional command. 
    # The above line of code contains a conditional statement which wont allow the program to run if one or more of the word have even letters in it, since the program wanted odd words. 
    print ('One or more of your inputed words is an even word. Please run the program again. Thanks:)') # This line of code contains a print command only if the 'if' command is followed above.
else: # This contains the else command which will be followed if the 'if' command is not followed.
    print("The secret message is", middle_letter_1,middle_letter_2,middle_letter_3,middle_letter_4,middle_letter_5) # This line of code contains an print command which printe out the middle letter of each word inputer, to give out the secret word or the secret message. 


                                                    ##This code took approximately about 3 - 4 tries to make it correct and to enable it to meet the requirements. ##
