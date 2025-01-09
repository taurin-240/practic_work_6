import os
import pandas as pd

file_path = 'data/CAvideos.csv'
df = pd.read_csv(file_path)

# Общий объем памяти, который занимает DataFrame
total_memory = df.memory_usage(deep=True).sum()
print(f"Размер файла при загрузке в память: {total_memory / (1024 * 1024):.2f} МБ")
# Размер файла на диске
file_size = os.path.getsize(file_path)
print(f"Размер файла на диске: {file_size / (1024 * 1024):.2f} МБ")