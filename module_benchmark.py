import time


def start_time():
    return time.time()


def end_time(start):
    end = time.time()
    total_time = end - start
    print("\n"+ str(total_time) + "secondes.")
