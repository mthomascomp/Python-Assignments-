#Author: Mervin Thomas
#Course: ICS3U - b
#Instructor: Mr. Kyle Batterink
#Due Date: February 26, 2016

first_payment_method = 15 #this is the first payment method where the saleswoman gets paid 15 dollars an hour. This is assigned to a variable which is: first_payment_method

second_payment_methoda = 10 #this is the second payment method where the saleswoman gets paid 10 dollars an hour. This is assigned to a variable : second_payment_methoda

second_payment_methodb = 7 #this is the second part of the second payment method where the saleswoman getspaid 7 dollars per sale, This is assigned to a variable: second_payment_methodb

third_payment_methoda = 5 #this is the third payment method where the saleswoman gets paid 5 dollars an hour. This is assigned to the variable : third_payment_methoda

third_payment_methodb = 12 #this is the second part of the third payment method, where the salewsoman gets paid 12 dollars per sale. This is assigned to the variable :third_payment_methodb

hours_worked = float(input('Please enter the ammount of hours the saleswoman worked:')) #this is variable hours_worked, where it allows the user to input the number of hours worked, and will convert that number into an integer so that there are no decimals and only whole numbers. 
#the above line contains a float and an input command. The input command allows the user to input the number of hours the saleswoman has worked. But the float commands allows the number to be the same wether it be a decimal or an whole number. 

hours_1 = int((first_payment_method * hours_worked)) #this is the variable hours_1, where it stores the variable and calculates the first_payment_method * hours_worked
#The reason it converts it into a integer is because the computer only reads number and therfefore will chop the extra decimals off when this command is applied.

hours_2 = int((second_payment_methoda * hours_worked))#this is the variable hours_2. This variable calculates the second payment method which is 10 dollars an hour * the number of hours the user inputs into the program. 
#the above line contains the command integer which means it will convert the inputs to an integer and chop the decimals off. 

hours_3 = int((third_payment_methoda * hours_worked))#this is the variable hours_3. It causes the third_payment_methoda to be multiplied with the number of hours worked. 
#The reason it converts it into a integer is because the computer only reads number and therfefore will chop the extra decimals off when this command is applied.

sales_womensales = float(input("please enter your sales:$"))
#The above line contains a float and an input command. This input command allows the user to input the ammount of sales in dollars the saleswman has had. The float command allows the input to remain in a decimal or in a whole number. 

sales_1 = int((second_payment_methodb * sales_womensales)) #This line contains the variable sales_1, whcih contains the command to multiply second_payment_methodb * sales_womensales and then converts it to an integer.  
#The reason it converts it into a integer is because the computer only reads number and therfefore will chop the extra decimals off when this command is applied.

sales_2 = int((third_payment_methodb * sales_womensales)) #This line contains the variable sales_2, which contains the command to multiply third_payment_methodb * sales_womensales and then converts it to an integer.
#The reason it converts it into a integer is because the computer only reads number and therfefore will chop the extra decimals off when this command is applied.

final_payment = max((sales_1 + hours_2), (sales_2 + hours_3), hours_1)  #This line allows the final payment to be calculated using the max command by commbing the total ammount of each variable like:
#sales_1 +hours_2 gives us the sales value + secondpayment
#sales_2+hours_3 gives us the sales value of the third payment option and adds it to the hours_3 variable which contains multi step as described above. 

print('The most the saleswoman could get paid is: $',final_payment,) #This line of code contains a string which displays the text. It contains a print command that allows the string to be displayed.
#The above line also contains a variable which is final_payment which will be displayed after all the input values are inserted in by the user.


# It took about 4-5 tries to make this program correctly and meet the basic requirements to make sure that the program completes the task. 


