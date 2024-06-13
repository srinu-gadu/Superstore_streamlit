import streamlit as st
import pandas as pd
import plotly.express as px
st.title("Sales, Profits or Quantity Analysis by Customer ID---ft.SRINU")
df=pd.read_excel("SSStore3.xlsx")
for col in ['Sales', 'Profit', 'Quantity']:
    df[col] = pd.to_numeric(df[col], errors='coerce')
select = st.selectbox("Select column for analysis", ['Sales', 'Profit', 'Quantity'])
top_n = st.number_input("Select top N values", min_value=1, max_value=df[select].nunique(), value=5, step=1)
summary_df = df.groupby('Customer ID')[select].sum().reset_index().nlargest(top_n, select)
st.write(f"Top {top_n} {select} by Customer ID:")
st.write(summary_df)
fig_bar= px.bar(summary_df, x='Customer ID', y=select, title=f"{select} by Customer ID")
st.plotly_chart(fig_bar)
#fig_pie= px.pie(summary_df, names='Customer ID', values=select, title=f"{select} by Customer ID")
#st.plotly_chart(fig_pie)
#fig_line= px.line(summary_df, x='Customer ID', y=select,title=f"{select} by Customer ID", markers=True)
#st.plotly_chart(fig_line)


# for getting only the plot you wish, remove the comment hash from the plot and make other plots as comments
