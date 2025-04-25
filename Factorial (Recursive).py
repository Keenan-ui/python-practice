def factorial_recursive(num):
    if num==1:
        return 1 #base class
    else:
        return num*factorial_recursive(num-1)#recursive class #Multiplies the number by the factorial of the previous number

num=int(input("Enter a number: ")) #Prompts user for the number for calculations to be performed on
result = factorial_recursive(num)
print("The factorial of the number is: ")
print(result)