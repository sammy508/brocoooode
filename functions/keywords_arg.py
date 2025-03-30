

# keyword_arg = an argument preceeded by an identifier helps with readablity order of an arguments doesnt matter 

print("Heres the example of keywords aerguments")

def get_phone(country, area, first, last):
    return (f"{country}-{area}-{first}-{last}")

phone_num = get_phone(country=+977, area= 984, first= 2000,last= 10)

print(phone_num)