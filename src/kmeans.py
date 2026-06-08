
import pandas as pd
from sklearn.cluster import KMeans

df=pd.read_csv('data/ventas.csv')
X=df[['ventas']]
model=KMeans(n_clusters=3,n_init=10,random_state=42)
df['segmento']=model.fit_predict(X)
df.to_csv('data/clientes_segmentados.csv',index=False)
print('Segmentación lista')
