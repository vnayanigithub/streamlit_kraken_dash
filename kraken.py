import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")


# Load data
# Assuming the scraped data is saved in a CSV file named "kraken_games.csv"
df = pd.read_csv("Kraken_Games_2023.csv")

# Sidebar
st.sidebar.header('Filters')

# Opponent Filter
unique_opponents = ['All Opponents'] + df['Opponent'].unique().tolist()
selected_opponent = st.sidebar.selectbox('Opponent', unique_opponents, index=0)

# Home/Away Filter
location_options = ['Home', 'Away', 'All']
selected_location = st.sidebar.selectbox('Home/Away', location_options, index=2)

# Outcomes Filter
outcome_options = ['W', 'L', 'All']
selected_outcome = st.sidebar.selectbox('Outcomes', outcome_options, index=2)

# Overtime Filter
overtime_options = ['OT', 'SO', 'REG', 'All']
selected_overtime = st.sidebar.selectbox('Overtime', overtime_options, index=3)

# Filter dataframe based on selections
if selected_opponent != 'All Opponents':
    df = df[df['Opponent'] == selected_opponent]
if selected_location != 'All':
    df = df[df['Location'] == selected_location]
if selected_outcome != 'All':
    df = df[df['Outcome'] == selected_outcome]
if selected_overtime != 'All':
    df = df[df['Overtime'] == selected_overtime]

# Reset index and drop old one
df.reset_index(drop=True, inplace=True)

# KPIs
st.header('Seattle Kraken 2022-2023 Season')

# Create columns for KPI layout
kpi1, kpi2, kpi3 = st.columns(3)

# kpi 1
number1 = df[df['Outcome'] == 'W'].shape[0]
kpi1.markdown(f"<div style='padding:20px; border: 1px solid #99D9D9; border-radius: 10px; text-align: center;'>"
              f"<h2 style='font-size: 30px;'>Wins</h2>"
              f"<h1 style='font-size: 60px; color: #99D9D9;'>{number1}</h1>"
              f"</div>", unsafe_allow_html=True)

# kpi 2
number2 = df[df['Outcome'] == 'L'].shape[0]
kpi2.markdown(f"<div style='padding:20px; border: 1px solid #99D9D9; border-radius: 10px; text-align: center;'>"
              f"<h2 style='font-size: 30px;'>Losses</h2>"
              f"<h1 style='font-size: 60px; color: #99D9D9;'>{number2}</h1>"
              f"</div>", unsafe_allow_html=True)

# kpi 3
number3 = number1 / (number1 + number2) if (number1 + number2) != 0 else 0
kpi3.markdown(f"<div style='padding:20px; border: 1px solid #99D9D9; border-radius: 10px; text-align: center;'>"
              f"<h2 style='font-size: 30px;'>Win Pct</h2>"
              f"<h1 style='font-size: 60px; color: #99D9D9;'>{number3*100:.1f}%</h1>"
              f"</div>", unsafe_allow_html=True)

st.markdown("<hr/>", unsafe_allow_html=True)

# Main
html = """
<style>
    table {
        width:100%;
    }
    th {
        text-align:center;
    }
    td {
        text-align:center;
    }
</style>
"""
html += df.to_html(index=False)

st.markdown(html, unsafe_allow_html=True)
