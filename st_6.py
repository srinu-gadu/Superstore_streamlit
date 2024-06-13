import streamlit as st
import pandas as pd
import plotly.express as px
st.write("## Sales and Profits Analysis by each of Category and Sub-Category--ft.Srinu")
df = pd.read_excel("SSStore3.xlsx")
st.write("Data Preview:")
st.write(df.head())
select = st.selectbox("Select level to analyze", ['Category', 'Sub-Category'])
select2 = st.selectbox("Select column for analysis", ['Sales', 'Profit'])
level = 'Category' if select == 'Category' else 'Sub-Category'
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
summary_df = df.groupby(level)[select2].sum().reset_index()
st.write(f"Analysis by {select}:")
st.write(summary_df)
if select == 'Category':
    fig = px.pie(summary_df, names=level, values=select2, title=f'{select2} by {select}')
else:
    fig = px.bar(summary_df, x=level, y=select2, title=f'{select2} by {select}')
st.plotly_chart(fig)

