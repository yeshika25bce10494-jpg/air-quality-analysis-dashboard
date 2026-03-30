import pandas as pd

def load_data():
    df = pd.read_csv("data/air_quality.csv")
    return df

def average_aqi(df):
    return round(df["AQI"].mean(), 2)

def most_polluted_city(df):
    return df.sort_values(by="AQI", ascending=False).head(5)

def cleanest_city(df):
    return df.sort_values(by="AQI").head(5)

def pollution_comparison(df):
    return df[["PM2.5", "PM10", "NO2", "CO"]].mean()