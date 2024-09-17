# your code goes here!
import time

def countdown(count):
    while count:
        print(f'{count} SECOND(S)!') 
        count -= 1

    print('HAPPY NEW YEAR!')

def countdown_with_sleep(count):
    while count:
        print(f'{count} SECOND(S)!')
        count -= 1
        time.sleep(1)
    print('HAPPY NEW YEAR!')