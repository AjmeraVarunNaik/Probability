import numpy as np

# Probability of winning in a single lottery
p_winning_single_lottery = 1/100

# Number of lotteries
num_lotteries = 50

# a) Probability of winning at least once
p_not_winning_single_lottery = 1 - p_winning_single_lottery
p_not_winning_all_lotteries = np.power(p_not_winning_single_lottery, num_lotteries)
p_winning_at_least_once = 1 - p_not_winning_all_lotteries

# b) Probability of winning exactly once
p_winning_exactly_once = p_winning_single_lottery * np.power(p_not_winning_single_lottery, num_lotteries - 1) * num_lotteries

# c) Probability of winning at least twice
p_winning_at_least_twice = np.sum([np.power(p_winning_single_lottery, 2) * np.power(p_not_winning_single_lottery, num_lotteries - 2) * num_lotteries for _ in range(num_lotteries - 1)])

print("Probability of winning at least once:", p_winning_at_least_once)
print("Probability of winning exactly once:", p_winning_exactly_once)
print("Probability of winning at least twice:", p_winning_at_least_twice)
