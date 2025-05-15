# write a function reverse_string(s) that takes a string as input and returns the string reverse without using slicing('[::-1]')
def reverse_string(s):
    reverse_str = ' '
    for char in s:
        reverse_str = char + reverse_str
    return reverse_str

origanal_string = "Indrayani"
result = reverse_string(origanal_string)        
print(f"origansl string : ", origanal_string)
print(f"reverse string : ", result)

# write string reverse with using slicing('[::-1]')
"""def reverse_string(s):
    reverse_str = s[::-1]
    return reverse_str

    origanal_string = "hello, world"
    result = reverse_string(origanal_string)        
    print(f"origansl string : ", origanal_string)
    print(f"reverse string : ", result)"""
    

