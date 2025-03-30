


# RBITRAY ARGUMENTS 

#   *args = allows you to pass multiple non-key arguments
#   ** kwargs = allows you to pass multiple keywords -arguments

# 8 - unpacking operator


# def displa_name(*args):

#     for arg in args:
#         print(arg, end= " ")

# displa_name("Dr", "sammy", "Harlod", "Basantapur", " III")

# # kwargs

# def print_address( **kwargs):

#     for key, value in kwargs.items():
#         print(f"{key} : {value}")

# print_address (
#     street = '123 lakeside',
#     apt = '100',
#     city = 'pokhara',
#     state = 'Gandaki',
#     zip = '54321'
#     )


#  oth in same

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end= " ")

    
    for key, value in kwargs.items():
        print(f"{key} : {value}")
        # print(f"{kwargs.get('street')}{kwargs.get('city')}")


shipping_label(
    "Dr", "sammy", "Harlod", "Basantapur", " III" , # args

    street = '123 lakeside',  # kwargs
    apt = '100',
    city = 'pokhara',
    state = 'Gandaki',
    zip = '54321'
)