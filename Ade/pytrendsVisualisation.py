import pandas as pd
import matplotlib.pyplot as plt
from Ade.Technology import query_trends

df = query_trends(['machine learning'])
print(df)

df.drop('isPartial', axis=1, inplace=True)
df.plot()
plt.title('Interest over Time for Machine Learning - 5 Year Period')
plt.xlabel('Date')
plt.ylabel('Interest over Time')
plt.show()