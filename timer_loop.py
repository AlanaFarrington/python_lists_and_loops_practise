# loop that runs for 1 mintue
# run loop for 100 iteractions
# prints "Hello World" every 5 seconds

import time

def time_printer(iterations):
    i = 0
    while i < iterations:
        print("Hello World!")
        i += 1
        time.sleep(0.1)
    if i == iterations:
        print(str(iterations) + " iterations complete")

time_printer(30)


