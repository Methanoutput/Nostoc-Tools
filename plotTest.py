import matplotlib.pyplot as plt

# Data from the user
organisms = ['Nostoc Azolla', 'Nostocales', 'Cyanos', 'Bacis', 'Alle']
counts = [695659, 1414815, 3768194, 6281796, 6296783]
relative_counts = [695659, 719156, 2353379, 2513602, 14987]

# Creating a bar chart
plt.figure(figsize=(10, 6))
# Plotting the original counts in blue
plt.bar(organisms, counts, color='skyblue', label='Total Counts')
# Plotting the relative counts in red
plt.bar(organisms, relative_counts, color='lightcoral', label='Relative Counts')

plt.xlabel('Organism')
plt.ylabel('Count of Reads')
plt.title('Read Counts for Different Organisms')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()  # Adding a legend to distinguish between the two sets of bars

# Show the plot
plt.show()