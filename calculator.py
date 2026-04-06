print("----CALCULATOR----")
while True:
    # MENU
    print("\n Choose a option: ") 
    print(" 1.Add")
    print(" 2.Subtract")
    print(" 3.Multiply")
    print(" 4.Divide")
    print(" 5.Quotient of division")
    print(" 6.Remainder of division")
    print(" 7.Exit")
    choice=input("\nEnter choice: ")

    if choice == "7": #Exit
        print("Exiting....")
        break
    try:
        num1 = int(input("Enter first number: ")) #User input first number
        num2 = int(input("Enter second number: ")) #User input second number
    except ValueError:
        print ("Input valid number only")
        continue

    if choice == "1": #Add
        Result=num1+num2 
        print("Result: ",num1+num2 )

    elif choice == "2": #Subtract
        print("Result: ",num1-num2)

    elif choice == "3": #Multiply
        print("Result: ",num1*num2)

    elif choice == "4": #Divide
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero")

    elif choice == "5": #Quotient
        if num2 != 0:
            print("Result:", num1 // num2)
        else:
            print("Cannot divide by zero")

    elif choice == "6": #Remainder
        if num2 != 0:
            print("Result:", num1 % num2)
        else:
            print("Cannot divide by zero")

    else:
        print("Invalid choice")
        

