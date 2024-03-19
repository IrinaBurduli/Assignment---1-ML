import pandas as pd
import numpy as np
import subprocess
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


# Set random seed for reproducibility
np.random.seed(0)

# Generate random data for each feature
network_traffic_anomalies = np.random.randint(0, 100, size=200)
connection_rates = np.random.uniform(0, 10, size=200)
unauthorized_access_events = np.random.randint(0, 50, size=200)
packet_payload_data = np.random.randint(0, 1000, size=200)

# Create DataFrame
df = pd.DataFrame({
    'Network Traffic Anomalies': network_traffic_anomalies,
    'Connection Rates': connection_rates,
    'Unauthorized Access Events': unauthorized_access_events,
    'Packet Payload Data': packet_payload_data
})

# Save DataFrame to CSV without column names
df.to_csv('network_data.csv', index=False, header=False)

print(df)

# Define the package you want to install
package_name = "reportlab"

# Use subprocess to run the pip install command
subprocess.call(["pip", "install", package_name])


# Read the network data from the CSV file with feature names indicated
df = pd.read_csv('network_data.csv', header=None)

# Define feature names
feature_names = ['Network Traffic Anomalies', 'Connection Rates', 'Unauthorized Access Events', 'Packet payload data']

# Set column names
df.columns = feature_names

# Calculate the correlation matrix using Pearson correlation coefficient
correlation_matrix = df.corr(method='pearson')

# Save the correlation matrix to a CSV file
correlation_matrix.to_csv('correlation_matrix.csv')

# Plot the correlation matrix as a heatmap
plt.figure(figsize=(8, 6))
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='nearest')
plt.title('Correlation Matrix')
plt.colorbar()
plt.xticks(range(len(feature_names)), feature_names, rotation=45)
plt.yticks(range(len(feature_names)), feature_names)
plt.tight_layout()

# Save the correlation matrix plot to a PDF file
plt.savefig('correlation_matrix.pdf')
plt.close()

# Find the features with the highest correlation
max_corr = correlation_matrix.unstack().sort_values(ascending=False)
highest_corr = max_corr[max_corr < 1].head(2)

# Save the names of features with the highest correlation to a text file
with open('highest_correlation.txt', 'w') as f:
    f.write(highest_corr.to_string())

# Create a PDF file for the names of features with the highest correlation
c = canvas.Canvas('highest_correlation.pdf', pagesize=letter)
text = f'Names of features with the highest correlation:\n\n{highest_corr.to_string()}'
c.drawString(50, 750, text)
c.save()

print('process ended sucessfully')