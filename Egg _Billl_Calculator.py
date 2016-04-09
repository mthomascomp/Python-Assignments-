# Mervin Thomas
# Mr. Kyle Batterink
# ICS3U - b 
# March 7, 2016

print ("Please insert the amount of eggs being purchased: ") # This line of code asks the user how many eggs they are buying.

number_of_eggs = int(input()) # Number of eggs is ammount of eggs the user inputs and the ammount of eggs the user puts into the program. 

if number_of_eggs > 0 and number_of_eggs <= 47: # This line of code contains an if command. This code tells that if the user is buying less than or equal to 47 eggs but greater than 0 then it will perform the command. 
    egg_value = (.5/12*number_of_eggs) # This variable is assigned to the price of the egg per dozen. It calculates how much money the consumer must pay for the egg based on the price in the assignment sheet. 

elif number_of_eggs >= 48 and number_of_eggs <= 71: # This line of code contains an if command. This code tells that if the user is buying less than or equal to 71 eggs but greater than 48 then it will perform the command. 
    egg_value = (.45/12*number_of_eggs) # This variable is assigned to the price of the egg per dozen. It calculates how much money the consumer must pay for the egg based on the price in the assignment sheet. 

elif number_of_eggs >= 72 and number_of_eggs <= 121: # This line of code contains an if command. This code tells that if the user is buying less than or equal to 121 eggs but greater than 72 then it will perform the command. 
    egg_value = (.40/12*number_of_eggs) # This variable is assigned to the price of the egg per dozen. It calculates how much money the consumer must pay for the egg based on the price in the assignment sheet. 

elif number_of_eggs >= 122:# This line of code contains an if command. This code tells that if the user is buying greater than or equal to 122 then it will perform the command. 
    egg_value = (.35/12*number_of_eggs) # This variable is assigned to the price of the egg per dozen. It calculates how much money the consumer must pay for the egg based on the price in the assignment sheet. 

print ("The cost will be $" +str((egg_value))) # This line of code shows how much money is needed to buy the eggs.

# The above line of code contains a string variable. This will help the program display the numbers in string format which is what we had started with in the beggining of the program. 




