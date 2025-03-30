
# File detection

import os

file = "C:/Users/sscpg/Desktop/New Microsoft Word Document.docx"

file_dir = "C:/Users/sscpg/Desktop"





if os.path.exists(file):
    print(f"Yes {file} exist")

else:
    print("file not found")

if os.path.isdir(file_dir):
    print(f"That a directory")
else : 
    print("Its not a directory")
