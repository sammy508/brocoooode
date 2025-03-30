
# Multithreading = Used to perfom multiple tasks concurrently (Multitasking)
     # Good for I/o bound task like reading files or fetching data from APIS threading. Thread(target = my_function)

import threading
import time

def walk_dog():
    time.sleep(10)
    print("its time for walk mr doggo ")

def tea_time(babe):
    time.sleep(4)
    print(f"Hei {babe} Lets grab a cup of tea ")

def get_email():
    time.sleep(6)
    print("Oh its time to check mail")

chore1 = threading.Thread(target=walk_dog)
chore1.start()
chore2 = threading.Thread(target=get_email)
chore2.start()
chore3 = threading.Thread(target=tea_time, args=("Beb",))  # yeha argument pass garne bela sadhai tuples ma pass garne otherwise error falxa
chore3.start()


# Here join method make main Thread to  waits until all the thread completes their task 
# It shynchronize the task of the thread
chore1.join()
chore2.join()
chore3.join()
