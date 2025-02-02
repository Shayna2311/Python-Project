#%%
#Chatbot (1)
FAQ ={}
FAQ = {"A" : "In order to proceed, please enter the name of the appliance of your choice. E.g Television, Fridge, Master Bedroom Air-Conditioning, etc",
       "B" : "You can find this information by looking at your appliance invoice/ labels on your appliance/searching online", 
       "C" : "E.g. If your fan has 5 speed settings, key in 20 for speed setting 1 and so on",
       "D" : "Please refer to your electricity bill"}
def faq():
    x= input("""[A] Appliance
[B] Amount of power consumed per hour
[C] Capacity
[D] Tariff rate
What do you need help with: """).upper()
    print(FAQ[x])
    
#Introduction (2)
user_name = input("Please enter your name:")

welcome_message = f"Hi {user_name}! Welcome to your personalised household electricity calculator! "
print(welcome_message)

print("""
      To compute your household electricity consumption, 
      you would have to provide details of your appliance capacity and usage. 
      Please fill up below accordingly.
     
      If you have any questions, stop the program and please enter: faq()""")

#Electricity consumption computation + Targets (3)
#Calculate total monthly electricity consumption & breakdown for each appliance

def calculate_appliance_energy(power, capacity):
    return power * capacity/100

def choice(msg):
     while True:
         try:
             user_input = input(msg)
             return user_input
         except ValueError:
             print("\nInvalid entry. Please enter either Y or N.")

def get_valid(msg):
    while True:
        try:
            user_input = float(input(msg))
            if user_input < 0:
                print("\nInvalid entry. Please enter only positive values.")
            return user_input
        except ValueError:
            print("\nPlease enter only numeric values!")

tariff_rate = get_valid("Tariff rate: ")

def energy_calculator():
     appliance = input("Enter appliance: ")
     
     
     appliance_power = get_valid("Enter amount of power consumed per hour (kWh): ")
         
         
     while True:
         capacity = get_valid(f"Enter the capacity {appliance} is operating at (%): ")
         if capacity < 0 or capacity > 100:
             print("\nInvalid entry.")
         else:
             break
     while True:
         capacity_goal = get_valid("Enter the targeted operating capacity (%): ")
         if capacity_goal < 0 or capacity_goal > 100:
             print("\nInvalid entry.")
         else:
             break
     
     while True:
         usage = get_valid(f"Enter the number of hours {appliance} is used per day: ")
         if usage < 0 or usage > 24:
             print("\nInvalid entry. Please provide your DAILY usage.")
         else:
             break
     while True:
         usage_goal = get_valid(f"Enter the number of hours you plan to use {appliance} per day: ")
         if usage_goal < 0 or usage_goal > 24:
             print("\nInvalid entry. Please provide your DAILY usage goal.")
         else:
            break
     
     while True:
         try:
             number = int(input(f"Enter the number of {appliance} at home: "))
             if number < 0:
                 print("\nInvalid entry. Please enter only positive values!")
             else:
                 break
         except ValueError:
             print("\nPlease enter only integer values!")
            
    #Savings/Spending (4&5)
    # Calculate daily energy consumption for appliance
     consumption = calculate_appliance_energy(appliance_power, capacity) * usage * number
   
    # Calculate daily energy consumption difference
     consumption_diff = calculate_appliance_energy(appliance_power, capacity_goal) * usage_goal * number
         
     appliance_monthly = consumption * 30
     print("\nThe current monthly electricity consumption for your", appliance, "is", round(appliance_monthly, 2), "kW.")
   
    # Check if user intend to use more or less
     if consumption_diff > consumption:
      extra_usage = (consumption_diff - consumption) * 30
      print("\nThe projected monthly energy consumption for", appliance, "will be", round(appliance_monthly + extra_usage, 2), "kWh and the average monthly electricity consumed is", round(extra_usage, 2), "kWh more than actual.")
      print("You would spend about S$", round(extra_usage * tariff_rate, 2), "more per month.")
   
     else:
      usage_diff = (consumption - consumption_diff) * 30
      print("\nThe projected monthly energy consumption for", appliance, "will be", round(appliance_monthly - usage_diff, 2), "kWh and the average monthly electricity saved is", round(usage_diff, 2), "kWh less than actual.")
      print("You would have saved about S$", round(usage_diff * tariff_rate, 2), "per month.") 

        
     return appliance_monthly

