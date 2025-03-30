
import os


Message = "I complete python code from bro code"
file_path = "C:/Users/sscpg/Desktop/test.txt"

file_dir = "C:/Users/sscpg/Desktop"


# with open(file=file_path,mode= "w") as file:
#     file.writelines(Message)
#     print("Message is written")

try:
    with open(file=file_path,mode= "r") as file:
        file.readlines()
        print(file)
except FileExistsError:
    print( "That file already exists")