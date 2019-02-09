import random
import time

RED = '\033[91m'
BLUE = '\033[94m'
GREEN = '\033[92m'

a = "In the morning."
b = "Encouraging me."
c = "Brothers and sisters."

list1 = [a, b, c]

random.shuffle(list1)

print(list1[0])

start = time.time()


typedword = input("Please retype the above sentence: ")

if typedword == list1[0]:
    now = time.time()
    end = round((now - start), 2)
    print("\033[1;32mThat's correct! \033[0m" + " You took " ,end,  " seconds!")

else:
    now = time.time()
    end = round((now - start), 2)
    print("\033[1;31mThat's incorrect\033[0m" + " You took ", end , " seconds!")







