import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

# Load Provo River Streamflow Data
csv_path = Path(__file__).with_name('June-2021-Provo-River-Streamflow-Rates (1).csv')
provo_df = pd.read_csv(csv_path)

# Map columns to specified variables
x_provo = provo_df['Site Number:'].to_numpy()
y_1_provo = provo_df['10163000'].to_numpy()
y_2_provo = provo_df['10155200'].to_numpy()
y_3_provo = provo_df['10155500'].to_numpy()
y_4_provo = provo_df['10154200'].to_numpy()
y_5_provo = provo_df['10155000'].to_numpy()

print("Provo River Streamflow Data loaded and sliced.")

"""### Graphing the Data

Plot x, y_1, y_2, y_3, y_4, and y_5 with the elements shown in the instructions in the code block below.
"""

plt.figure(figsize=(12, 6))
plt.plot(x_provo, y_1_provo, label='Site 10163000')
plt.plot(x_provo, y_2_provo, label='Site 10155200')
plt.plot(x_provo, y_3_provo, label='Site 10155500')
plt.plot(x_provo, y_4_provo, label='Site 10154200')
plt.plot(x_provo, y_5_provo, label='Site 10155000')

plt.title('June 2021 Provo River Streamflow Rates')
plt.xlabel('Date & Time')
plt.ylabel('Streamflow Rate')
plt.xticks(x_provo[::96], rotation=45) # label daily
plt.grid(True, linestyle='--')
plt.legend()
plt.tight_layout()
plt.show()

