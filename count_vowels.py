"""def count_vowels(s):
    string = "Programming"
    vowels = {
        a == 0,
        e == 0,
        i == 0,
        o == 0,
        u == 0
    }                                
    count = 0
    
    for c in s:
        if c in string:
            count = count+1                     
        return 
        """
        
#create a function count_vowels(string) that accepts a string and return the number of vowels(a,e,i,o,u) in the string,
# cosidering both upercase and lowercase
def count_vowels(s):
    vowels = "aeiouAEIOU"   
    count_vowels = 0
    vowels_present = " "
    for letter in s:
        if letter in vowels:
            count_vowels += 1
            vowels_present += letter
            
    print("Count of vowels is :",count_vowels)
    print("vowels present in string is :", vowels_present)
    
string = input("Enetr the number : ")
count_vowels(string)