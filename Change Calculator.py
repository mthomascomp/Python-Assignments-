# Mervin Thomas
# Mr. Kyle Batterink
# ICS3U-b
# March 28, 2016

# Program Name - Change Calculator
# Program Instructions - Make a program that will give the exact ammount of each type of change when the user inputs the total price and the ammount given to the cashier. 

print ("Change Calclator") # This line of code prints out the title change program whcih makes it look neat. 

fifty_dollar_bill = 50 #This is the variable called fifty dollar bill which is assigned to a value of 50
twenty_dollar_bill  = 20 # This is a twenty dollar bill whcih is assigned to avalue of 20 
ten_dollar_bill = 10 # This is a ten dollar bill, whcih is assigned to a value of 10 
five_dollar_bill = 5 # This is a five dollar bill whcih is assigned to a value of 5 
two_dollar_bill = 2 # This is a two dollar bill whcih is assigned to a value of 2 
one_dollar_bill = 1 # This is a one dollar bill which is assigned to a value of 1 
quarter = 0.25 #This is a warter coin whcih is assigned to a value of 0.25
dime = 0.10 # This is a dime coin which value is assigned to a value of 0.10
nickel = 0.05 # This is a nickle coin which value is assigned to 0.05
penny = 0.01 # This is a penny coin which value is assigned to 0.01 

item_cost = float(input("Enter the total price: $ ")) # This variable is called item _cost. It allows the user to input the total price of the product purchased, so the program can calculate the change.
# The above line of code contains a float command. This float command allows the program to conver the string to a decimal number. 
moneygiven = float(input("Enter how much money given: $ ")) # This variable is called moneygiven. It allows the user to input the ammount of money given to the cashier, so that the program can calculate the change.
moneyback = moneygiven - item_cost # This line of code allows the program to calculate the change of the ammount given and recieved. 

fiftydmb = int(moneyback / fifty_dollar_bill) # This line of code assigns to the variable fifty dmb. Which stands for fifty dollar money back.
# The above line of code calculates the division of moneyback and fifty dollar bill variable, as mentioned above. 
fiftydnewbalance=moneyback-fiftydmb*fifty_dollar_bill # This lines of code allows us to caculate the fiftydmb * the fifty dollar bill. 

twentydmb=int(fiftydnewbalance / twenty_dollar_bill) # This line of code assigns to the variable fifty dmb. Which stands for fifty dollar money back.
# The above line of code calculates the division of fiftydmb and twenty dollar bill variable, as mentioned above. 
twentydnewbalance=fiftydnewbalance-twentydmb*twenty_dollar_bill # This lines of code allows us to caculate the fiftynewdmb * the twenty dollar bill. 

tendmb=int(twentydnewbalance / ten_dollar_bill) # This line of code has the ten dollar money back variable. This allows the twenty new balance divided by the ten dollars bill variable.
# The above line of code also contains an integer, which allows the program to convert the answer to an integer. 
tendnewbalance=twentydnewbalance-tendmb*ten_dollar_bill # This line of code caculates the new ten dolla balance which we have. 

fivedmb=int(tendnewbalance / five_dollar_bill) # This line of code is the five dollar back balance, which is the integer of the ten new balance divided by the five dollar bill variable value. 
fivednewbalance=tendnewbalance-fivedmb*five_dollar_bill #This is the vairable five new balance which allws the program to store in a new five dollar back value. 

twodmb= int(fivednewbalance / two_dollar_bill) # This line of code allows the program to calculate the two dollar balance.
# The above line of code also contains an integer command, which converts the answer to an integer. 
twodnewbalance=fivednewbalance-twodmb*two_dollar_bill #This is the new two dollar balance which makes it easier for us to calculate it further down as we go. 

onedmb=int(twodnewbalance / one_dollar_bill) #This is one dollar back balance, this allows the program to calculate the balance of one dollar. 
onednewbalance=twodnewbalance-onedmb*one_dollar_bill # This variable allows the program to calculate the new one dollar balance. 

print (fiftydmb,"$ 50 Bill") # This line of code prints out the ammount of fifty dollar we need. 
print (twentydmb,"$ 20 Bill") # This line of code prints out the ammount of ten dollar we need. 
print (tendmb,"$ 10 Bill") # This line of code prints out the ammount of ten dollar we need. 
print (fivedmb,"$ 5 Bill") # # This line of code prints out the ammount of five dollar we need. 
print (twodmb,"$ 2 Bill")# This line of code prints out the ammount of two dollar we need. 
print (onedmb,"$ 1 Bill") # This line of code prints out the ammount of one dollar we need. 


moneybacknew=moneyback-int(moneyback) # This is the new variable which is money back new and which calculates the decimals of the money
quarter_money_back = int(moneybacknew / quarter) # This variable allows the program to calculate, the ammount of quarters needed. 

partialtotal = moneybacknew - quarter_money_back * quarter # This variable is the first partial total and calculate the partial ammount of money remaining. 

dimes_money_back = int(partialtotal / dime) # This variable calculates the dime money back, by dividing the integer of the partial total by dime
dpartialtotal = partialtotal - dimes_money_back * dime # This line of code contains the partial total - the ammount of dimes needed. 

nickel_money_back = int(dpartialtotal / nickel) # This line of code calculate the integer of the dime partial total and divide it by the value of a nickle 
npartialtotal = dpartialtotal - nickel_money_back * nickel # This line of code contains the clauclations of the n partial total 

penny_money_back = int(npartialtotal / penny) + int(round((0.99),1)) # This line of code calculates the integer of the nickle partial total and divides it by the value of penny 
penny_partial_total = npartialtotal - penny_money_back * penny # This line of code calculate the penny partial total 

print(quarter_money_back, 'quarters' ) # This line of code prints out howmuch of quarter money is needed. 
print(dimes_money_back,'dime') # This line of code prints out how much of dime money is needed. 
print(nickel_money_back,'nickels') # # This line of code prints out how much of nickel money is needed. 
print(penny_money_back, 'pennys') # This line of code prints out howmuch of penny money is needed.

# This program took about 5-6 tries to complete it and to get the right results. 


