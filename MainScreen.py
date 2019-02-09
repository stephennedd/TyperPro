import random
import time


a = "In the morning."
b = "Encouraging me."
c = "Brothers and sisters."

Sentences = [a, b, c]

random.shuffle(Sentences)

print(Sentences[0])

start = time.time()


typedword = input("\033[1;34mPlease retype the above sentence: \033[0m")

if typedword == Sentences[0]:
    now = time.time()
    end = round((now - start), 2)
    print("\033[1;32mThat's correct! \033[0m" + " You took " ,end,  " seconds!")

else:
    now = time.time()
    end = round((now - start), 2)
    print("\033[1;31mThat's incorrect\033[0m" + " You took ", end , " seconds!")







