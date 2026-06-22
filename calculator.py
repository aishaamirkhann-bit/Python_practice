num1=float(input("enter first number: "))
operator=input("enter any sign(+,-,*,/): ")
num2=float(input("enter second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("result:", num1 / num2)
    else:
        print("number is not divisible by zero")
else:
    print("Invalid operator")