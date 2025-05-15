#write function is_prime(num) that takes a number as input and result 'True' if the number is prime, otherwise 'False'
def is_prime(num):
    i = 1
    count = 0
    if num % 1 == 0:
        count = count + 1
        i = i + 1
        return True   
    elif count == 2:
        return True      #prime
    else:
        return False     #not prime
    
print(is_prime(6))