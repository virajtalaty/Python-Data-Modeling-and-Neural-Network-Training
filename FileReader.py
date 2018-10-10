import pandas

df = pandas.read_excel('sample.xls')
# print the column names
print
df.columns
# get the values for a given column
values = df['Arm_id'].values
# get a data frame with selected columns
FORMAT = ['Arm_id', 'DSPName', 'Pincode']
df_selected = df[FORMAT]
