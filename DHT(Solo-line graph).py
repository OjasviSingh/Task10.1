import pandas as pd
import matplotlib.pyplot as plt  

Real_Time_Data = pd.read_csv('temp_data dht  1.csv')

date_time_data = [
    "2023-09-11T15:50:09.673Z",
    "2023-09-11T15:50:10.678Z",
    "2023-09-11T15:50:11.668Z",
    "2023-09-11T15:50:12.668Z",
    "2023-09-11T15:50:13.673Z",
    "2023-09-11T15:50:14.673Z",
    "2023-09-11T15:50:15.673Z",
    "2023-09-11T15:50:16.673Z",
    "2023-09-11T15:50:17.673Z",	
    "2023-09-11T15:50:18.673Z",	
    "2023-09-11T15:50:19.673Z"
]

individual_date_times = [value.split('Z')[0] for value in date_time_data]

datetime_objects = pd.to_datetime(individual_date_times, format="%Y-%m-%dT%H:%M:%S.%f")

plt.figure(figsize=(10, 6))
plt.plot(Real_Time_Data['Timestamp'], Real_Time_Data['Temperature(celsius)'])
plt.xlabel('Timestamp')
plt.ylabel('Temperature(celsius)')
plt.title('Line Graph of Timestamp vs. Temperature')
plt.grid(True)  
plt.xticks(rotation=45)  
plt.show()






