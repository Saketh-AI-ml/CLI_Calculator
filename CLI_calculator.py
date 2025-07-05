# building of CLI calculator
num1 = float(input("Enter your First Number:"))
num2 = float(input("Enter your Second Number:"))
operator = input("operations to be performed(+,-,/,*,%,**,//):")
if operator=="+":
    print("The sum of the two numbers is:",num1+num2)
elif operator=="-":
    print("The subtract of the two numbers is:",num1-num2)
elif operator=="/":
    if num2==0:
        print("zero is not divisible")
    else:
        print("The division of the two numbers is:",num1/num2)
elif operator=="*":
    print("The multiplication of the two numbers is:",num1*num2)
elif operator=="%":
    print("The modules of the two numbers is:",num1%num2)
elif operator=="**":
    print("The square of the two numbers is:", num1**num2)
elif operator=="//":
    if num2==0:
        print("zero is not divisible")
    else:
        print("The Floor division of two numbers is:", num1//num2)
else:
    print("Error:please enter correct operator and values")