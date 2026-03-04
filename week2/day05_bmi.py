height_cm = float(input("height(cm): "))
weight = float(input("weight(kg): "))

height_m = height_cm / 100
bmi = weight / (height_m * height_m)

if bmi < 18.5:
    print(f"BMI: {round(bmi, 1)} 판정: 저체중")
elif bmi < 23:
    print(f"BMI: {round(bmi, 1)} 판정: 정상")
elif bmi < 25:
    print(f"BMI: {round(bmi, 1)} 판정: 과체중")
else:
    print(f"BMI: {round(bmi, 1)} 판정: 비만")