import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60) #method takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder.
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r') # /r overwrites the output for each iteration.
        time.sleep(1)
        time_sec -= 1

    print("GO Engineers!")

t=int(input("Enter time in seconds:"))
countdown(t)