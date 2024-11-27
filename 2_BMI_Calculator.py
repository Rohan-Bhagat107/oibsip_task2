print("Please enter your details here: ")
name=input("Please Enter your Name: ")
weight=float(input("Please Enter your weight: "))
height=float(input("Please Enter your height in centimeter: "))
height*=0.01

bmi=weight/height**2
if bmi<18.4:
    print(f"{name} you are underwight by {bmi} BMI")
elif bmi>18.4 and bmi<24:
    print(f"{name} you are normal by {bmi} BMI")
if bmi>=25 and bmi<29:
    print(f"{name} you are overweight by {bmi} BMI")
elif bmi>=30:
    print(f"{name} you have obesity by {bmi} BMI")
