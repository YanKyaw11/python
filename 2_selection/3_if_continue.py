age = int(input("How Old Are You ?"))

if age > 85 and age <= 100:
    print("very old")
if age > 60 and age <= 85:
    print("old")
if age > 40 and age <= 60:
    print("Very Adult")
if age > 30 and age <= 40:
    print("adult")
if age > 20 and age <= 30:
    print("Young")
if age > 10 and age <= 20:
    print("Teenger")
if age > 1 and age <= 10:
    print("baby")
if age > 100 or age < 1:
    print("Invalid age !")