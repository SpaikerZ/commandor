import os
import sys
import creater as crt
import deleter as dlt


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

    if (goal != 'stop'):
        index()



    print()
    print()


if __name__ == "__main__":
    index()


