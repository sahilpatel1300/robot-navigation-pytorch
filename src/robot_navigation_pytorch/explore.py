import pandas as pd

columns = [
    "front",
    "left",
    "right",
    "back",
    "action"
]

df = pd.read_csv(
    "data/sensor_readings_4.data",
    header = None,
    names=columns)

#print(df.head())
#print(df.shape)
#print(df.info())
print(df.loc[0:5, ["front"]])

front_sensor_avg = df["front"].mean()
print(front_sensor_avg)

action_counts = df["action"].value_counts()
print(action_counts)

# find lows less than 1 
low_values = df[df["front"] < 1]

move_forward_avg = df[df["action"] == "Move-Forward"]["front"].mean()
print(move_forward_avg)

# figure out which of the 4 sensors has the highest avg
sensors = ["front", "left", "right", "back"]
avg_values = {sensor: df[sensor].mean() for sensor in sensors}
highest_avg_sensor = max(avg_values, key=avg_values.get)

sensor_means = df[sensors].mean()
highest_avg_sensor = sensor_means.idxmax()