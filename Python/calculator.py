import re

def multiplyDivide(match) :
    num1, operator, num2 = match.groups()
    num1 = float(num1)
    num2 = float(num2)
    
    if operator == 'x':
        return str(num1 * num2)
    elif operator == '/':
        return str(num1 / num2)

def addSubtract(match) :
    num1, operator, num2 = match.groups()
    num1 = float(num1)
    num2 = float(num2)
    
    if operator == '+':
        return str(num1 + num2)
    elif operator == '-':
        return str(num1 - num2)

def remove_leading_zeros(match):
    num = match.group()
    num = num.lstrip('0')
    return num if num != '' else '0'

def compute(operation):
    result = operation.replace(' ', '')

    if re.search(r"[x/]{2,}|[x/][+]|[\+\-][x/]|[+\-]{2,}", result):
        return "Invalid request"
    

    regex = r"(-?\d+(?:\.\d+)?)([x/])(-?\d+(?:\.\d+)?)"
    result = re.sub(regex, remove_leading_zeros, result)

    result = re.sub(regex, multiplyDivide, result)
    regex = r"(-?\d+(?:\.\d+)?)([+\-])(-?\d+(?:\.\d+)?)"

    while re.search(regex, result):
        result = re.sub(regex, addSubtract, result)

    return result


print('*** This is a console calculator ***')
print('Type the operation you wish to calculate and press Enter.\n')
operation = input('The valid operators are +, -, x, / and . for decimals.\n')

print(compute(operation))

