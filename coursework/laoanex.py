# jane owns a money lending buisness called save to grow. credit that loans out money.a given client of his company is givena loan that has to be repaid in a months time(30 days).or less with 10%
# interest. if the client fails to pay at th end of 30days, the client is charged a finr of 1%of the loan per. 
# Write a pythin application that determines the totalammount hta is paid to the company after the given number of days.

name=input("please enter your name: ")
ammount=int(input("Please enter the ammount of loan you want to get in shs.: "))
days=int(input("Enter the number of days spent with the loan: "))
interest_rate=(float((10/100)*ammount))
total=(ammount+interest_rate)
if days>=30:
    extra=(float((1/100)*ammount))*days
    total2=total+extra
    print("Hello",name,"Your total ammount to pay back is shs.:", total2)
else:
    print("Hello",name, "The total you are paying back is shs. ",total)

