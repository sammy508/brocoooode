
# Iterables = An object / collection that can return its element one at a time
#               allowing it to be repeated over in a loop


my_dictionary ={
    "a":1,
    "b":2,
    "c":3,

}

# it shows the key of the dictionary which is iterable
for key in my_dictionary:
    print(key)

# But doesn't gives values , to make value iterable we have to use values method 

for values in my_dictionary.values():
    print( values)

# and to make both key and values we use item method

for key, values in my_dictionary.items():
    print( key ,values)
    
for key, values in my_dictionary.items():
    print( key ,values)



# # Membership operator 
# here we use operator like in , not in they are the membership operator
# they are used to test the values or data is there found or not 

 # EG
# for key, values in my_dictionary.items():
#     print( key ,values)


# List comprehension  =  A concise way to create lists in python compact
#           and easier to read than traditional loops 
#            [expression for value in iterable if condition]

fruits = ["apple","banana","mango","grape"]
fruits = [fruit.upper() for fruit in fruits]  # it return a capital on each fruit on fruits
print(fruits)

fruits = [fruit[0]for fruit in fruits]
print(fruits)


# List comprehension with conditions 

numbers = [-11, 10 ,-12,15,*20]
positiv_num = [num for num in numbers if num>=0]
            #  [return value for loop on list num element in numbers list and conditions]
print(f"Neg numbers {positiv_num}")

neg_num = [num for num in numbers if num<0]
print(f"Neg numbers {neg_num}")