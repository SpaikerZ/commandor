import os
import sys
import creater as crt
import deleter as dlt
import place as place
import time_info as time
import operating as OS
import weather as wth

def index():
    print()
    print("Hello,Egor")
    print()
    print()
    print("Write here your goal,senior")


    goal = str(input())


    print()
    print()


    if (goal == 'create file'):
        crt.create_file()

    if (goal == 'delete file'):
        dlt.delete_file()

    if (goal == 'create folder'):
        crt.create_folder()

    if (goal == 'delete folder'):
        dlt.delete_folder()

    if(goal == 'get my place'):
        place.placer()

    if(goal == 'get weather'):
        wth.weather()

    if(goal == 'get time'):
        time.time()

    if(goal == 'tell about operating system'):
        OS.operating_system()

    if (goal != 'stop'):
        index()



    print()
    print()


if __name__ == "__main__":
    index()


