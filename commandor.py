import os
import sys
import modules.creater as crt
import modules.deleter as dlt
import modules.place as place
import modules.time_info as time
import modules.operating as OS
import modules.weather as wth
import modules.ip_adress as ip
import modules.modules as modules

def index():
    print()
    print("Hello")
    print()
    print("Write here your goal,senior")


    goal = str(input())


    print()


    if (goal == 'create file'):
        crt.create_file()

    if (goal == 'delete file'):
        dlt.delete_file()

    if (goal == 'create folder'):
        crt.create_folder()

    if (goal == 'delete folder'):
        dlt.delete_folder()

    """
    if(goal == 'get my place'):
        place.placer()

    if(goal == 'get weather'):
        wth.weather()
    """

    if(goal == 'get time'):
        time.time()

    if(goal == 'tell about operating system'):
        OS.operating_system()

    if(goal == 'get my ip'):
        ip.getIP()

    if(goal == 'number of skills commandor'):
        modules.number_skills()

    if(goal == 'get skills'):
        modules.skills()

    if (goal != 'stop'):
        index()
    print()



if __name__ == "__main__":
    index()


