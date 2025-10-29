import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("thermometer-diffs.csv",skipinitialspace=True)
print(data)
data["Difference"] = round(data["Dallas_Digital"] - data["LM35_Analogue"],2)
data["LM35_smooth"] = data["LM35_Analogue"].rolling(window=5).mean()
print(data)
print(data["Difference"].mean())
print(data["Difference"].median())
meanminus= pd.DataFrame(data["Dallas_Digital"]-data["Difference"].mean())
print(meanminus)

print("Correlation:", data["Dallas_Digital"].corr(data["LM35_smooth"]))

plt.plot(data["Difference"].rolling(window=3).mean())
plt.show()
