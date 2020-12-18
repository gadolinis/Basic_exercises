# simple expample

#num1 = input("Enter first number: ")
#num2 = input("Enter another number: ")
#result = float(num1) + float(num2)      # float - realus skaiciai; int - sveiki skaičiai

#print(result)

# More advanced calculator
###

q_simbolis = "a"

while (q_simbolis != "q"):

    num1 = float(input("Enter first number: "))
    op = input("Enter operator: ")
    num2 = float(input("Enter second number: "))

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1-num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "^":
        print (num1 ** num2)
    else:
        print("Invalid operator")

    print("Tęsiame")
    q_simbolis = input("Nutraukti? (q) ")
