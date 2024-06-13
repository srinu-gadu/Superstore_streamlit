import streamlit as st
import pandas as pd
import plotly.express as px
import os
st.title("Ship Mode analysis: Profit,Quantity,Sales --ft.Srinu")
file_path = "SSStore3.xlsx"
if os.path.exists(file_path):
    df = pd.read_excel(file_path)
    st.write("Data Preview:")
    st.write(df.head())
    if 'Ship Mode' in df.columns:
        select = st.selectbox("Select column for analysis", ['Profit', 'Quantity', 'Discount', 'Sales'])
        results = []
        for mode, mode_df in df.groupby('Ship Mode'):
            mode_df['Sales'] = pd.to_numeric(mode_df['Sales'].replace('[^\d.]', '', regex=True))
            mode_value = mode_df[select].sum() if select in ['Profit', 'Discount', 'Sales'] else mode_df[select].count()
            results.append({'Ship Mode': mode, select: mode_value})
        results_df = pd.DataFrame(results)
        st.write("Analysis Results:")
        st.write(results_df)
        fig3 = px.pie(results_df, names='Ship Mode', values=select, title=f'{select} Distribution by Ship Mode')
        st.plotly_chart(fig3)
        
        fig1 = px.bar(results_df, x='Ship Mode', y=select, title=f'{select} by Ship Mode')
        st.plotly_chart(fig1)
        
        fig2 = px.line(results_df, x='Ship Mode', y=select, title=f'{select} by Ship Mode', markers=True)
        st.plotly_chart(fig2)

        fig4 = px.scatter(results_df, x='Ship Mode', y=select, title=f'{select} by Ship Mode')
        st.plotly_chart(fig4)
#to get only the plot you wish, remove the lines of code for other plots
    else:
        st.write("The dataset does not contain 'Ship Mode' column.")

