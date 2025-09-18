#calculate simple calculation using python 

#user inputed

number1=float(input("Enter first number is : "))
number2=float(input("Enter second number is : "))

print("\nchoose your operation : ")
print("Addition(+)")
print("Subtration(-)")
print("multition(*)")
print("Division(/)")

select=input("Enter selected operator(+,-*,/):")
#perform our calculation

if select=="+":
    result=number1+number2
    print(f"\nResult: {number1}+{number2}={result}")

elif select=="-":
    result=number1-number2
    print(f"\nResult: {number1}-{number2}={result}")

elif select=="*":
    result=number1*number2
    print(f"\nResult: {number1}*{number2}={result}")

elif select=="/":
    result=number1/number2
    print(f"\nResult: {number1}/{number2}={result}")

else:
    print("\nYou have select an invalid operation." )

