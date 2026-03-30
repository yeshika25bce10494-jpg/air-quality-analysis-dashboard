import streamlit as st
from analysis import load_data, average_aqi, most_polluted_city, cleanest_city, pollution_comparison

st.set_page_config(page_title="Air Quality Dashboard", layout="wide")

st.title("🌍 Air Quality Analysis Dashboard")

df = load_data()

# Sidebar filter
st.sidebar.header("Filter by City")
selected_city = st.sidebar.selectbox("Select City", df["City"].unique())

filtered_df = df[df["City"] == selected_city]

# Main dashboard
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Average AQI")
    st.metric(label="Average AQI", value=average_aqi(df))

with col2:
    st.subheader("🏙 Selected City AQI")
    st.metric(label=selected_city, value=int(filtered_df["AQI"].values[0]))

st.subheader("📋 Dataset")
st.dataframe(df)

st.subheader("🚨 Top 5 Most Polluted Cities")
st.dataframe(most_polluted_city(df))

st.subheader("🌿 Top 5 Cleanest Cities")
st.dataframe(cleanest_city(df))

st.subheader("📈 Pollution Comparison")
st.bar_chart(pollution_comparison(df))