import time
x = int(input("Please enter number: "))
for i in range(x + 1):
    print(x)
    x = x - 1 
    time.sleep(1)