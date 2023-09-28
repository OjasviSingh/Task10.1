import pandas as pd
import matplotlib.pyplot as plt

heart_rate_data = pd.read_csv('SIT.csv')

threshold = 100

alert_time = []

for index, row in heart_rate_data.iterrows():
    time = row['time']
    heart_rate = row['data values']
    
    if heart_rate > threshold:
        alert_time.append(time)

plt.figure(figsize=(12, 6))
plt.plot(heart_rate_data['time'], heart_rate_data['data values'], label='Heart Rate', color='blue')

if alert_time:
    plt.scatter(alert_time, [threshold] * len(alert_time), color='red', marker='o', label='Alert (HR > 75)')

plt.xlabel('time')
plt.ylabel('Heart Rate')
plt.title('Heart Rate Data with Alerts (Threshold = 100)')
plt.legend()
plt.grid(True)
plt.show()

if alert_time:
    print("Heart rate exceeded 100 at the following time:")
    for time in alert_time:
        print(time)
else:
    print("No heart rate exceeded 100.")
