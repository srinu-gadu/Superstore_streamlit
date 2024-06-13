import streamlit as st
import pandas as pd
import plotly.express as px
st.title("Discount analysis on Sales and Profit ---ft.SRINU")
df = pd.read_excel("SSStore3.xlsx")
select = st.selectbox("Select column for analysis", ['Sales', 'Profit', 'Quantity'], index=0)
data1 = df.groupby('Discount')[select].sum().reset_index()
st.write("Total {} by Discount:".format(select))
st.write(data1)
fig_bar = px.bar(data1, x='Discount', y=select, title="Total {} by Discount".format(select))
st.plotly_chart(fig_bar)
#fig_line = px.line(data1, x='Discount', y=select, title="Total {} by Discount".format(select))
#st.plotly_chart(fig_line)
#fig_pie= px.pie(data1, values=select, names='Discount', title="Total {} by Discount".format(select))
#st.plotly_chart(fig_pie)

# for getting only the plot you wish, remove the comment hash from the plot and make other plots as comments
