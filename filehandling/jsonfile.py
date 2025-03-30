

import json
import os

file_path = "C:/Users/sscpg/Desktop/testfile.json"

 
data = {
    "name":"Sammy",
    "age":22,
    "study":"Bachelor",
    "hobby": "IT"
}


try:
    with open(file_path,'w') as file:
        json.dump(data, file, indent=4)
        print("Json file created on given path")

except FileExistsError :
    print("File exist already")