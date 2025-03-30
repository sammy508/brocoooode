
import json

file_path = "C:/Users/sscpg/Desktop/testfile.json"

try:
    with open(file_path,'r') as file:
        content = json.load(file)
        print(content)
except FileExistsError:
    print("File not found")