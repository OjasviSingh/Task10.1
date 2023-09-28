import pandas as pd

running_data = pd.read_csv('RUN.csv')
sitting_data = pd.read_csv('SIT.csv')

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(running_data['time'], running_data['data values'], label='Running')
plt.xlabel('Time')
plt.ylabel('Heart Rate')
plt.title('Heart Rate During Running')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(sitting_data['time'], sitting_data['data values'], label='Sitting')
plt.xlabel('Time')
plt.ylabel('Heart Rate')
plt.title('Heart Rate While Sitting')
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))
plt.boxplot([running_data['data values'], sitting_data['data values']], labels=['Running', 'Sitting'])
plt.xlabel('Scenario')
plt.ylabel('Heart Rate')
plt.title('Heart Rate Comparison (Box Plot)')
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(running_data['data values'], bins=20, alpha=0.5, label='Running')
plt.hist(sitting_data['data values'], bins=20, alpha=0.5, label='Sitting')
plt.xlabel('Heart Rate')
plt.ylabel('Frequency')
plt.title('Heart Rate Comparison (Histogram)')
plt.legend()
plt.show()

