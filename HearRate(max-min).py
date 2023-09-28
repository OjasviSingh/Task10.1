import pandas as pd
import matplotlib.pyplot as plt

running_data = pd.read_csv('RUN.csv')  
sitting_data = pd.read_csv('SIT.csv')  

running_data['time'] = pd.to_datetime(running_data['time'])
sitting_data['time'] = pd.to_datetime(sitting_data['time'])

running_data['date'] = running_data['time'].dt.date
sitting_data['date'] = sitting_data['time'].dt.date

running_max_hr = running_data.groupby('date')['data values'].max()
running_min_hr = running_data.groupby('date')['data values'].min()

sitting_max_hr = sitting_data.groupby('date')['data values'].max()
sitting_min_hr = sitting_data.groupby('date')['data values'].min()

print("Running Data:")
print("Max Heart Rate per Day:")
print(running_max_hr)
print("\nMin Heart Rate per Day:")
print(running_min_hr)

print("\nSitting Data:")
print("Max Heart Rate per Day:")
print(sitting_max_hr)
print("\nMin Heart Rate per Day:")
print(sitting_min_hr)
