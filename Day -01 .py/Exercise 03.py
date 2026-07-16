num1= int(input("Enter val 1:"))
num2= int(input("Enter val 2:"))
op = input("Enter a operator (+,-,*,/)")
if op =="+" :
    print("Result is:",num1+num2)
elif op =="-" :
    print("Result is:",num1-num2)
elif op =="*" :
    print("Result is:",num1*num2)
elif op =="/" :
    if num2 != 0:
        print("Result is:",num1/num2)
    else:
        print("Division by zeronis not possible.")
else:
    print("Invalid number.")
