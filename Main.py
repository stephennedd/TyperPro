import random
import time

# Open file article.txt and seperate the sentences using ('.') as split.
# Then write a randomly chosen sentence into sentence.txt.
for i in range(1000):
    with open("article.txt", 'r') as f:
        sentences = f.read().split(".")
    with open("sentence.txt", 'w') as f:
        f.write(random.choice(sentences) + ".")
# Read the sentence that was written into sentences.txt and print it.
with open("sentence.txt", 'r') as q:
    sentence = q.read().strip()
    print(sentence)

# Create a time stamp of the time it printed the sentence.
start = time.time()

# Ask for user to input (retype) the sentence.
typedword = input("\033[1;34mPlease retype the above sentence: \033[0m")

# If user types sentence correctly..
# Take another timestamp of the time the print happened.
# Subtract the current time from the start time)
if typedword == sentence:
    now = time.time()
    end = round((now - start), 2)
    print("\033[1;32m\nThat's correct! \033[0m" + " You took " ,end,  " seconds!")

# If user types sentence wrongly..
else:
    now = time.time()
    end = round((now - start), 2)
    print("\033[1;31m\nThat's incorrect\033[0m" + " You took ", end , " seconds!")