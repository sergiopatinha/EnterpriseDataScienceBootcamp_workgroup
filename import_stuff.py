import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.model_selection import train_test_split
import openpyxl

print("✅ Todas as bibliotecas foram importadas com sucesso!\n")

# Teste pandas + numpy
df = pd.DataFrame({
    "x": np.arange(1, 6),
    "y": np.random.randint(10, 100, 5)
})
print("Pandas DataFrame de teste:\n", df, "\n")

# Teste matplotlib
plt.plot(df["x"], df["y"], marker="o")
plt.title("Teste Matplotlib")
plt.show()

# Teste seaborn
sns.scatterplot(data=df, x="x", y="y")
plt.title("Teste Seaborn")
plt.show()

# Teste plotly
fig = px.line(df, x="x", y="y", title="Teste Plotly")
fig.show()

print("Se viste gráficos do matplotlib, seaborn e plotly -> tudo OK ✅")
