import time

def focus_timer(minutes):
    seconds = minutes * 60
    for i in range(seconds, 0, -1):
        print("{:02d}:{:02d}".format(*divmod(i, 60)))
        time.sleep(1)
    print("Time's up!")
