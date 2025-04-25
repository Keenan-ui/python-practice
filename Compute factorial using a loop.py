def factorial_loop():
    num=int(input("Enter a number:")) #User enters the number which is to be computed
    result=num #Create another variable to hold the number which will store the final answer
    while num>1: #Multplies and updates result by descending values of num until 1
        num-=1
        result*=num
    print("The factorial of the number is: ")
    print(result)

factorial_loop()
