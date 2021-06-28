import time

start_time = time.time()
print(f"module was imported at {start_time}")

def start():
    global start_time
    start_time = time.time()

def finish():
    return time.time() - start_time

if __name__ == "__main__":
    start()
    print("test")
    print(finish())