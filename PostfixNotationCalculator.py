print("Welcome to Postfix Notation Calculator! First enter two numbers and then repeatedly enter an operator and number"
      " until the expression is finished!")

sum = 0
x = float(input())
sum += x

while True:
    y = input()
    if y == "=":
        break
    z = input()
    y = float(y)

    if z == "+":
        sum = sum + y
    elif z == "-":
        sum = sum - y
    elif z == "*":
        sum = sum * y
    elif z == "/":
        sum = sum / y
    else:
        raise SyntaxError("Read token %s, expected operator" % z)


print("Output: \n\t%.2f" % (sum))
