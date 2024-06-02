try:
    a = input("Enter a:")
    b = input("Enter b:")
    if b == 0:
        raise ZeroDivisionError
    else:
        print("a/b")
except ZeroDivisionError:
    print("zerodivisionerror: division by zero")
except ValueError:
    print("please use a and b as integer value !")