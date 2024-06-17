import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.title("Top Profitable Cities and States--ft.Srinu")

file_path = "SSStore3.xlsx"
if os.path.exists(file_path):
    df = pd.read_excel(file_path) if file_path.endswith('.xlsx') else pd.read_csv(file_path)
    st.write(df.head())
    
    if 'Profit' in df.columns:
        select = st.selectbox("Aggregate by", ["State","City"])
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

st.title("Ship Mode analysis: Profit,Quantity,Sales --ft.Srinu")
if 'Ship Mode' in df.columns:
    s2 = st.selectbox("select column for analysis", ['Profit', 'Quantity', 'Discount', 'Sales'])
    
    results = []
    for mode, mode_df in df.groupby('Ship Mode'):
        mode_df['Sales'] = pd.to_numeric(mode_df['Sales'].replace('[^\d.]', '', regex=True))
        mode_value = mode_df[s2].sum() if s2 in ['Profit', 'Discount', 'Sales'] else mode_df[s2].count()
        results.append({'Ship Mode': mode, s2: mode_value})
    
    results_df = pd.DataFrame(results)
    st.write("Analysis Results:")
    st.write(results_df)
    
    fig_pie = px.pie(results_df, names='Ship Mode', values=s2, title=f'{s2} Distribution by Ship Mode', width=1000, height=600)
    #fig_bar = px.bar(results_df, x='Ship Mode', y=s2, title=f'{s2} by Ship Mode', width=1000, height=600)
    #fig_line = px.line(results_df, x='Ship Mode', y=s2, title=f'{s2} by Ship Mode', markers=True, width=1000, height=600)
    #fig_scatter = px.scatter(results_df, x='Ship Mode', y=s2, title=f'{s2} by Ship Mode', width=1000, height=600)
    #these commented plots can be uncommented to ge a plot of choice/requirement
    st.plotly_chart(fig_pie)
    #st.plotly_chart(fig_bar)
    #st.plotly_chart(fig_line)
   #st.plotly_chart(fig_scatter)
else:
    st.write("The dataset does not contain 'Ship Mode' column.")

st.title("Profit over time (aggregatable) by few Columns --- ft. Srinu")
col1, col2 = st.columns([1, 4])

with col1:
    s3 = st.selectbox("select column to group by", ['Ship Mode', 'Segment', 'City', 'State', 'Region', 'Category', 'Sub-Category', 'Product Name'])

with col2:
    s32 = st.selectbox("select aggregation function", ["Sum", "Average", "Count", "Median", "Min", "Max", "Std Dev"])

aggregate = {
    "Sum": "sum",
    "Average": "mean",
    "Count": "count",
    "Median": "median",
    "Min": "min",
    "Max": "max",
    "Std Dev": "std"
}

s_df = df.groupby(s3)['Profit'].agg(aggregate[s32]).reset_index()
s_df = s_df.sort_values(by='Profit', ascending=False).head(10)

st.write(f"Top 10 {s32} of Profit per {s3}:")
st.write(s_df)

fig_bar = px.bar(s_df, x=s3, y='Profit', title=f'Top 10 {s32} of Profit per {s3}')
st.plotly_chart(fig_bar)

#these commented plots can be uncommented to ge a plot of choice/requirement same same
# fig_line = px.line(s_df, x=s3, y='Profit', title=f'Top 10 {s32} of Profit per {s3}', markers=True, width=1000, height=600)
# st.plotly_chart(fig_line)
# fig_pie = px.pie(s_df, names=s3, values='Profit', title=f'Top 10 {s32} of Profit per {s3}', width=1000, height=600)
# st.plotly_chart(fig_pie)

st.title("Discount analysis on Sales and Profit ---ft.SRINU")
s45 = st.selectbox("select column for analysis", ['Sales', 'Profit', 'Quantity'], index=0)
dat45 = df.groupby('Discount')[s45].sum().reset_index()
st.write("Total {} by Discount:".format(s45))
st.write(dat45)
fig_line = px.line(dat45, x='Discount', y=s45, title="Total {} by Discount".format(s45),markers=True, width=1000, height=600)
st.plotly_chart(fig_line)

#these commented plots can be uncommented to ge a plot of choice/requirements
# fig_bar = px.bar(dat45, x='Discount', y=s45, title="Total {} by Discount".format(s45), width=1000, height=600)
#st.plotly_chart(fig_bar)
# fig_pie = px.pie(dat45, values=s45, names='Discount', title="Total {} by Discount".format(s45), width=1000, height=600)
# st.plotly_chart(fig_pie)

st.title("Sales and Profits Analysis by each of Category and Sub-Category--ft.Srinu")
s6 = st.selectbox("select level to analyze", ['Category', 'Sub-Category'])
s62 = st.selectbox("select column for analysis", ['Sales', 'Profit'])
level = 'Category' if s6 == 'Category' else 'Sub-Category'
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
s_df2 = df.groupby(level)[s62].sum().reset_index()

st.write(f"Analysis by {s6}:")
st.write(s_df2)

if s6 == 'Category':
    fig = px.pie(s_df2, names=level, values=s62, title=f'{s62} by {s6}', width=1000, height=600)
else:
    fig = px.bar(s_df2, x=level, y=s62, title=f'{s62} by {s6}', width=1000, height=600)

st.plotly_chart(fig)

st.title("Sales, Profits or Quantity Analysis by Customer ID---ft.SRINU")
for col in ['Sales', 'Profit', 'Quantity']:
    df[col] = pd.to_numeric(df[col], errors='coerce')
top_n7 = st.number_input("select top N values", min_value=1, max_value=df["Customer ID"].nunique(), value=10, step=1)

summary_df = df.groupby('Customer ID')[s45].sum().reset_index().nlargest(top_n7, s45)
st.write(f"Top {top_n7} {s45} by Customer ID:")
st.write(summary_df)

fig_bar = px.bar(summary_df, x='Customer ID', y=s45, title=f"{s45} by Customer ID", width=1000, height=600)
st.plotly_chart(fig_bar)

#these commented plots can be uncommented to ge a plot of choice/requirements
# fig_pie = px.pie(summary_df, names='Customer ID', values=s45, title=f"{s45} by Customer ID", width=1000, height=600)
# st.plotly_chart(fig_pie)
# fig_line = px.line(summary_df, x='Customer ID', y=s45, title=f"{s45} by Customer ID", markers=True, width=1000, height=600)
# st.plotly_chart(fig_line)

st.title("Order Count by each of City and State---ft.SRINU")
s8 = st.selectbox("selct level to analyze", ['City', 'State'])
top_n8 = st.number_input("select top N values", min_value=1, max_value=df[s8].nunique(), value=10)

summary_df = df.groupby(s8).size().reset_index(name='Number of Orders')
t8_df = summary_df.nlargest(top_n8, 'Number of Orders')

st.write(f"Top {top_n8} {s8}s by Number of Orders:")
st.write(t8_df)

fig_bar = px.bar(t8_df, x=s8, y='Number of Orders', title=f'Number of Orders by {s8}', width=1000, height=600)
st.plotly_chart(fig_bar)
fig_line = px.line(t8_df, x=s8, y='Number of Orders', title=f"Number of Orders by {s8}", markers=True, width=1000, height=600)
st.plotly_chart(fig_line)

# these commented plots can be uncommented to ge a plot of choice/requirements
# fig_pie = px.pie(t8_df, names=s8, values='Number of Orders', title=f'Number of Orders by {s8}', width=1000, height=600)
# st.plotly_chart(fig_pie)

