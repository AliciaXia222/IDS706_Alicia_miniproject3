"""
Test goes here

"""


from main import (
    stats_population,
    viz_population,
    report_population,
)
import pandas as pd
import polars as pl


def test_stats_population():
    df = stats_population("population.csv")
    assert df.shape == (9, 9)


def test_report_population():
    report_population()


def test_viz_population():
    viz_population("population.csv")


if __name__ == "__main__":

    test_main()
