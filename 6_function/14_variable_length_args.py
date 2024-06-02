def signup_member(**kwargs):
    for i,a in kwargs.items():
        print(f"{i}=>{a}")

signup_member(name="Kyaw Kyaw",age="25",gender="Male")