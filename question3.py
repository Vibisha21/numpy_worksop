#write a program to find the factorial of a nummber
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
n= int(input("Enter a number to find its factorial"))
print(fact(n))
