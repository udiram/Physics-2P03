import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# Generate some sample data
np.random.seed(0)
x = np.linspace(0, 10, 100)
y = 2 * x + np.random.normal(0, 2, 100)

# Fit a line of best fit to the data
fit = np.polyfit(x, y, 1)
fit_fn = np.poly1d(fit)

# Calculate the R^2 value
r2 = r2_score(y, fit_fn(x))

# Plot the data and the line of best fit
plt.scatter(x, y, label='Actual Data')
plt.plot(x, fit_fn(x), '--', label='Line of Best Fit')
plt.legend()
plt.title(f'R^2 = {r2:.2f}')
plt.show()

# Perform some other statistical analysis
print("Coefficients:", fit)
print("Mean Squared Error:", np.mean((fit_fn(x) - y) ** 2))
print("Explained Variance Score:", np.var(y) / np.var(fit_fn(x)))
