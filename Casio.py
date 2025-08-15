#Operation
operator = input("Enter an operator (+ - * / or power): ")
num1 = float(input("Enter the First number: "))
num2 = float(input("Enter the Second number: "))
#processing
if operator == "+":
    answer = num1 + num2
    print(round(answer, 4))
elif operator == "-":
    answer = num1 - num2
    print(round(answer, 4))
elif operator == "*":
    answer = num1 * num2
    print(round(answer, 4))
elif operator == "/":
    answer = num1 / num2
    print(round(answer, 4))
elif operator == "power":
    answer = num1 ** num2
    print(round(answer, 4))
else:
    print(f"{operator},Enter a valid operation")