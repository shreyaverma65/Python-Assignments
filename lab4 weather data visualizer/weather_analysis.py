import pandas as pd

df = pd.read_csv("DailyDelhiClimateTrain.csv")
print(df.head())
import matplotlib.pyplot as plt

# -------------------------------
# STEP 4: Data Cleaning
# -------------------------------

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# If there are any NaNs, fill or drop them
df = df.dropna()  # safest option

# Display cleaned data info
print("\nCleaned Data Info:")
print(df.info())

# ----------------------------------------
# STEP 5: Statistical Analysis with NumPy
# ----------------------------------------

import numpy as np

print("\n--- Daily Statistics ---")
print("Mean Temperature:", np.mean(df['meantemp']))
print("Min Temperature:", np.min(df['meantemp']))
print("Max Temperature:", np.max(df['meantemp']))
print("Std Deviation:", np.std(df['meantemp']))

# Extract month and year
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

print("\n--- Monthly Temperature Statistics ---")
monthly_stats = df.groupby('month')['meantemp'].agg(['mean','min','max','std'])
print(monthly_stats)

print("\n--- Yearly Temperature Statistics ---")
yearly_stats = df.groupby('year')['meantemp'].agg(['mean','min','max','std'])
print(yearly_stats)

# ---------------------------------------
# STEP 6.1: Line Chart (Daily Temperature)
# ---------------------------------------

plt.figure(figsize=(10,5))
plt.plot(df['date'], df['meantemp'])
plt.xlabel("Date")
plt.ylabel("Mean Temperature")
plt.title("Daily Temperature Trend")
plt.tight_layout()
plt.savefig("daily_temperature_trend.png")
plt.show()


# ---------------------------------------
# STEP 6.2: Bar Chart (Monthly Avg Temp)
# ---------------------------------------

monthly_avg = df.groupby('month')['meantemp'].mean()

plt.figure(figsize=(8,5))
plt.bar(monthly_avg.index, monthly_avg.values)
plt.xlabel("Month")
plt.ylabel("Avg Temperature")
plt.title("Average Monthly Temperature")
plt.tight_layout()
plt.savefig("monthly_avg_temperature.png")
plt.show()

# ---------------------------------------
# STEP 6.3: Scatter Plot (Humidity vs Temp)
# ---------------------------------------

plt.figure(figsize=(7,5))
plt.scatter(df['meantemp'], df['humidity'])
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.title("Humidity vs Temperature")
plt.tight_layout()
plt.savefig("humidity_vs_temperature.png")
plt.show()

# ---------------------------------------
# STEP 6.4: Combined Plot (Subplots)
# ---------------------------------------

fig, ax = plt.subplots(1, 2, figsize=(12,5))

# Subplot 1 — Line graph
ax[0].plot(df['date'], df['meantemp'])
ax[0].set_title("Temperature Trend")
ax[0].set_xlabel("Date")
ax[0].set_ylabel("Temperature")

# Subplot 2 — Scatter graph
ax[1].scatter(df['meantemp'], df['humidity'])
ax[1].set_title("Temp vs Humidity")
ax[1].set_xlabel("Temperature")
ax[1].set_ylabel("Humidity")

plt.tight_layout()
plt.savefig("combined_plot.png")
plt.show()

# ---------------------------------------
# STEP 7: Export Cleaned Data to CSV
# ---------------------------------------

df.to_csv("cleaned_weather_data.csv", index=False)
print("\nCleaned data exported successfully!")
