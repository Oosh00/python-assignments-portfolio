#importing some libraries
import numpy as np
from scipy.special import gamma
import statistics
import math
 #imported from greg
def t_distribution_pdf(x, nu):


    coeff = gamma((nu + 1) / 2) / (np.sqrt(nu * np.pi) * gamma(nu / 2))
    density = coeff * (1 + x**2 / nu) ** (-0.5 * (nu + 1))
    return density

def find_t_star(prob, nu, x_start=0, x_end=20, num_points=10000):

   

      #imported from greg
    x = np.linspace(x_start, x_end, num_points)
    y = t_distribution_pdf(x, nu)
    cdf = np.cumsum(y) * (x[1] - x[0])
    target_half_prob = prob / 2
    index = np.where(cdf >= target_half_prob)[0][0]
    return x[index]
       
       
    
 #putting list into python
scorelist = [92.64,79.00,84.79,97.41,93.68,65.23,84.50,73.49,73.97,79.11]
           
       #getting the number of items in the list
n = len(scorelist)
       #summing
a = sum(scorelist)
       #this is the mean
mean = a/n
       #this is standard deviation
s = statistics.stdev(scorelist)
       #this is degrees of freedom
v = n-1
       
       #computing t0, using 75% as u0
to = ((mean-75)/((s)/(math.sqrt(n))))
       
       #adding in necessary values to the 'pseudocode' given
prob = 0.95
nu = v

t_star = find_t_star(prob, nu)
#checking if t0 is in the interval [-t*, t*]. if it isn't, then u doesn't equal 75.
if to <= t_star:
    print ("False")
elif to >= -1*t_star:
    print ("False")
else:
    print ("True")
    
    
    