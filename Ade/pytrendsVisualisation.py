import pandas as pd
import matplotlib.pyplot as plt
from Ade.Technology import query_trends

df = query_trends(['machine learning'])
df2 = query_trends(['oracle'])

df.drop('isPartial', axis=1, inplace=True)
df2.drop('isPartial', axis=1, inplace=True)


fig, ax = plt.subplots(nrows=2)
df.plot(ax=ax[0])
df2.plot(ax=ax[1])
ax[0].set_title('Interest over Time for Machine Learning - 5 Year Period')
ax[1].set_title('Interest over Time for Oracle - 5 Year Period')
#plt.title('Interest over Time for Machine Learning - 5 Year Period')
ax[0].set_xlabel('Date')
ax[1].set_xlabel('Date')

ax[0].set_ylabel('Interest over Time')
ax[1].set_ylabel('Interest over Time')

fig.subplots_adjust(hspace=0.5)
plt.show()