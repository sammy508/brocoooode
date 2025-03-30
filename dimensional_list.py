

# fruit =["Apple", "banana","org"]
# veg =["bean", "cauli","cabbage"]
# meat = ["Mutton","chicken","buff"]

# groceries = [fruit ,veg ,meat]
# print(groceries)

# print(f"{groceries[0][1] }Here it prints the data of 1st 0 index horizontally and 1 index of 0 in vertical and ans is banana") 


# Numpad

num_pad = [
    (1,2,3),
    (4,5,6),
    (7,8,9),
    ( "*",0,"#")

]
print(num_pad )

for row in num_pad:
    for num in row :
        print(num, end= " ")
    print()