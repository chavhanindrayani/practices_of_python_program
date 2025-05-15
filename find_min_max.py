# write a program that takes a list of numbers as input and use a loop to find the max and min numbers
# without using the buit-in number
number = [47,90,78,60,45,23]
smallest = min = number[0]
llargest = max = number[0]

for i in range(len(number)):
    if number[i] < min:
        min = number[i]
    elif number[i] > max:
        max = number[i]
        
print("min",min)
print("max",max)



"""def find_min_max(numbers):
    if not numbers:
        return None
    smallest = min(numbers)
    largest = max(numbers)
    return smallest, largest

nums = [4,1,9,7,3]
result = find_min_max(nums)
if result:
    print("smallest :{result[0]}, largest :{result[1]}")
else:
    print("the list is empty.")"""
    
    
    
# find the second last largest number
"""nums = [10, 20, 4, 45, 99]
nums.sort()
print(nums[-2])"""
