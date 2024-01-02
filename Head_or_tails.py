print("Welcome to the game of Heads and Tails")
import random
random_side=random.randint(0,1)
#if random_side==1, It will be printed as heads
#if random_side==2, it will be printed as tails
if random_side==0:
    print("Heads")
else:
    print("Tails")