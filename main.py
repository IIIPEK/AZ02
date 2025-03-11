from asyncio.streams import FlowControlMixin

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df =pd.read_csv("data.csv", index_col=0)
print(df.head())
print(df.describe())
Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math
lower_bound_math = Q1_math - 1.5 * IQR_math
upper_bound_math = Q3_math + 1.5 * IQR_math
std = df['Математика'].std()

print(f"1-ый квартиль: {Q1_math}")
print(f"3-ий квартиль: {Q3_math}")
print(f"Межквартильный размах: {IQR_math}")
print(f"Нижний предел: {lower_bound_math}")
print(f"Верхний предел: {upper_bound_math}")
print(f"Стандартное отклонение: {std}")

df_out = df[(df['Математика'] < lower_bound_math) & (df['Математика'] > upper_bound_math)]
print(f"Количество отсечённых значений: {df_out.shape[0]}")
if df_out.shape[0] > 0:
    df.drop(df_out.index, inplace=True)

df.boxplot()
plt.show()



