import streamlit as st
import pandas as pd
import plotly.express as px
st.title("Order Count by each of City and State---ft.SRINU")
df = pd.read_excel("SSStore3.xlsx")
st.write("Data Preview:")
st.write(df.head())
select = st.selectbox("Select level to analyze", ['City', 'State'])
top_n = st.number_input("Select top N values", min_value=1, max_value=df[select].nunique(), value=10)
summary_df = df.groupby(select).size().reset_index(name='Number of Orders')
top_summary_df = summary_df.nlargest(top_n, 'Number of Orders')
st.write(f"Top {top_n} {select}s by Number of Orders:")
st.write(top_summary_df)
fig_bar=px.bar(top_summary_df,x=select,y='Number of Orders',title=f'Number of Orders by {select}')
st.plotly_chart(fig_bar)
#fig_pie=px.pie(top_summary_df,names=select,values='Number of Orders',title=f'Number of Orders by {select}')
#st.plotly_chart(fig_pie)
#fig_line=px.line(top_summary_df,x=select,y='Number of Orders',title=f"Number of Orders by {select}",markers=True)
#st.plotly_chart(fig_line)


# for getting only the plot you wish, remove the comment hash from the plot and make other plots as comments
