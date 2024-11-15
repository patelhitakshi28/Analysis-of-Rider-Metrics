import pandas as pd # type: ignore
import json

# Your CSV data as a string
csv_data = """device_id,ride_nr,rider_name,duration,distance,calories_burned,gender
101,1,John Doe,30,10.5,250,M
101,2,John Doe,45,15.2,370,M
102,3,Jane Smith,60,20.0,450,F
102,4,Jane Smith,35,12.5,290,F
103,5,Alice Johnson,50,18.3,420,F
103,6,Alice Johnson,55,19.5,430,F
104,7,John Doe,40,13.8,320,M
104,8,John Doe,65,22.0,490,M
105,9,Jane Smith,70,25.5,520,F
105,10,Jane Smith,80,28.0,600,F
"""

# Save the CSV data to a file
with open('data.csv', 'w') as file:
    file.write(csv_data)

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('data.csv')

# Calculate the required statistics for each driver
report = []

for rider_name, group in df.groupby('rider_name'):
    num_trips = int(group['ride_nr'].count())
    total_distance = float(group['distance'].sum())
    loggers_used = list(map(int, group['device_id'].unique().tolist()))
    total_duration = float(group['duration'].sum())
    total_calories_burned = float(group['calories_burned'].sum())
    avg_speed = total_distance / total_duration if total_duration > 0 else 0
    calories_per_km = total_calories_burned / total_distance if total_distance > 0 else 0
    gender = group['gender'].iloc[0]


    driver_report = {
        'name': rider_name,
        'number_of_trips': num_trips,
        'total_distance': total_distance,
        'loggers_used': loggers_used,
        'total_duration': total_duration,
        'calories_burned': total_calories_burned,
        'average_speed': avg_speed,
        'calories_per_km': calories_per_km,
        'gender': gender
    }
    
    report.append(driver_report)

# Save the report to a JSON file
with open('driver_report.json', 'w') as json_file:
    json.dump(report, json_file, indent=4)

# Display the JSON report
print(json.dumps(report, indent=4))
