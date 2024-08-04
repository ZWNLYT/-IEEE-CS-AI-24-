import pandas as pd

url = r"D:\demo\your_file.csv"
df = pd.read_csv(url)

print("Initial Data Types:")
print(df.dtypes)
df['column1'] = df['column1'].astype(str)

df['column2'] = pd.to_numeric(df['column2'], errors='coerce')

df['column3'] = pd.to_numeric(df['column3'], errors='coerce')

print("\nUpdated Data Types:")
print(df.dtypes)
print("\nMissing Values:")
print(df.isnull().sum())

df['column1'].fillna('Unknown', inplace=True)

df['column2'].fillna(df['column2'].mean(), inplace=True)
df['column3'].fillna(df['column3'].mean(), inplace=True)

print("\nMissing Values after filling:")
print(df.isnull().sum())