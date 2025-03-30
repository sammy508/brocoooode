
#  Positional Arguments

# return statement used to end a function and send a result to the caller 
def create_name (first, last):

    first = first.capitalize()
    last = last.capitalize()
    return first+ " "+last

fullname = create_name("sammy","cpgn")
print(fullname)

