import winsound
import time
import os

# Coding the sound of alarm of clock
def sound():
    for i in range(2):  # Number of repeats

        for j in range(9):  # Number of beeps

            winsound.MessageBeep(-1)  # Sound played

        time.sleep(2)  # How long between beeps


def alarm(n):
    print(f"Wait time {n} seconds.")
    time.sleep(n)  # Waits n seconds before alarm
    sound()


def input_destination(user_input):

    if user_input == 1:
        wait_time = (int(input("Enter the desired hours: ")) * 60) * 60
        alarm(wait_time)
    elif user_input == 2:
        wait_time = (int(input("Enter the desired Minutes: ")) * 60)
        alarm(wait_time)
    elif user_input == 3:
        wait_time = int(input("Enter the desired Seconds: "))
        alarm(wait_time)
    elif user_input == 4:
        hours = int(input("Hours: "))
        minutes = int(input("Minutes: "))
        seconds = int(input("Seconds: "))
        wait_time = ((hours*60)*60) + minutes*60 + seconds
        print(wait_time)
        alarm(wait_time)
    else:
        os.system('cls')
        main()


def main():
    # This runs the main code
    print("What is the unit of time do you want to wait?\n (1)Hours (2)Minutes (3)Seconds (4)Combination")
    main_input = int(input(": "))

    input_destination(main_input)


if __name__ == "__main__":
    main()
