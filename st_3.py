import streamlit as st
import pandas as pd
import plotly.express as px
st.title("Profit over time (aggregatable) by few Columns --- ft. Srinu")
df = pd.read_excel("SSStore3.xlsx")
st.write("Data Preview:")
st.write(df.head())
col1, col2 = st.columns([1, 4])
with col1:
    select = st.selectbox("Select column to group by", ['Ship Mode', 'Segment', 'City', 'State', 'Region', 'Category', 'Sub-Category', 'Product Name'])
with col2:
    select2 = st.selectbox("Select aggregation function", ["Sum", "Average", "Count", "Median", "Min", "Max", "Std Dev"])
aggregate = {
    "Sum": "sum",
    "Average": "mean",
    "Count": "count",
    "Median": "median",
    "Min": "min",
    "Max": "max",
    "Std Dev": "std"
}
summary_df = df.groupby(select)['Profit'].agg(aggregate[select2]).reset_index()
summary_df = summary_df.sort_values(by='Profit', ascending=False)
top_n = 10
summary_df = summary_df.head(top_n)
st.write(f"Top {top_n} {select2} of Profit per {select}:")
st.write(summary_df)
fig_bar = px.bar(summary_df, x=select, y='Profit', title=f'Top {top_n} {select2} of Profit per {select}')
st.plotly_chart(fig_bar)

# remove comment hash '#' for the following lines to display required plots

# Create and display the line plot
# fig_line = px.line(summary_df, x=select, y='Profit', title=f'Top {top_n} {select2} of Profit per {select}', markers=True)
# st.plotly_chart(fig_line)

# Create and display the pie chart
# fig_pie = px.pie(summary_df, names=select, values='Profit', title=f'Top {top_n} {select2} of Profit per {select}')
# st.plotly_chart(fig_pie)

