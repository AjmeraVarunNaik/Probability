import numpy as np

# Probability of winning in one specific lottery
p_win = 1/100

# Probability of not winning in one specific lottery
p_not_win = 1 - p_win

# Number of lotteries
num_lotteries = 50

# a) Probability of winning at least once
prob_at_least_once = 1 - np.power(p_not_win, num_lotteries)

# b) Probability of winning exactly once
prob_exactly_once = p_win * np.power(p_not_win, num_lotteries - 1) * num_lotteries

# c) Probability of winning at least twice
prob_not_win_twice = np.power(p_not_win, num_lotteries) + p_win * np.power(p_not_win, num_lotteries - 1) * num_lotteries
prob_at_least_twice = 1 - prob_not_win_twice

print("a) Probability of winning at least once:", prob_at_least_once)
print("b) Probability of winning exactly once:", prob_exactly_once)
print("c) Probability of winning at least twice:", prob_at_least_twice)

