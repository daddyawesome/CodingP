# BMI calculator
name1 = "Daddy Awesome"
height_m1 = 1.6
weight_kg1 = 82

name2 = "Eleonore"
height_m2 = 1.52
weight_kg2 = 70

name3 = "Yumi"
height_m3 = 1.2
weight_kg3 = 35

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight"
    else:
        return name + " is overweight"
    
result1 = bmi_calculator(name1, height_m1,weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)

print(result1)
print(result2)
print(result3)
