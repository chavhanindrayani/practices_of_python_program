"""n = int(input("Enter the number : "))
fact = 1
for i in range(1 ,n+1):
    fact = fact * i
print("Factorial number",fact) """

#impement a function factorial(num) that calculates the factorial of number using recursion.
def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num*factorial(num-1)
    
print(factorial(4))
