from calculator1 import Add, Subtract, Multiply, Divide                                   

def menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
choice = int(input("Enter your choice (1 to 4): "))    
a = int(input("the Enter the 1 number: "))
b = int(input("the Enter the 2 number: "))

if choice == 1:
    result = Add(a , b)
    print("Result: ",result)
    
elif choice == 2:
    result = Subtract(a , b)
    print("Result: ",result)   
    
elif choice == 3:
    result = Multiply(a , b)
    print("Result: ",result)
    
elif choice == 4:
    result = Divide(a , b)
    print("Result: ",result)   
    
elif choice == 5:
    print("Exit the choice")
else:
    print("Invalid the choice")
    
    menu()    # repeat menu

menu()        # start menu

    

    
    
