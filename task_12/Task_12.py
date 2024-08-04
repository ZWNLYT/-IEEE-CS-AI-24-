import pandas as pd

url = "C:\Users\MICROSOFT\Downloads\New folder\your_file.csv"
df = pd.read_csv(url)
df['date'] = pd.to_datetime(df['date'])

df.set_index('date', inplace=True)

grouped_data = df.resample('M')['sales'].mean()
print("Mean of 'sales' by year and month:")
print(grouped_data)

grouped_data = df.resample('Q')['sales'].sum()
print("\nSum of 'sales' by quarter:")
print(grouped_data)

grouped_data = df.resample('Y').count()
print("\nCount of rows by year:")
print(grouped_data)

grouped_data = df.resample('M')['sales'].std()
print("\nStandard deviation of 'sales' by month:")
print(grouped_data)

grouped_data = df.groupby(df.index.dayofweek)['sales'].mean()
print("\nMean of 'sales' by day of the week:")
print(grouped_data)

grouped_data = df.groupby(df.index.hour)['sales'].sum()
print("\nSum of 'sales' by hour of the day:")
print(grouped_data)