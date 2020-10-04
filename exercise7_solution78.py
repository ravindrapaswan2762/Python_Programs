# HEALTHY PROGRAMMER SOLUTION
# 9AM - 5AM
# WATER - water.mp3 (3.5 liters) - drank - log - every 40 min
# EYES - eyes.mp3 - every 30 min - eyedone - log - every 30 min
# PHYSICAL ACTIVITY - physical.mp3 - every 45 min- exdone - log
# RULES
# pygame module to play audio
"""
from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

if __name__ == '__main__':
    musiconloop("water.mp3", "stop")

    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 5
    exsecs = 10
    eyesecs = 20

    while True:
        if time() - init_water > watersecs:
            print("water drinking time, enter 'drank' to stop the alarm ! ")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            log_now("drank water at")

        if time() - init_eyes > eyesecs:
            print("Eye exercise time, enter 'eyedone' to stop the alarm ! ")
            musiconloop('eyes.mp3', 'eyedone')
            init_eyes = time()
            log_now("Eyes relaxed  at")

        if time() - init_exercise > exsecs:
            print("Physical activity time, enter 'exdone' to stop the alarm ! ")
            musiconloop('physical.mp3', 'exdone')
            init_exercise = time()
            log_now("Physical activity done at")"""



from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    musiconloop("sound.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 5
    exsecs = 10
    eyessecs = 15

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes >eyessecs:
            print("Eye exercise time. Enter 'doneeyes' to stop the alarm.")
            musiconloop('eyes.mp3', 'doneeyes')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical Activity Time. Enter 'donephy' to stop the alarm.")
            musiconloop('physical.mp3', 'donephy')
            init_exercise = time()
            log_now("Physical Activity done at")