import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('quarterly_data.csv')

# Calculate the average metric
average_metric = data['Metric'].mean()
print(f"Average Metric: {average_metric}")

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(data['Quarter'], data['Metric'], marker='o', linestyle='-', label='Quarterly Metric')
plt.axhline(y=8, color='r', linestyle='--', label='Target (8)')
plt.axhline(y=average_metric, color='g', linestyle='--', label=f'Average ({average_metric:.2f})')

# Add labels and title
plt.title('Quarterly Metric Trend Analysis')
plt.xlabel('Quarter')
plt.ylabel('Metric')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the plot
plt.savefig('trend.png')

print("Plot saved as trend.png")
