import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\Users\DELL\Desktop\ProdigyInfotech_DataScience\1\archive\world_population.csv"

df = pd.read_csv(file_path)

print(df.head())

plt.figure(figsize=(12, 8))

country_populations = df.groupby('Country/Territory')['2022 Population'].sum().sort_values(ascending=False)

country_populations.head(20).plot(kind='bar', color='skyblue')

plt.title('Top 20 Countries/Territories by Population in 2022')
plt.xlabel('Country/Territory')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
