weight = int(input('input weight (lbs)(integer number)'))/2.20462
height = int(input('input height (ft)(integer number)'))/3.281
storage = int(input('input height (in)(integer number)'))/39.372
height=height+storage
BMI=weight/height**2
print('Your BMI is', BMI, "assuming you are an adult male you are ", end = "")
if BMI<18.5:
    print('underweight')
elif BMI<25:
    print('of a healthy weight')
elif BMI<30:
    print('overweight')
else:
    print('obese')
