# write program that print the fillowing pattern using nested loop for n = 5:
#output pattern 1
#               1 2
#               1 2 3
#               1 2 3 4
#               1 2 3 4 5

for i in range(5):               #row
    for j in range(i+1):         #column
        print(j+1, end=" ")
    print()