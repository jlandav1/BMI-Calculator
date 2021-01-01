import time

print("Good day to you!")
time.sleep(1)
name = input("What's your name? ")
time.sleep(1)
def personalized_greeting():
    """Adds user's name to greeting string"""
    print("Hi " + name + "!")
personalized_greeting()
time.sleep(1)
age = input("How old you are you? ")
time.sleep(1)
def age_response():
    """"A response to user's age revelation."""
    if int(age) < 30: 
        print("You got the whole world ahead of you!")
    if int(age) >= 30 and int(age) <= 40: 
        print("30's baby, let's go!")
    if int(age) > 40 and int(age) < 70: 
        print("Middle-aged I see!")
    if int(age) > 70: 
        print("You are aging wonderfully!")
age_response()
time.sleep(1)
print("What is your weight?" )
time.sleep(1)
weight_lbs = input( "Pounds = ")
time.sleep(1)
kilograms = int(weight_lbs) * float(0.453592)
print("What is your height? ") 
time.sleep(1)
height_feet = input( "Feet = " )
time.sleep(1)
height_inches = input( "Inches = ")
time.sleep(1)
feet_inch_conv = int(height_feet) * 12
meters = (feet_inch_conv + int(height_inches)) * float(0.0254)
BMI_calc_float = kilograms/meters**2
BMI_calc = round(BMI_calc_float, 1)
Optimal_weight_calc = round(abs(21.5 - BMI_calc) * 2.20462) 
if BMI_calc < 18.5: 
    print(name , ", your BMI is ", BMI_calc, ", you are underweight. However, you are well on your way to achieving a healthy weight!", "Gaining ", Optimal_weight_calc, " more pounds will put you at your optimal weight. Keep working hard my friend.")
if  BMI_calc >=18.5 and BMI_calc <= 24.9: 
    print("Nice job! " , name , ", Your BMI is ", BMI_calc,".", "You are at a healthy weight and size.")
if BMI_calc >= 25 and BMI_calc < 30: 
    print(name , ", your BMI is ", BMI_calc, ", you are overweight. However, you are well on your way to achieving a healthy weight!", "Losing ", Optimal_weight_calc, " more pounds will put you at your optimal weight. Keep working hard my friend.")
if BMI_calc >= 30: 
    print(name , ", your BMI is ", BMI_calc, ", you are overweight. However, you are well on your way to achieving a healthy weight!", "Losing ", Optimal_weight_calc, " more pounds will put you at your optimal weight. Keep working hard my friend.")
