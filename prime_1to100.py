# write a program that takes a all prime number between 1 to 100 using 
print("prime number between 1 to 100")
for i in range(1, 101):
    if i > 1:
        for j in range(2, i):
            if i%j == 0:
                break
        else:
            print("the prime",i)
        
