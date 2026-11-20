#1405/08/28
#calculator

def calculator(num1 , num2 , operator) :
    #switch case
    match operator :
        #add
        case "+" :
            return num1 + num2
        #minus
        case "-" :
            return num1 - num2
        #multiply
        case "*" :
            return num1 * num2
        #divide
        case "/" :
            if num2 == 0 : 
                return "Cannot divide by ZERO !"
            return num1 / num2 
        #percent
        case "%" :
            return (num1 * num2 // 100 )
        #power
        case "^" :
            result = 1
            for i in range (num2) :
                    result = result * num1
            return result

        case _:
            return "Invalid operator"

while True :
    user_input = input ("Enter first number or (press 'q' to quit) : ")

    if user_input.lower() == "q" :
        print ("Goodbye")
        break

    elif not user_input.isdigit():
        print("Please enter a valid number!")
        continue

    num1 = int(user_input)
    user_input2 = input("Enter second number or (press 'q' to quit) : ")
        
    if user_input2.lower() == "q" :
        print ("Goodbye")
        break

    elif not user_input2.isdigit():
        print("Please enter a valid number!")
        continue
    num2 = int(user_input2)
    operator = input("Enter operator (* , / , + , - , % , ^) or (press 'q' to quit) : ")
    if operator.lower() == "q" :
        print ("Goodbye")
        break

    result = calculator(num1 , num2 , operator)
    print ("Result: " , result )