
# Decorator = A function that extends the behaviour of another function w/o modifying the base function
            # pass the base function as the an argument to the decorator

def add_sprinkles(func):
    def wrapper():
        print("YOu add sprinkles ! : ")
        func()
    return wrapper

def add_Choco(func):
    def wrapper():
        print (f"Add chocho to list")
        func()  # calling to base function 
    return wrapper

@add_sprinkles   # it helps yo add all the function tp another method like def fet.cream  // extends
@add_Choco
def get_icecram():
    print("YOu got ice cream 🍦")



get_icecram()



# func is a reference to the original function being decorated (in this case, get_icecream).

# When you call func() inside the wrapper function, you're actually calling the original get_icecream function.

# Here's how it works step by step:

# When you decorate get_icecream with @add_sprinkles, it's equivalent to doing:
# get_icecream = add_sprinkles(get_icecream)

# The decorator returns the wrapper function

# When you later call get_icecream(), you're actually calling the wrapper function

# Inside wrapper, it first prints "You add sprinkles ! : "

# Then it calls the original function (via func()), which prints "You got ice cream 🍦"
