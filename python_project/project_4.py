# Python Countdown 
import time
# import os
my_time = int(input("Enter the time in seconds: "))
for i in reversed(range(0,my_time)):
    seconds = i % 60
    minutes =int( i / 60) % 60
    hours = int(i / 3600)
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
    time.sleep(1)   
    # os.system('clear') 

print("times up")