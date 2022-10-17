import numpy as np

fibo_list=[0,1]

for i in range(10) :
    if i >= 2 :
        fibo = fibo_list[i-1] + fibo_list[i-2]
        fibo_list.append(fibo) 
