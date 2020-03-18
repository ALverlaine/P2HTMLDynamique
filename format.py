import pandas as pd
import math

#Programme pour faciliter la récupération des données depuis le csv

cases = pd.read_csv("./total_cases.csv")
country = ["Belgium", "France", "Italy", "China", "United Kingdom", "United States"]
for c in country:
    print(c)
    for x in cases[c]:
        
        if math.isnan(x):
            print(0, end=", ")
        else:
            print(x, end=", ")

    print("")
    print("")
    print("")
    print("")


"""
for x in cases["date"]:
    print('"' + str(x) + '"', end=", ")
    """