import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file into a pandas DataFrame
df = pd.read_csv('cereal.csv')

# Extract relevant data
cereal_names = df['name']
fat = df['fat']
protein = df['protein']
sugar = df['sugars']

# Create positions for the bars
bar_width = 0.25
bar_positions_fat = np.arange(len(cereal_names))
bar_positions_protein = bar_positions_fat + bar_width
bar_positions_sugar = bar_positions_fat + 2 * bar_width

# Plot the bar graph
fig, ax = plt.subplots(figsize=(15, 8))

bar1 = ax.bar(bar_positions_fat, fat, width=bar_width, label='Fat', color='b')
bar2 = ax.bar(bar_positions_protein, protein, width=bar_width, label='Protein', color='r', alpha=0.5)
bar3 = ax.bar(bar_positions_sugar, sugar, width=bar_width, label='Sugar', color='g', alpha=0.5)

# Formatting the graph
ax.set_xlabel('Cereal Names')
ax.set_ylabel('Amount (g)')
ax.set_title('Comparison of Fat, Protein, and Sugar in Cereals')

# Rotate x-axis labels so it is more legible
ax.set_xticks(bar_positions_protein)
ax.set_xticklabels(cereal_names, rotation=45, ha='right', fontsize=8)

# Set y-axis scale
ax.set_ylim(-2, 16)

# Move the legend
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

# Present the bar graph
plt.tight_layout()
plt.show()
