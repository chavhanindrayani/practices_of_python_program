Number = int(input("Enetr the number : "))

if Number % 3==0 and Number % 5==0:
    print("number is divisible by 3 or 5")
elif Number % 3==0:
    print("numbner is divisible by 3")
elif Number % 5==0:
    print("number is divisible by 5")
else:
    print("number is not divisible by 3 or 5")