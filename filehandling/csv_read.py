
# to read csv file

import csv

file_path = file_path = "C:/Users/sscpg/Desktop/bro code/filehandling/testfile.csv"

try:
    with open(file_path, 'r') as file:
        content = csv.reader(file)
        for line in content:
         print(line)
except FileExistsError :
   print("file error")
   