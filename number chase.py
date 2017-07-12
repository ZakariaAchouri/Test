import random
import time


n = random.randint(-10000,10000)

x = True

m = random.randint(-10000,10000)
while x == True:
    if m == n:

        print("yay!")
        break

    else:
        if m < n:

            m = m + random.randint(0,100)

            n = n + random.randint(-100,100)

        if m > n:

            m = m - random.randint(0,100)

            n = n + random.randint(-100,100)
    time.sleep(0.0000000000000000001)
    print(n,"_-_-_-_",m)
    if n > 100000:

            n = n - random.randint(0,100)

    if n < -100000:

            n = n + random.randint(0,100)