#Calculate monthly electricity bill (4&5)      
total_monthly = 0
total_monthly_goal = 0
while True:
    while True:
     add_appliance = choice("Add Appliance (Y/N): ").upper()
     if add_appliance not in "YN":
          print("\nInvalid entry. Please enter either Y or N.")
     else:
        break
    if add_appliance == "N":
        print("\nThe total monthly electricity consumption for your household is", round(total_monthly,2), "kW.")
        break    
    appliance_monthly = energy_calculator()
    total_monthly += appliance_monthly

monthly_electricity_bill = round(tariff_rate * total_monthly, 2)
print("\nYour monthly electricity bill is $", monthly_electricity_bill)

#Storing of monthly electricity bill (6)
#Save monthly electricity consumption and bill to a file for retrieval by user
from datetime import date
to_day = date.today()
datenow = to_day.strftime("%m/%y")

filename = "monthly_electricity consumption.txt"
with open(filename,"a") as file:
    electricity_consumption = "\nIn {}, your household electricity consumption and bill was {}kW and ${} respectively.".format(datenow, round(total_monthly, 2), monthly_electricity_bill)
    file.write(electricity_consumption)
    
while True:
  review = choice("Would you like to review your past monthly electricity consumption (Y/N): ").upper()
  if review not in "YN":
     print("\nInvalid entry. Please enter either Y or N.")
  elif review == "Y":
    with open(filename) as file:
        for each_line in file:
            print(each_line)
    break
  else:
      break

#Checking national usage with your own consumption (7)
#Comparison by housing type
options = ['A', 'B', 'C', 'D', 'E', 'F']

while True:
    household_type = input(f"""A: 1 or 2 room flat
B: 3 room flat
C: 4 room flat
D: 5 room flat / Executive
E: Condo
F: Landed
\n{user_name}, please enter the alphabet corresponding to your household type: """).upper()
    if household_type in options: 
        break
    else:
        print("\nPlease enter a valid household option.")

def print_consumption_message(consumption, household_type):
  # Dictionary for consumption limit
  consumption_limit = {
    "A": 170.2,
    "B": 274.2,
    "C": 375.5,
    "D": 456,
    "E": 538.7,
    "F": 1209.1
  }

  reminder_msg = "\nYou are consuming more electricity than average. You should try to conserve more electricity by lowering your daily usage or lower your appliance's usage capacity!"

  encourage_msg = "\nGood job! You are consuming less electricity than the national average! Please continue conserving your daily electricity usage!"
  
  if consumption >= consumption_limit[household_type]:
    print (reminder_msg)
  else:
    print (encourage_msg)

# Print message
print_consumption_message(total_monthly, household_type)

#%%
#Game to increase awareness on environmentally-friendly practices (8)
while True:
 play = choice("Would you like to play a game? (Y/N): ").upper()
 if play not in "YN":
    print("\nInvalid entry. Please enter either Y or N.")
 else:
    break  
score = 0
total_questions = 8 
if play == "N":
    print("See you next time! Goodbye!")
