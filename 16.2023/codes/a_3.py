import numpy as np
from scipy.optimize import minimize

# Probability density function (PDF)
def pdf(x, alpha, lam):
    if x <= 0:
        return 0.0
    return alpha * lam * x**(alpha - 1) * np.exp(-lam * x**alpha)

# Calculate the CDF at a specific point
def calculate_cdf(x, alpha, lam):
    if x <= 0:
        return 0.0

    num_steps = 10000  # Number of steps for numerical integration
    step_size = x / num_steps

    cdf = 0.0
    for i in range(num_steps):
        xi = i * step_size
        pdf_value = pdf(xi, alpha, lam)
        cdf += pdf_value * step_size

    return cdf

# Objective function for optimization
def objective(params):
    alpha, lam = params
    median = calculate_cdf(1.0, alpha, lam)
    quantile = calculate_cdf(2.0, alpha, lam)
    error = abs(median - 0.5) + abs(quantile - 0.75)
    return error

# Initial guess
initial_guess = [1.0, np.log(2.0)]  # Corrected lambda value

# Perform optimization
result = minimize(objective, initial_guess, method='Nelder-Mead')

alpha = result.x[0]
lam = result.x[1]

print("Alpha (𝛼) =", alpha)
print("Lambda (𝜆) =", lam)


