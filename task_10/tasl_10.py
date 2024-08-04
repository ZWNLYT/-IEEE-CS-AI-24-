import pandas as pd

url = r"C:\demo\your_file.csv"
df = pd.read_csv(url)
print("Original DataFrame:")
print(df.head())
print("\nSelecting rows and columns:")
print(df.loc[:, ["Name", "Age"]].head())

print("\nSetting index to 'Name' column:")
df.set_index("Name", inplace=True)
print(df.head())

print("\nResetting index:")
df.reset_index(inplace=True)
print(df.head())

print("\nFiltering rows where Age > 30:")
print(df[df["Age"] > 30].head())

print("\nFiltering columns where data type is numeric:")
print(df.select_dtypes(include=[int, float]).head())

print("\nUpdating 'Age' column by adding 1:")
df["Age"] += 1
print(df.head())

print("\nAdding a new column 'Score' with default value 0:")
df["Score"] = 0
print(df.head())

print("\nRemoving 'Score' column:")
df.drop("Score", axis=1, inplace=True)
print(df.head())

print("\nSorting by 'Age' in ascending order:")
df.sort_values("Age", inplace=True)
print(df.head())

print("\nSorting by 'Age' in descending order:")
df.sort_values("Age", ascending=False, inplace=True)
print(df.head())