import scipy.stats as stats
import numpy as np

# If using Windows, use pre-compiled wheel package to install scipy. See https://scipy.org/install.html#windows-packages
# Will also need "numpy+mkl" pre-compiled package in this case

# skew and kurtosis of normal distribution are ~0
x = np.random.normal(0, 1, 1_000_000)
print(stats.skew(x))
print(stats.kurtosis(x))
