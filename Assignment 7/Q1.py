import numpy as np
import pandas as pd

part-I

roll_number = 102317124
np.random.seed(roll_number)

sales_data = np.random.randint(1000, 5001, size=(12, 4))

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Sports']

df = pd.DataFrame(sales_data, columns=categories, index=months)
df

part-II

print("First 5 rows:\n", df.head())
print("\nSummary statistics:\n", df.describe())

total_per_category = df.sum()
print("\nTotal Sales per Category:\n", total_per_category)

df['Total Sales'] = df.sum(axis=1)
print("\nTotal Sales per Month:\n", df['Total Sales'])

growth = df[categories].pct_change().mean()
print("\nAverage Sales Growth per Category:\n", growth)

df['Growth Rate'] = df['Total Sales'].pct_change() * 100

if roll_number % 2 == 0:
    # Roll number is even → apply 10% discount to Electronics
    df['Electronics'] = df['Electronics'] * 0.9  
else:
    df['Clothing'] = df['Clothing'] * 0.85

print("\nDataFrame after Discount:\n", df)

part-III

import matplotlib.pyplot as plt
import seaborn as sns

df[categories].plot(figsize=(10, 6), marker='o')
plt.title("Monthly Sales Trends (After Discount)")
plt.xlabel("Month")
plt.ylabel("Sales Units")
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df[categories])
plt.title("Sales Distribution by Category (After Discount)")
plt.ylabel("Sales Units")
plt.show()
