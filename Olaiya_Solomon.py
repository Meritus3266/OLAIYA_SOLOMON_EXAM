# Question 1

def add(a,b):
        return a+b
def subtract(a,b):
         return a-b
def multiply(a,b):
        return a*b
def division(a,b):
        if b == 0:
         return f"division error"
        else:
            return a/b  
         
while True: 
    try:  
        a = int(input("please enter your first number: "))
        b = int(input("please enter your second number"))
        calc = input("choose calculator(+,-,*,/) rather 'exit' ")
        
        if calc == "+":
            print(f"result", add(a,b))
        
        elif calc == "-":
            print(f"result", subtract(a,b))

        elif calc == "*":
            print(f"result", multiply(a,b))

        elif calc == "/":
            print(f"result", division(a,b))
        elif calc.lower() == "exit":   
            print("exiting calc")
            break
        else:
            print("error. enter a correct number")
    except ValueError:
        print("What you enterd is invalid")




# Question 2

while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    if user_input == "exit":
        print("Goodbye!")
        break        # break out of loop
    
    num = int(user_input)   # convert to integer
    
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

#Question 3

while True:
    age = int(input("Enter your age (or type exit to quit): "))
    if age == exit:
        print("Goodbye!")
        break
    
    try:
        if age >= 18:
            print("You can vote")
        else:
            print("You cannot vote")
    except ValueError:
        print("Invalid input")