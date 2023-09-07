
def get_input(text, convert_to_float = True):
    print(f"Please provide the {text}")
    user_input = input()

    if convert_to_float:
        user_input = float(user_input)
    
    return user_input

def calculate(first_number, second_number, operator):
    first_number = float(first_number)
    second_number = float(second_number)

    if operator == "-":
        return first_number - second_number
    
    elif operator == "+":
        return first_number + second_number
    
    elif operator == "/":
        if second_number == 0:
            raise ValueError("Zero division not allowed")
        return first_number / second_number    
    
    elif operator == "*":
        return first_number * second_number
    
    else: 
        raise ValueError("Operator provided does not match operators available (+, -, *, /)")

if __name__ in "__main__":
    number1 = get_input("first number")
    number2 = get_input("second number")
    operator = get_input("operator", convert_to_float=False)

    output = calculate(number1, number2, operator)
    print(f"The result is: {output}")