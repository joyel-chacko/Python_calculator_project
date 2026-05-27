print("===Calculator App===")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
print("=====================")

running = True


def calculator():
        def add():
            result = first_number + second_number
            return result

        def subtract():
            result = first_number - second_number
            return result

        def multiply():
            result = first_number * second_number
            return result

        def divide():
            result = first_number / second_number
            return result

        def exit():
            return "Goodbye! 👋"



               
        choice = int(input("Enter your choice: "))

        with open("calculations.txt", "a") as file:
            
        
            if choice == 1:
                first_number = int(input("Enter first number: "))
                second_number = int(input("Enter second number: "))
                addition = add()
                print(f"Result: {first_number} + {second_number} = {addition}")
                addition_string = str(addition)  
                file.write('\n'+addition_string)
                print("Calculation saved!")
                

            elif choice == 2:
                first_number = int(input("Enter first number: "))
                second_number = int(input("Enter second number: "))
                subtraction = subtract()
                print(f"Result: {first_number} - {second_number} = {subtraction}")
                subtraction_string = str(subtraction)
                file.write('\n'+subtraction_string)
                print("Calculation saved!")

            elif choice == 3:
                first_number = int(input("Enter first number: "))
                second_number = int(input("Enter second number: "))
                multiplication = multiply()
                print(f"Result: {first_number} * {second_number} = {multiplication}")
                multiplication_string = str(multiplication)
                file.write(multiplication_string)
                print("Calculation saved!")

            elif choice == 4:
                first_number = int(input("Enter first number: "))
                second_number = int(input("Enter second number: "))
                division = divide()
                print(f"Result: {first_number} / {second_number} = {division}")
                division_string = str(division)
                file.write(division_string)
                print("Calculation saved!")

            elif choice == 5:
                print(exit())


try:

    calculator() 
    asking = input("Do you want to calculate again? (yes/no):")

except ValueError:
    print("Invalid!")

while running:

 try :

    if asking == 'yes':
        calculator()
        asking = input("Do you want to calculate again? (yes/no):")

    elif asking == 'no':
        print("Goodbye! 👋")
        running = False
 except NameError:
     print("Error 404!")
     running = False
 except ValueError:
     print("Error 404!")
     running = False

