import numpy as np
import matplotlib.pyplot as plt
import random as rand

# np.set_printoptions(threshold=np.inf)

# Using dice rolls
n =10000
choices = [0,1,2,3]
weights = [0.5333,0.2667,0.1333,0.0667]
def dice_roll():
	dice = np.array(rand.choices(choices, weights,k=n))         
	return dice
X = dice_roll()
values, sim_count = np.unique(X, return_counts=True)
pmf_sum_sim = np.array(sim_count)/n
print("value =",values,"\n","probability =",pmf_sum_sim,"\nTheoretical =",weights)

