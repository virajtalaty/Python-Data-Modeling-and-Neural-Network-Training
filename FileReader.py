import pandas as pd
import os
import xlrd
import csv


#creating Sum function as the input contains string values also
def Sum_List(A,i,offset):
    value = 0
    for j in range(i*offset, i*offset + len(A)):
        if(A[j] != '-'):
            value = value + float(A[j])
    return value

dataLocation = "E:\\ASU USA\\Subjects\\CSE 564 Software Design\\Assignment\\data\\"
data = pd.read_table(dataLocation + 'mode1\Student1mode1\Student1mode1.2016-11-22_074716.datacol.sas',
                      usecols=['Velocity', 'LanePos', 'SpeedLimit', 'Steer', 'Accel', 'Brake', 'LongAccel', 'HeadwayTime', 'HeadwayDist'])
Vh_Output_Data = dataLocation + "Vh_Output_Data.xlsx" 
local_path = "E://ASU USA//Subjects//CSE 564 Software Design//Assignment//Answer//"

# print(data)

file_length = len(data)

offset = file_length // 5


# iteration on data sets and splitting the file
if file_length % offset == 0:
    chuncks_length = range(int(file_length/offset))
else:
    chuncks_length = range(int(file_length/offset)+1)


# creating the output csv
with open(local_path+'persons.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)    
        filewriter.writerow(["Velocity", 'LanePos','SpeedLimit', 'Steer','Accel', 'Brake','LongAccel', 'HeadwayTime','HeadwayDist','User','Mode','Speed','Number Of Errors','Response Time','Number of Steps'])


#for i in chuncks_length:
for i in chuncks_length:

    
    #Fetching data from output file
    #Hardcoding taking first 6 lines from output VH fle
    Student_Id = 1;
    xls = pd.ExcelFile(Vh_Output_Data)
    df = xls.parse('Sheet1', skiprows=0, index_col=None, na_values=['NA'])
    Mode = df.loc[i][0]
    Speed = df.loc[i][1]
    NOE = df.loc[i][2]
    Response_Time = df.loc[i][3]
    No_Steps = df.loc[i][4]

    
    df = data[i*offset: (i+1)*offset]
    Velocity = Sum_List(df.Velocity,i,offset)/offset
    LanePos =  Sum_List(df.LanePos,i,offset)/offset
    SpeedLimit = Sum_List(df.SpeedLimit,i,offset)/offset
    Steer =  Sum_List(df.Steer,i,offset)/offset
    
    Accel = Sum_List(df.Accel,i,offset)/offset
    Brake =  Sum_List(df.Brake,i,offset)/offset
    LongAccel = Sum_List(df.LongAccel,i,offset)/offset
    HeadwayTime =  Sum_List(df.HeadwayTime,i,offset)/offset
    HeadwayDist =  Sum_List(df.HeadwayDist,i,offset)/offset

    with open(local_path+'persons.csv', 'a', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow([Velocity, LanePos,SpeedLimit, Steer,Accel, Brake,LongAccel, HeadwayTime,HeadwayDist,Student_Id,Mode,Speed,NOE,Response_Time,No_Steps])
