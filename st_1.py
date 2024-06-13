import streamlit as st
import pandas as pd
import plotly.express as px
st.title("Top Profitable Cities and States--ft.Srinu")
import os
file_path = "SSStore3.xlsx"
if os.path.exists(file_path):
    df = pd.read_excel(file_path) if file_path.endswith('.xlsx') else pd.read_csv(file_path)
    st.write(df.head())
    if 'Profit' in df.columns:
        with st.sidebar:
            select = st.selectbox("Aggregate by", ["State", "City"])
            top_n = st.number_input("Top N", min_value=1, max_value=df[select].nunique(), value=10)
        summary_df = df.groupby(select)['Profit'].sum().nlargest(top_n).reset_index()
        st.write(f"Top {top_n} {select}s by Profit")
        st.write(summary_df)  
        fig_bar = px.bar(summary_df, x=select, y='Profit', title=f'Top {top_n} {select}s by Profit', width=1000, height=600)
        fig_pie = px.pie(summary_df, names=select, values='Profit', title=f'Top {top_n} {select}s by Profit', width=1000, height=600)
        st.plotly_chart(fig_bar)
        st.plotly_chart(fig_pie)
    else:
        st.write("The dataset does not contain a 'Profit' column.")

