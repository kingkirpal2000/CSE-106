import pandas as pd
import datetime
def maxActualPrecipitation(w):
    print(w.actual_precipitation.max())

def averageMaxTemp(w):
    selections = (w["date"] > "07-01-2014") & (w["date"] <= "07-31-2014")
    selections = w.loc[selections]
    print(selections.actual_max_temp.mean())

def recordBreakers(w):
    record = w.iloc[0]
    print(record.date)
    for index, i in w.iterrows():
        if(float(i["actual_max_temp"]) > record["actual_max_temp"]):
            record = i
            print(record.date)

def raininOct(w):
    selections = (w["date"] > "10-01-2014") & (w["date"] <= "10-31-2014")
    selections = w.loc[selections, "actual_precipitation"]
    print(selections.sum())

def betweenDegrees(w):
    found = False
    for index, i in w.iterrows():
        if(i["actual_min_temp"] < 60 and i["actual_max_temp"] > 90):
            found = True
            print(i.date)
    if found == False:
        print("--No Dates match--")
def main():
    weather_data = pd.read_csv("weather_data.txt")
    weather_data["date"] = pd.to_datetime(weather_data["date"])
    print("\n3a.")
    maxActualPrecipitation(weather_data)
    print("\n3b.")
    averageMaxTemp(weather_data)
    print("\n3c.")
    recordBreakers(weather_data)
    print("\n3d.")
    raininOct(weather_data)
    print("\n3e.")
    betweenDegrees(weather_data)
if __name__ == "__main__":
    main()