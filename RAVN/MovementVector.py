import pandas as pd
df = pd.read_csv('./OILT Output Frames/CurrentFrame1.csv', sep=',', header=None)
df.columns = ['X Cent', 'Y Cent',	'X Dist', 'Y Dist',	'Class']
print(df)
class_priority = [1,2,3,4,5]

print(df.values[1][4])
