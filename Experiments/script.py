import pandas as pd
import statsmodels.api as sm
import numpy as np

files = {
    "CleanWater.csv": 0,
    "12drops.csv": 12,
    "24drops.csv": 24
}

X_data = []
y_data = []

mean_table = []

for filename, drops in files.items():

    # Load CSV
    data = pd.read_csv(filename, sep=r"\s+", header=None)

    # Flatten all signals and all time samples
    values = data.values.flatten()

    # Store all samples for regression
    y_data.extend(values)
    X_data.extend([drops] * len(values))

    # Mean for display
    mean_table.append({
        "file": filename,
        "drops_water": drops,
        "mean_ir_received": np.mean(values)
    })


# Table of means
mean_df = pd.DataFrame(mean_table)

print("\nMean values:")
print(mean_df.to_string(index=False))


# Regression
X = pd.DataFrame({"drops_water": X_data})
y = pd.Series(y_data)

X = sm.add_constant(X)

model = sm.OLS(y, X).fit()


print("\nRegression:")
print(model.summary())


# Equation
b0 = model.params["const"]
b1 = model.params["drops_water"]

print("\nRegression equation:")
print(f"ir_received = {b0:.4f} + ({b1:.4f}) * drops_water")