else:
    print()
    print("Welcome to the energy consumption quiz!".center(90, "="))
    answer = input("""What is the recommended temperature for air-conditioners?
(a) 22
(b) 24
(c) 25
(d) 26
Ans: """).lower()
    if answer == "c":
        score += 1
        print("Congratulations! You are right!")
    else:
        print("Wrong answer. The correct answer is (c) 25.")
    answer = input("""How much can one save per year by increasing the air-conditioner temperature by one degree celsius?
(a) $5
(b) $15
(c) $100
Ans: """).lower()
    if answer == "b":
        score += 1
        print("That's right!")
    else:
        print("Good try. But that's not the right answer. The correct answer is (b) $15.")
    answer = input("""What is the estimated annual cost savings of using an air-conditioner with 4 ticks instead of 1 tick?
(a) $350
(b) $450
(c) $550
(d) $650
Ans: """).lower()
    if answer == "b":
        score += 1
        print("You are absolutely right!")
    else:
        print("Incorrect. The correct answer is (b) $450.")
    answer = input("""What are some ways to reduce the electricity consumption of your refrigerator?
(a) Allow hot food to cool before storing it in the refrigerator
(b) Ensure that the refrigerator door shuts tightly
(c) Not overloading the refrigerator
(d) All of the above
Ans: """).lower()
    if answer == "d":
       score += 1
       print("""Yes! 
Test by closing the door over a piece of paper so it is half in and half out of the refrigerator. If you can pull the paper out easily, the hinge may need adjustment or the seal may need replacing.
Also,too many food items may block air circulation. Consider using containers to minimise clutter.
Lastly, try to decide what to take beforehand so you don't leave the door open longer than necessary.""")
    else:
        print("""Wrong answer. It should be (d) All of the above. 
              Test by closing the door over a piece of paper so it is half in and half out of the refrigerator. If you can pull the paper out easily, the hinge may need adjustment or the seal may need replacing.
              Also, too many food items may block air circulation. Consider using containers to minimise clutter.
              Lastly, try to decide what to take beforehand so you don't leave the door open longer than necessary.""")
    
    answer = input("""How should we reduce our household electricity consumption?
(a) Use the fan instead of the aircon
(b) Allow natural daylight into the house instead of switching on the lights during the day 
(c) Service your air conditioner 
(d) Everything above
Ans: """).lower()
    if answer == "d":
        score += 1
        print("Congratulations! You are right! Please do include the above actions in your day to day life to conserve electricity")
    else: 
        print("Wrong answer, the correct answer shd be (d)everything above. Please try to include the above actions in your day to day life to conserve electricity")
    
    
    
    answer = input("""Which of the following is more energy efficient?
(a) Laptop
(b) Desktop
Ans: """).lower()
    if answer == "a": 
        score += 1
        print("Congratulations! You are right! Do try to use a laptop instead of desktop since it is more energy efficient")
    else: 
        print("Wrong answer, the correct answer should be (a)laptop. Do try to use a laptop instead of desktop since it is more energy efficient ")
     
        
     
    answer == input("""Which of the following is not a good practice when cooking?
(a) Leaving electric hotplates on until the food is fully cooked
(b) Cover pots when cooking
(c) Thaw frozen food before cooking
Ans: """).lower()
    if answer == "a": 
        score += 1
        print("Congratulations! You are right! To conserve electricity, you need not leave electric hotplates on till the food is fully cooked!")
    else: 
        print("Wrong answer. The correct answer should be (a)leaving electric hotplates on until the food is fully cooked. remember that you need not leave electric hotplates on till the food is fully cooked")
    
    
    
    answer = input("""Which of the following are energy efficient?
(a) Using hot water for your washing machine
(b) Using room temperature water for your washing machine
(c) Using fabric conditioner to reduce creasses to reduce ironing time
(d) Options a & c
(e) Options b & c
Ans: """).lower()
    if answer == "e":
        score += 1
        print("Congratulations! You are right! Using room temperature water for your washing machine is sufficient, and using fabric conditioner reducing creases is a good way to minimise ironing time")
    else: 
        print("Wrong answer, the correct answer should be (e)options b & c. Using room temperature water for your washing machine is sufficient, and using fabric conditioner reducing creases is a good way to minimise ironing time ")
        
    print(f"Your score is: {score}. Thank you for playing! Goodbye!") 
    
