import numpy as np  
from scipy import stats  
import matplotlib.pyplot as plt

num_of_samples     = 15

call_time_same_sex = np.random.exponential(15,num_of_samples)   # mean value 15
call_time_diff_sex = np.random.exponential(10,num_of_samples)   # mean value 10
quality_internet   = np.random.normal(80, 20, num_of_samples)   # mean value 80, variance 20
time               = np.random.normal(3, 1, num_of_samples)     # mean value 3 , variance 1
if_new_friend      = np.random.randint(0,2,num_of_samples)      # generate a random list consisting of 0 and 1
credit             = np.random.normal(3, 1, num_of_samples)     # mean value 3 , variance 1
age_diff           = np.random.randint(0,15,num_of_samples)     # generate a randon list 
language_fluence   = np.random.normal(5, 3, num_of_samples)     # mean value 5 , variance 3

print call_time_same_sex[0]

with open("data.csv",'w') as f:
    for i in range(num_of_samples):
        line = ",".join( [str(call_time_same_sex[i]), str(call_time_diff_sex[i]), str(quality_internet[i]), str(time[i]),
                          str(if_new_friend[i]),      str(credit[i])            , str(age_diff[i]),         str(language_fluence[i])] )
        f.write(line + "\n")
f.close()

