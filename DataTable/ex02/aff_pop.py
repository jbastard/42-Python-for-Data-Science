from load_csv import load
import matplotlib.pyplot as plt
import seaborn as sns
from sys import argv
import pandas as pd
import matplotlib.ticker as mticker


def pop_parser(pop_str: str) -> float:
    """Convert population strings to float.

    Args:
        pop_str (str): Pop value as a string, e.g., '10M', '250k', or '12345'.

    Returns:
        float: Population as a number in absolute units.
    """
    if pop_str.endswith('B'):
        return float(pop_str[:-1]) * 1e9
    elif pop_str.endswith('M'):
        return float(pop_str[:-1]) * 1e6
    elif pop_str.endswith('k'):
        return float(pop_str[:-1]) * 1e3
    else:
        return float(pop_str)


def population_formatter(x, pos):
    """Format population numbers for plotting based on magnitude.

    Converts values to a readable string with suffixes:
        - 'B' for billions
        - 'M' for millions
        - 'k' for thousands
        - plain integer for smaller numbers

    Args:
        x (float): The value to format.
        pos (int): Position (unused, required by FuncFormatter).

    Returns:
        str: Formatted population string.
    """
    if x >= 1e9:
        return f"{x/1e9:.1f}B"
    elif x >= 1e6:
        return f"{int(x/1e6)}M"
    elif x >= 1e3:
        return f"{int(x/1e3)}k"
    else:
        return str(int(x))


def load_country(dataset: pd.DataFrame, country_key: str) -> pd.DataFrame:
    """Load and reshape a country's population data from wide to long format.


    Converts a wide-format dataset with years as columns into a long-format
    DataFrame suitable for plotting. Also applies `pop_parser` to convert
    population strings to numeric values.
    Args:
        dataset (pd.DataFrame): The full pop dataset
        country_key (str): The country to extract.

    Returns:
        pd.DataFrame: Long-format DataFrame with columns:
            - 'country': str
            - 'Year': int
            - 'Population': float
    """
    country_data = dataset[dataset['country'] == country_key]
    country_long = country_data.melt(
        id_vars='country',
        var_name='Year',
        value_name='Population'
    )
    country_long['Year'] = pd.to_numeric(country_long['Year'])
    country_long['Population'] = country_long['Population'].apply(pop_parser)
    return country_long


def main():
    """Main function load population CSV and plot France and South Korea.

    Loads a CSV file (default: 'population_total.csv' or from argv[1]),
    extracts population data for France and South Korea,
    clips years to 1800-2050,
    formats the y-axis automatically, and displays a Seaborn line plot with the
    legend inside the plot.
    """
    path = ("population_total.csv")
    campus = "France"
    country = ("South Korea")
    dataset = load(path)
    if not dataset.empty:
        try:
            france_long = load_country(dataset, campus)
            sk_long = load_country(dataset, country)

            plt.rcParams['toolbar'] = 'None'

            data_all = pd.concat([france_long, sk_long])
            data_clip = data_all[(data_all['Year'] >= 1800)
                                 & (data_all['Year'] <= 2050)]

            ax = sns.lineplot(
                data=data_clip,
                x="Year",
                y="Population",
                hue="country"
            )

            ax.set_xlim(1795, 2055)
            ax.set_xticks(range(1800, 2051, 40))
            ax.set_xticklabels(range(1800, 2051, 40))

            ax.yaxis.set_major_formatter(
                mticker.FuncFormatter(population_formatter)
            )
            ax.set_title("Population Projections")
            ax.set_xlabel("Year")
            ax.set_ylabel("Population")

            ax.legend(
                loc='lower right',
                frameon=True,
                fancybox=True,
                title=""
            )
            plt.tight_layout()
            plt.show()

        except Exception as e:
            print(f"{Exception.__name__}: {e}")


if __name__ == "__main__":
    main()
