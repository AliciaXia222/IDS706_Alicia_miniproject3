"""
Test goes here

"""


from main import stats_population, generate_summary_and_visualization
import polars as pl


def test_stats_population():
    df = stats_population("population.csv")
    assert df.shape == (9, 9)


def test_generate_summary_and_visualization():
    data = "population.csv"
    output_summary_report = "test_summary_report.md"
    histogram_image_path = "test_histogram.png"
    generate_summary_and_visualization(
        data, output_summary_report, histogram_image_path
    )


if __name__ == "__main__":
    test_generate_summary_and_visualization()
