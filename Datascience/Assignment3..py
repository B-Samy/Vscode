import random
from fractions import Fraction
from itertools import product
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# num_tossess = 10000

# toss = [random.choice(['H','T']) for _ in range(num_tossess)]
# numheads = toss.count('H')
# numtial = toss.count('T')

# print(Fraction(numheads,num_tossess))
# print(Fraction(numtial,num_tossess))





#  b. Rolling two dice and computing the probability of getting a sum of 7.  


# dice_outcomes = list(product(range(1,7), repeat=2))

# dice_thrown = [pair for pair in dice_outcomes if sum(pair) == 7]
# print(dice_thrown)



# Write a function to estimate the probability of getting at least one "6" in 10 rolls of a fair die.  



# def estimate(numtrials):
#     successfultrials = 0
    
#     for _ in range(numtrials):
#         rolls = [random.randint(1, 6) for _ in range(10)]
        
#         if 6 in rolls:
#             successfultrials += 1
    
#     probability = successfultrials / numtrials
    
#     return probability

# numtrials = 10000  
# probability = estimate(numtrials)
# print(f"Estimated probability of getting at least one 6 in 10 rolls: {probability}")




# values = [1, 2, 3]
# probabilities = [0.25, 0.35, 0.4]

# sample_size = 1000
# sample = np.random.choice(values, size=sample_size, p=probabilities)

# emp_mean = np.mean(sample)
# emp_variance = np.var(sample)
# emp_std_dev = np.std(sample)

# print(f"Empirical Mean: {emp_mean}")
# print(f"Empirical Variance: {emp_variance}")
# print(f"Empirical Standard Deviation: {emp_std_dev}")




# mean = 5
# sample_size = 2000
# samples = np.random.exponential(scale=mean, size=sample_size)

# plt.figure(figsize=(10, 6))

# plt.hist(samples, bins=30, density=True, alpha=0.6, color='g', label='Histogram')

# xmin, xmax = plt.xlim()
# x = np.linspace(xmin, xmax, 100)
# pdf = (1 / mean) * np.exp(-x / mean)
# plt.plot(x, pdf, 'r-', lw=2, label='PDF (Exponential)')

# plt.title('Exponential Distribution: Histogram and PDF Overlay')
# plt.xlabel('Value')
# plt.ylabel('Density')
# plt.legend()

# plt.show()





# uniform_data = np.random.uniform(0, 1, 10000)

# sample_size = 30
# num_samples = 1000
# sample_means = [np.mean(np.random.choice(uniform_data, sample_size)) for _ in range(num_samples)]

# plt.figure(figsize=(12, 6))

# plt.subplot(1, 2, 1)
# plt.hist(uniform_data, bins=30, color='skyblue', edgecolor='black')
# plt.title('Uniform Distribution')
# plt.xlabel('Value')
# plt.ylabel('Frequency')

# plt.subplot(1, 2, 2)
# plt.hist(sample_means, bins=30, color='salmon', edgecolor='black')
# plt.title('Distribution of Sample Means')
# plt.xlabel('Sample Mean')
# plt.ylabel('Frequency')

# plt.tight_layout()
# plt.show()







