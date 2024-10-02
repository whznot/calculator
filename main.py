print("write an expression: ", end='')
user_input = input()


def parse_expression(expression):
    nums = []
    operators = []
    current_num = ''

    for char in expression:
        if char.isnumeric():
            current_num += char
        elif char in '+-/*':
            nums.append(current_num)
            operators.append(char)
            current_num = ''
        else:
            return "expression is invalid"


parse_expression(user_input)
