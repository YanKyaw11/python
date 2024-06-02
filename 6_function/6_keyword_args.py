def calculator(a, b, c):
    return(a + b) * c

a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

print("Result = ", calculator(c=c, b=b, a=a))