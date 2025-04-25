def even_or_odd():
    num=int(input("Enter your number: ")) #User enters the number to be checked
    print("Is it even?")
    if num%2==0: #Checks whether the number is divisible by 2, hence whether it's even
        return True
    else:
        return False

result=even_or_odd()
print(result)