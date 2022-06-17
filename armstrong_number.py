#How to check a number is armstrong or not?
# A Armstrong number is equal to the number in any given number base, which forms the total of the same number, when each of its digits is raised to the power of the number of digits in the number.
# For ex- 153, 370, 371, 1634 and so on..

n = int(input("Enter a number: "))
length = int(len(str(n)))

k=0 
temp=n

if temp <= 0:
    print("Invalid input!!.Enter a  number greater than 1")
else:
    while temp > 0:
        dig = temp%10
        k += dig**length
        temp = temp//10
    if k == n:
        print(f"Yes, {n} is a Armstrong number")
    else:
        print(f"No, {n} is not a Armstrong number!")
