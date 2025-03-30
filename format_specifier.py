
# format specifier = {value:flags} format a value based on what flags are insertged

# .(number)f = round to that many decimal places
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :+ = indicate +v
# :, = comma seperator





price1 = 3.1455
price2 = -3.1455
price3 = 13.1455

print(f"price 1 is {price1:>} ")
print(f"price 1 is {price2:>} ")
print(f"price 1 is {price3:>} ")
#output for {price1:<} it justified content to right
# price 1 is 3.1455 
# price 1 is -3.1455 
# price 1 is 13.1455 

# output for {price:>}

print(f"price 1 is {price3:.2f} ")
# output price 1 is 13.15 prints only to digits after decimal

