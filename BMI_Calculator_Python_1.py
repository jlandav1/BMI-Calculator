# programs
import time
import random

#variables
days_week = 7
calories_per_pound_fat = 3500
kg_to_lb = 2.204622
bmi_goal = 21.5
print("Good day to you!")
time.sleep(1)
name = input("What's your name? ")
time.sleep(1)
age = input("How old you are you? ")
time.sleep(1)
def age_response():
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

# determine weight to gain or lose to achieve and communicate the user's BMI
Optimal_weight_calc = round(abs(21.5 - BMI_calc) * 2.20462) 
if BMI_calc < 18.5: 
    print(name , ", your BMI is ", BMI_calc, ", you are underweight. However, you are well on your way to achieving a healthy weight!", "Gaining ", Optimal_weight_calc, " more pounds will put you at your optimal weight. Keep working hard my friend.")
if  BMI_calc >=18.5 and BMI_calc <= 24.9: 
    print("Nice job! " , name , ", Your BMI is ", BMI_calc,".", "You are at a healthy weight and size.")
if BMI_calc >= 25 and BMI_calc < 30: 
    print(name , ", your BMI is ", BMI_calc, ", you are overweight. However, you are well on your way to achieving a healthy weight!", "Losing ", Optimal_weight_calc, " more pounds will put you at your optimal weight. Keep working hard my friend.")
if BMI_calc >= 30: 
    print(name , ", your BMI is ", BMI_calc, ", you are overweight. However, you are well on your way to achieving a healthy weight!", "Losing ", Optimal_weight_calc, " more pounds will put you at your optimal weight. Keep working hard my friend.")
time.sleep(1)

# give the user a choice to move on to further data collection using a "yes" or "no" function
print("Would you like to know how long it will take you to lose ", Optimal_weight_calc, " pounds following a basic gym routing?" )
phase_2_answer = input(" Yes or No  ")
if phase_2_answer == "Yes" or "yes" or "Yes" or "yEs":
    ##choose a random gym activity from the Harvard list and take the cal/pound ratio and compute the time it takes to loose the weight required to achieve optimal BMI.  
    gym_activities_dict = {'Weight Lifting: general': 0.72, 'Aerobics: water': 0.96, 'Stretching, Hatha Yoga': 0.96, 'Calisthenics: moderate': 1.08, 'Riders: general': 1.2, 'Aerobics: low impact': 1.32, 'Stair Step Machine: general': 1.44, 'Teaching aerobics': 1.44, 'Weight Lifting: vigorous': 1.44, 'Aerobics, Step: low impact': 1.68, 'Aerobics: high impact': 1.68, 'Bicycling, Stationary: moderate': 1.68, 'Rowing, Stationary: moderate': 1.68, 'Calisthenics: vigorous': 1.92, 'Circuit Training: general': 1.92, 'Rowing, Stationary: vigorous': 2.04, 'Elliptical Trainer: general': 2.16, 'Ski Machine: general': 2.28, 'Aerobics, Step: high impact': 2.4, 'Bicycling, Stationary: vigorous': 2.52}
    ##convert dict to list???
    entry_list = list(gym_activities_dict.items())
    ##choose a random wourkout from gym activities dict
    random_entry = (random.choice(entry_list))
    ##access the value of the random choice 
    random_entry_number = (random_entry[1])
   ##calculate the time required to loose weight (number of calories per pound of human fat * BMI attributable to weight) / (cal/pound ratio of exercise * user's weight))
    time_to_lose_weight = (calories_per_pound_fat * Optimal_weight_calc)/ (random_entry_number * weight_lbs) 
    print(time_to_lose_weight)
