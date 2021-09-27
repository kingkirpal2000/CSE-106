import pandas as pd
import matplotlib.pyplot as plt

def lineCharts(weather_data):
    plt.plot(weather_data["actual_max_temp"], color="red")
    plt.plot(weather_data["actual_min_temp"], color="blue")
    plt.show()

def histogramChart(weather_data):
    weather_data["actual_precipitation"].plot(kind="hist")
    plt.show()

def main():
    weather_data = pd.read_csv("weather_data.txt")
    weather_data["date"] = pd.to_datetime(weather_data["date"])
    lineCharts(weather_data)
    histogramChart(weather_data)

if __name__ == "__main__":
    main()