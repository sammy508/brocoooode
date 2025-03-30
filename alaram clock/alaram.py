

import time
import datetime
import pygame

def set_alarm(alara_time):
    print(f"Alaram set for {alara_time} : ")
    sound_file = "C:\\Users\\sscpg\\Desktop\\bro code\\alaram clock\\kanye_good_morning.mp3"
    is_running = True

    while is_running :
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        time.sleep(1)
        if current_time == alara_time :
            print("wakeup ! 😴")

       
            pygame.mixer.init()
            pygame.mixer_music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_running = False


    

if __name__ == "__main__":
    alara_time = input("enter time for alarm HH : MM : SS : ")
    set_alarm(alara_time)
   
