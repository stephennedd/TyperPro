import random
import time

# The list of available variables for sentences, this can be made more random in the future.
# Maybe add a whole article and create a function that Gets() a random sentence.
a = "In the morning."
b = "Encouraging me."
c = "Brothers and sisters."

# Create's the list of sentences.
Sentences = [a, b, c]
# Randomize and print the list.
random.shuffle(Sentences)
print(Sentences[0])

# Create a time stamp of the time it printed the sentence.
start = time.time()

# Ask for user to input (retype) the sentence.
typedword = input("\033[1;34mPlease retype the above sentence: \033[0m")

# If user types sentence correctly..
# Take another timestamp of the time the print happened.
# Subtract the current time from the start time)
if typedword == Sentences[0]:
    now = time.time()
    end = round((now - start), 2)
    print("\033[1;32m\nThat's correct! \033[0m" + " You took " ,end,  " seconds!")

# If user types sentence wrongly..
else:
    now = time.time()
    end = round((now - start), 2)
    print("\033[1;31m\nThat's incorrect\033[0m" + " You took ", end , " seconds!")