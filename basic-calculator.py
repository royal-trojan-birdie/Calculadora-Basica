# Despues intentar una calculadora en la que puedas elegir cuantos numeros poner sin uso de mucho codigo

print("Welcome to the")
print("CALCULATOR DUO\n")
firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))
print()
print("+ Plus, - Minus, * Multiply, / Divide")
operationSelect = str(input("Enter the operation: "))

def calculate(a, b, c):
    if c == "+":
        return a + b
    if c == "-":
        return a - b
    if c == "*":
        return a * b
    if c == "/":
        return a / b
    else:
        return

print(calculate(firstNumber, secondNumber, operationSelect))

