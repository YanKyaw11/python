try:
    a = input("Enter a :")
    if not a.isnumeric():
        raise ValueError
    else:
        pass
except ValueError:
    print("Plase use a as integer value !")