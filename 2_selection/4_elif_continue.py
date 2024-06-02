age = int(input("How old are you ?"))

if age > 85 and age <= 100:
    print("very old")
elif age > 60 and age <= 85:
    print("old")
elif age > 40 and age <= 60:
    print("very old")
elif age > 30 and age <= 40:
    print("very aldult")
elif age > 20 and age <= 30:
    print("adult")
elif age > 10 and age <= 20:
    print("young")
else:
    print("Invaild age")