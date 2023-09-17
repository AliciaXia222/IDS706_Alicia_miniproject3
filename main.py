"""
Main cli or app entry point
"""

import polars as pl
import pandas as pd
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport

# Define a function to read csv file and generate statistical description.
def stats_population(csv):
    # read csv file in polars
    population = pl.scan_csv(csv).fetch()
    
    population_stats = population.describe()
    ''' only work on population.csv dataset '''
    return population_stats[
        ["describe", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]
    ]


# Polars viz for 2022 column of the data
def viz_population(csv):
    """generate example visualization of the population dataset"""
    pd.set_option("display.max_columns", None)
    polars_df = pl.read_csv(csv)
    plt.figure(figsize=(10, 6))
    plt.hist(polars_df["2022"], bins=20, edgecolor="black")
    plt.title("2022 population growth")
    plt.xlabel("population")
    plt.ylabel("Frequency")
    plt.show()


# generate a analyse report, polars dataframe can't be plot using ydata_profiling
# so we need to convert it to pandas dataframe
def report_population():
    population2 = pd.read_csv("population.csv")
    population_report = population2.loc[0:8, ["Country Name", "2022"]]
    profile = ProfileReport(
        population_report, title="Country Population Report", explorative=True
    )
    profile.to_file("data_profiling_report.html")
    return profile
