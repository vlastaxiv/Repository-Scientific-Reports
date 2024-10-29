import matplotlib.pyplot as plt

# Data for fold change percentages
categories = ['T0', 'T2 vs T0', 'T6 vs T0', 'T24 vs T0', 'T48 vs T0', 'T72 vs T0']
btg3_s = [100, -121.66, 185.56, 571.88, 764.88, 1524.22]
cd69_s = [100, 377.67, 563.08, 1494.33, 1659.16, 2488.39]
cd83_s = [100, -116.82, 171.60, 285.38, 497.19, 602.70]
ermn_s = [100, 118.92, 162.34, 442.07, 186.92, 499.33]
jun_s = [100, 202.99, 807.43, 3181.04, 3301.93, 4362.68]
phf1_s = [100, 122.02, 118.49, 145.54, 145.93, 218.64]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(categories, btg3_s, label='BTG3 S', marker='o')
plt.plot(categories, cd69_s, label='CD69 S', marker='o')
plt.plot(categories, cd83_s, label='CD83 S', marker='o')
plt.plot(categories, ermn_s, label='ERMN S', marker='o')
plt.plot(categories, jun_s, label='JUN S', marker='o')
plt.plot(categories, phf1_s, label='PHF1 S', marker='o')

# Add labels and title
plt.xlabel('Comparison')
plt.ylabel('Expression Change (%)')
plt.title('Fold Change Percentage Comparison for Genes')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
