#outer loop
for i in range(10):
    #inner loop
    for j in range(10):
        print(0, end=" ")
    print()


# Lets get the time complexity
import time

startTime = time.time()

#outer loop
for i in range(100):
    #inner loop
    for j in range(100):
        print(0, end=" ")
    print()

print(round((time.time() - startTime),2))


