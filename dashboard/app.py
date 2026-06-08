
import streamlit as st
import pandas as pd
import plotly.express as px

st.title('SecureVision Analytics')

df=pd.read_csv('data/ventas.csv')

st.metric('Ventas Totales', f"${df['ventas'].sum():,.0f}")
st.metric('Clientes', df['cliente'].nunique())

fig=px.bar(df.groupby('producto',as_index=False)['ventas'].sum(),
           x='producto',y='ventas',title='Ventas por producto')
st.plotly_chart(fig,use_container_width=True)

st.dataframe(df.head(50))
