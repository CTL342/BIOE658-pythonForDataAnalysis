# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 09:18:35 2025

@author: Bahaa
"""

import numpy as np
import pandas as pd

# ---------------------------------------
# 1. Generate synthetic wearable data
# ---------------------------------------
np.random.seed(42)
N = 1000  # number of samples

# Wearable sensor features
heart_rate = np.random.normal(80, 10, N)        # bpm
skin_temp  = np.random.normal(33, 1.2, N)       # °C
gsr        = np.random.normal(0.7, 0.15, N)     # stress (a.u.)
steps      = np.random.normal(5000, 1200, N)    # steps during measurement window

# Physiological model for glucose (synthetic)
# Blood glucose depends on physiology (synthetic model)
y = (
    0.4 * heart_rate
    - 1.5 * skin_temp
    + 20 * gsr
    - 0.001 * steps
    + np.random.normal(0, 1, N)
    + 110   # measurement noise
)

# Enforce physiologically realistic minimum glucose level
glucose = y

# ---------------------------------------
# 2. Create DataFrame
# ---------------------------------------
df = pd.DataFrame({
    "HeartRate": heart_rate,
    "SkinTemp": skin_temp,
    "GSR": gsr,
    "Steps": steps,
    "Glucose": glucose
})

# ---------------------------------------
# 3. Save to CSV
# ---------------------------------------
df.to_csv("wearable_glucose_dataset.csv", index=False)

print("Dataset saved as wearable_glucose_dataset.csv")
