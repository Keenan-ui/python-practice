def sum_of_digits():
    num=int(input("Enter a number: "))
    sum=0 #Holds the sum of the digits of num
    for digit in str(num): #Every digit in the number is added to sum
        sum+=int(digit)
    return sum

result=sum_of_digits()
print(result)