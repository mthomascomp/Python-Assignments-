# Mervin Thomas     
# Mr. Kyle Batterink
# ICS3U - b
# April 15, 2016


# The following line of code contains def statements that allow the program to basicallly create a new set of command for the computer.
# It also has the return value which will return the ammount of the desired conversion method.

#does kilometers to miles calculation and returns the value in miles
def km_mi(value):
    return round((value/1.6),2)
#does miles to kilometers calculation and returns the value in kilometers
def mi_km(value):
    return round((value*1.6),2)
def in_cm(value):
    return round((value*2.54),2)
#does centimeters to inches calculation and returns the value in inches
def cm_in(value):
    return round((value/2.54),2)
#does feet to centimeters calculation and returns the value in centimeters
def ft_cm(value):
    return round((value*30),2)
#does centimeters to feet calculation and returns the value in feet
def cm_ft(value):
    return round((value/30),2)
#does yards to meters calculation and returns the value in meters
def yd_m(value):
    return round((value*0.91),2)
#does meters to yards calculation and returns the value in yards
def m_yd(value):
    return round((value/0.91),2)

#shows user input user_choices
print("1. Inches to Centimeters\n2. Centimeters to Inches\n3. Feet to Centimeters\n4. Centimeters to Feet\n5. Yards to Meters\n6. Meters to Yards\n7. Miles to Kilometers\n8. Kilometers to Miles")
#asks user for input
print("\nEnter your user_choice:")
# user user_choice into varible as int
user_choice = int(input())
#allows the user to enter the value
print("Enter value to be converted:")
#stores the input as a float
value = float(input())

#prints the right choice on the screen of the user. 
if user_choice == 1:
    print(in_cm(value),"centimeters")
elif user_choice == 3:
    print(ft_cm(value),"centimeters")
elif user_choice == 4:
    print(cm_ft(value),"feet")
elif user_choice == 2:
    print(cm_invalue),"inches")
elif user_choice == 6:
    print(m_yd(value),"yards")
elif user_choice == 5:
    print(yd_m(value),"meters")
elif user_choice == 8:
    print(km_mi(value),"miles")
elif user_choice == 7:
    print(mi_km(value),"kilometers")
else:
    #prints if an invalid choice  is made by the user. 
    print("Invalid error")


# This program took about 7 - 8 tries to make it correct according to the rubrics
