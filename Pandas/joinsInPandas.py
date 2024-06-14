import pandas as pd

userUsage = pd.read_csv('user_usage.csv')
print(userUsage)

userDevice = pd.read_csv('user_device.csv')
print(userDevice)

# Merge Function

mergeFiles = userUsage.merge(userDevice, on='use_id')
print(mergeFiles)

# outer Join

outerJoin = userUsage.merge(userDevice, on='use_id', how='outer')
print(outerJoin)

# Left Join

leftJoin = userUsage.merge(userDevice, on='use_id', how='left')
print(leftJoin)

# Right Join

rightJoin = userUsage.merge(userDevice, on='use_id', how='right')
print(rightJoin)

# concatenate DataFrame

concateData = pd.concat((userUsage, userDevice))
print(concateData)