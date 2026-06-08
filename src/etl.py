
import pandas as pd
df=pd.read_csv('data/ventas.csv')
resumen=df.groupby(['producto'],as_index=False)['ventas'].sum()
resumen.to_csv('data/dw_ventas.csv',index=False)
print('DW generado')
