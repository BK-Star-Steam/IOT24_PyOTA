from time import sleep

while True:
    with open("info.txt") as f:
        data = f.readlines()
        print("info.txt content:", data)
    sleep(3)
