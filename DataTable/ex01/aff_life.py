from load_csv import load
import matplotlib.pyplot as plt
import pandas as pd


def main():
    path = "life_expectancy_years.csv"
    try:
        df = load(path)
        if not isinstance(df, pd.DataFrame):
            return
        print(df["country"][58])
        df.plot()
        plt.title("France Life expectancy Projections")
        plt.ylabel("Life expectancy")
        plt.xlabel("Year")
        plt.show()
    except Exception as e:
        print(f"{type(e).__name__}: {e}.")


if __name__ == "__main__":
    main()