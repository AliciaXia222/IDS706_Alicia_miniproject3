"""
Main cli or app entry point
"""

import polars as pl
import pandas as pd
import matplotlib.pyplot as plt


# Define a function to read csv file and generate statistical description.
def stats_population(csv):
    # read csv file in polars
    population = pl.scan_csv(csv).fetch()
    population_stats = population.describe()
    return population_stats[
        ["describe", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022"]
    ]


# Polars viz for 2022 column of the data
def generate_summary_and_visualization(
    data, output_summary_report, histogram_image_path
):

    """generate example visualization of the population dataset"""
    pd.set_option("display.max_columns", None)
    polars_df = pl.read_csv(data)
    plt.figure(figsize=(10, 6))
    plt.hist(polars_df["2022"], bins=20, edgecolor="black")
    plt.title("2022 population growth")
    plt.xlabel("population")
    plt.ylabel("Frequency")
    plt.savefig(histogram_image_path, bbox_inches="tight")
    plt.show()

    with open(output_summary_report, "w", encoding="utf-8") as markdown_file:
        markdown_file.write(
            stats_population("population.csv").to_pandas().to_markdown()
        )
        markdown_file.write(f"\n![Histogram]({histogram_image_path})\n")
    print(f"Summary report saved to {output_summary_report}")
