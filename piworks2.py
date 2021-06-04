import pandas as pd

data = pd.read_csv('country_vaccination_stats.csv')

data["daily_vaccinations"].fillna(data.groupby("country")["daily_vaccinations"].transform("min"), inplace=True)
data["daily_vaccinations"].fillna(0, inplace=True)

print(data.groupby("country")["daily_vaccinations"].median().sort_values(ascending=False).head(3))
