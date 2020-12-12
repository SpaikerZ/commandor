import os
import sys
import creater as crt
import deleter as dlt

print("egor")
def index():
    print()
    print("Hello,Egor")
    print()
    print()
    print("Write here your goal,senior")


    goal = str(input())


    print()
    if (goal == 'create file'):
        crt.create_file()

    if (goal == 'delete file'):
        dlt.delete_file()

    if (goal != 'stop'):
        index()

if __name__ == "__main__":
    index()


