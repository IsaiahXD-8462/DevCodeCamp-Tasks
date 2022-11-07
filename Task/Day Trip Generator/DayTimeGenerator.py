
commitment_1 = "Going to SuperBowl"
commitment_2 = "Meeting with Family"
commitment_3 = "Trying plenty of Foods"
number_of_days = 21
budget = 5000.50

destination_list = ["french quarter", "riverwalk", "convention center", "superdome", "bourbon street"]
restaurant_list = ["drago", "acme", "cafe du monde", "french press", "gambinos", "transcontinental"]
mode_of_transportation_list = ["vehicle", "plane", "ferry", "trolley", "train"]
entertainment_list = ["second line dancing", "comic con", "seafood boil party", "ferry ride", "casino playing", "watching superbowl"]
import random

itenerary_list = [destination_list, restaurant_list, mode_of_transportation_list, entertainment_list]

print(random.choice(itenerary_list))
print(random.choice(destination_list))
print(random.choice(restaurant_list))
print(random.choice(mode_of_transportation_list))
print(random.choice(entertainment_list))

ideal_destination = "convention center"
ideal_restaurant = "drago"
ideal_mode_of_transportation = "plane"
ideal_entertainment = "comic con"

will_not_do = True

while will_not_do == True:
    if random.choice(destination_list) == ideal_destination:
        will_not_do = False
        print("Destination Decided!")
    else:
        print("Decide Again.")   
        print(random.choice(destination_list)) 

will_not_do = True

while will_not_do == True:
    if random.choice(restaurant_list) == ideal_restaurant:
        will_not_do = False
        print("Restaurant Decided!")
    else:
        print("Decide Again.")   
        print(random.choice(restaurant_list)) 

will_not_do = True       

while will_not_do == True:
    if random.choice(mode_of_transportation_list) == ideal_mode_of_transportation:
        will_not_do = False
        print("Mode of Tranportation Decided!")
    else:
        print("Decide Again.")
        print(random.choice(mode_of_transportation_list)) 

will_not_do = True          

while will_not_do == True:
    if random.choice(entertainment_list) == ideal_entertainment:
        will_not_do = False
        print("Entertainment Decided!")
    else:
        print("Decide Again.")
        print(random.choice(entertainment_list))



completed_list = [ideal_destination, ideal_restaurant, ideal_mode_of_transportation, ideal_entertainment]   
print(f"Enjoy your destination to {completed_list[0]} and eating in {completed_list[1]} by {completed_list[2]} then enjoy the {completed_list[3]}!")               