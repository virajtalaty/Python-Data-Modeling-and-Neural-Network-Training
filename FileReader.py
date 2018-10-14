import pandas as pd
import os
import math as m

data = pd.read_table('data.sas', usecols=['Velocity', 'LanePos', 'SpeedLimit', 'Steer', 'Accel', 'Brake', 'LongAccel', 'HeadwayTime', 'HeadwayDist'])
local_path = "DataSets/"
# print(data)

file_length = len(data)

offset = file_length // 5

# iteration on data sets and splitting the file

chuncks_length = range(m.ceil(file_length/offset))

for i in chuncks_length:
    df = data[i*offset: (i+1)*offset]
    df.to_csv(os.path.join(local_path, 'splittedfile_chunk_{}'.format(i)))



