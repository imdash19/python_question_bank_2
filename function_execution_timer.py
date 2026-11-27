# Write a decorator function named @timer that prints how many seconds a function takes to execute. Apply it to a function that simulates a heavy computation using time.sleep().

import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Execution time: {end - start:.2f} seconds")
    return wrapper

@timer
def heavy_computation():
    print("Heavy computation started...")
    time.sleep(3)
    print("Heavy computation completed.")

heavy_computation()
