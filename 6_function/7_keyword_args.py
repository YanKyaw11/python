def calculator(a, b, c):
    return(a + b) * c

a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

print("Result = ", calculator(A=c, b=b, a=a))

#TypeError: calculator 'A' keyword not found.