import os 
import random

cd = os.getcwd()
cd
os.listdir()
x = os.listdir('Universe')
random.shuffle(x)
itemstep = 25
for item in x[:itemstep]:
    print(item)
