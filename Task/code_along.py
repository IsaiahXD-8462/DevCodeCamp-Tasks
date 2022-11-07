my_money = 0
car_price = 50000
cannot_purchase = True
car_color = "cerulean"

while cannot_purchase == True:
    if my_money == car_price:
        cannot_purchase = False
        print("Wahoo! Got a new car!")
    else:
        print("Still too poor. Try again later.") 
        my_money += 10000  