from load_csv import load
import matplotlib.pyplot as plt


def main():
    path = "life_expectancy_years.csv"
    country = "France"
    try:
        df = load(path)

        row = df[df["country"] == country]
        if row.empty:
            raise ValueError(f"Error: Country '{country}' not found.")

        years = df.columns[1:]

        values = row.iloc[0, 1:].values
        years = years.astype(int)

        plt.figure(figsize=(10, 6))
        plt.plot(years, values, linewidth=2)

        plt.title(f"{country} Life Expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")

        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"{type(e).__name__}: {e}.")


if __name__ == "__main__":
    main()
