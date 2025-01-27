import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Gráficos\\clases.csv")
sns.lineplot(x="fecha",y="pedos",data=df)

#creando un punto en el momento de mas clases
plt.plot("01-09",17,"o")
plt.show()