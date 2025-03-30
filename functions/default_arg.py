
# Default arguments = A default value for certain parameters
#  default id used when that argument is omitted make your functions more flexible,reduces
#  # of arguments 
# 1. positional 2. default  3. keywords,  4.arbitary


def net_price(list_price, discount,tax=0):
    return  list_price*(1-discount)*(1 + tax)

print(net_price(500, 0)) 
print(net_price(500,0.5))
print(net_price(500, 20, 0.13))

# output
# 500
# 250.0
# -10734.999999999998

# here in default functions it takes the
# default value of parameter but we can manipulate by passing positional arguments
# def net_price(list_price, discount,tax=0): when we have to put default arguments we have to pou positional arguments 1st then only default
