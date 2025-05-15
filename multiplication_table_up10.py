#write program take number as input and print the multiplication table up to 10 using for loops.
#num = int(input("Enter the number : "))
for i in range(1, 11):
    print(f"table of i {i}")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j} ")
    
