import pandas as pd
import os

data = pd.read_table('data.sas', usecols=['Velocity', 'LanePos', 'SpeedLimit', 'Steer', 'Accel', 'Brake', 'LongAccel', 'HeadwayTime', 'HeadwayDist'])
local_path = "DataSets/"
# print(data)

file_length = len(data)

offset = file_length // 5

# iteration on data sets and splitting the file

if file_length % offset == 0:
    chuncks_length = range(int(file_length/offset))
else:
    chuncks_length = range(int(file_length/offset)+1)

for i in chuncks_length:
    df = data[i*offset: (i+1)*offset]
    df.to_csv(os.path.join(local_path, 'splittedfile_chunk_{}'.format(i)))



