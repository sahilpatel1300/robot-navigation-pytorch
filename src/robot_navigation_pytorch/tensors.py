import torch

# a single robot observation 

sensor_readings = [1.2, 0.8, 2.1, 0.5]

x = torch.tensor(sensor_readings, dtype=torch.float32)

print(x)
print(x.shape)
print(x.ndim)
print(x.dtype)