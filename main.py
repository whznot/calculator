print("write a number: ", end='')


def get_valid_number(prompt):
    try:
        return int(prompt)
    except ValueError:
        print("write a valid number")


num1 = get_valid_number(input())

print("choose operation:\n1. +\n2. -\n3. *\n4. /\n5. %\n6. **")
operation = input()
availableOperations = ['+', '-', '*', '/', '%', '**']

print("write a number: ", end='')
num2 = get_valid_number(input())

if operation in availableOperations:
    match operation:
        case '+':
            result = num1 + num2
        case '-':
            result = num1 - num2
        case '*':
            result = num1 * num2
        case '/':
            result = num1 / num2
        case '%':
            result = num1 % num2
        case '**':
            result = num1 ** num2
        case _:
            result = "enter a valid operation"
else:
    result = "enter a valid operation"

print(result)

print("want to add more numbers? (y/n)")
