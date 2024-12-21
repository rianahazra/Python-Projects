#simple calculator
number1=float(input("Enter a number here"))
number2=float(input("Enter another number here"))
operator=input("Enter an operator here")
if operator=="+":
    sum=number1 + number2
    print(f'{number1} {operator} {number2} = {sum}') #addition
elif operator=="-":
    difference=number1 - number2
    print(f'{number1} {operator} {number2} = {difference}')#subtraction
elif operator=="x":
    product=number1 * number2
    print(f'{number1} {operator} {number2} = {product}')#multiplication
elif operator=="/":
    quotient=number1/number2
    print(f'{number1} {operator} {number2} = {quotient}')# actual division
elif operator=="//":
    quotient=number1//number2
    print(f'{number1} {operator} {number2} = {quotient}')# quotient no decimal
elif operator=="^":
    exponent=number1 ** number2
    print(f'{number1} {operator} {number2} = {exponent}')#power
elif operator=="%":
    remainder=number1 % number2
    print(f'{number1} {operator} {number2} = {remainder}')#remainder
else:
    print("Invalid operator")
