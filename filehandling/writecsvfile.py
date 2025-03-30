# comma seperated value

import csv

file_path = file_path = "C:/Users/sscpg/Desktop/bro code/filehandling/testfile.csv"
employee = [["name", "age", "job"],
            ["sammy", "22", "student"],
            ["ammy", "21", "it"],
            ["aarsh", "21", "medical"]
            ]

try:

    with open( file=file_path, mode='w' ) as file :
        writer = csv.writer(file)

        for row in employee:
            writer.writerow(row)

        print("Csv file is created at given loation")

except FileExistsError :
    print("file exist already")