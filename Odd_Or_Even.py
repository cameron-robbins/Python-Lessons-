#Ask the user for a number. 
# Depending on whether the number is even or odd, 
# print out an appropriate message to the user.
# hint: how does an even / odd number react differently 
# when divided by 2?

num = int(input("Enter a number:"))
check = num % 2
if check > 0: 
    print ("odd")
else: 
    print("even")




#Extras:
#    If the number is a multiple of 4, print out a different message.
num = int(input("Enter a number:"))
check = num % 4

if check == 0 :
    print (num, "is a multuple of 4")
elif num % 2 :
    print (num, "is even")
else: 
    print (num, "is odd")




#Extras: 
#    Ask the user for two numbers: one number to check (call it num) 
#    and one number to divide by (check)
#    If check divides evenly into num, tell that to the user. 
#    If not, print a different appropriate message.

num = int(input("Enter a number:"))

check = int(input("Give me a number to divide by: "))

    
if num % check == 0 : 
    print ("Yes", num, "divides evenly by", check)
else: 
    print ("No", num, "does not divide evenly by", check)
    

