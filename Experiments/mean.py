import pandas as pd
import numpy as np

# Load data
data = pd.read_csv("signals.csv", sep=r"\s+", header=None)

# Overall mean of all signals and all time samples
overall_mean = data.values.mean()

print(overall_mean)