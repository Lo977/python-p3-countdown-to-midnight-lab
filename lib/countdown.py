# your code goes here!
import time

def countdown(count_num):
    while count_num > 0:
        print(f'{count_num} SECOND(S)!')
        count_num -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(count_num):
    while count_num > 0:
        print(f'{count_num} SECOND(S)!')
        time.sleep(1)
        count_num -= 1
    print("HAPPY NEW YEAR!")