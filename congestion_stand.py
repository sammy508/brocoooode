
# program that utilize sets 

menu = {
    "pizza":4.00,
    "pasta": 2.30,
    "noodles": 1.50,
    "fries": 3.00,
    "lemonades": 1.50,
    "cokes": 3.00,
}

cart = []
total = 0

# print(food_item, end="  ")



for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

     
while True:

    order = input("Enter items you wanted : ").lower()
    
    if order == "q":
        break
    elif menu.get(order) is not None :
        cart.append(order)
print(cart)

print('<<<<<<< Total Price >>>>>>>>>')

print()
for order in cart : 
    total += menu.get(order)
    print(order, end=" " )
    print()

print(f"\n Total price is : {total} ")