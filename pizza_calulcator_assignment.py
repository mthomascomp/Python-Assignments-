#Author: Mervin Thomas
#Course: ICS3U
#Instructor: Mr. Kyle Batterink
#Due Date: February 26, 2016

pizza_price = 12 #This is a variable which is called pizza_price. This assigns 12 dollars of value to a pizza.

money_billy= float(input('Billy, enter your money: $'))#This code is a variable which is enter_your_money1. This variable represents the input or the ammount of money the user(billy) will type in. 
#The above line contains a float and an input command. The input command allows the user billy to enter the ammount of money he has. The float command allows the user to enter decimal numbers without the program crashing.

money_sally = float(input('Sally, enter your money: $'))#This code is a variable which is enter_your_money2. This variable represents the input or the ammount of money the user(sally) will type in.
#The above line contains a float and an input command. The input command allows the user sally to enter the ammount of money she has. The float command allows the user to enter decimal numbers without the program crashing.

money_jesse = float(input('Jesse, enter your money: $'))#This code is a variable which is enter_your_money1. This variable represents the input or the ammount of money the user(jesse) will type in. 
#The above line contains a float and an input command. The input command allows the user Jesse to enter the ammount of money he has. The float command allows the user to enter decimal numbers without the program crashing.

total_money = int((money_billy) + (money_sally) + (money_jesse))#This variable represents the calculation which allows the program to calculate the ammount of money these three people have. It basically adds the three variabls whcih represent the ammount each individual has typed in. 
#The above command contains the command integer. Because it will add all the money the kids have to calculate the total ammount the group has.

number_of_pizza = int((total_money / pizza_price))#This variable represents the calculation for the number_of_pizza that can be bought with the ammount of money that is available. It takes the ammount of money that has been calculated before and divides it by the variable pizza, which has been assigned before. 
#The above contains an integer command because if the number of pizzas turn out to be an decimal, then that does not make sense. So it chops the decimal off in order to have the number of pizza rounded to a whole number.

print('You can buy', number_of_pizza, 'pizzas')#This is a print command, where it prints the text'you can buy' and it puts the variable(number_of_pizza) and then the text'pizza'. 
#The above command contains a string and a variable number_of_pizza that will be displayed, once all the inputs are completed. 

#This program took about 2-3 tries to get everything corrected, and to give logical outputs to the user. 
