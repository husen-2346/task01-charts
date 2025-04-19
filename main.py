import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker


# Set Seaborn theme for modern look
sns.set_theme(style="whitegrid")

# Load the dataset
data = pd.read_csv('Data/dataP.csv')

# -------- Line Plot: Population Over Time --------
plt.figure(figsize=(12, 6))
top_countries = ['India', 'China', 'United States', 'Indonesia', 'Brazil']

for country in top_countries:
    country_data = data[data['Country Name'] == country]
    plt.plot(country_data['Year'], country_data['Population'] / 1e9, label=country, linewidth=2.5)

plt.title('🌍 Population Growth Over Time (1960–2023)', fontsize=16, weight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Population (in Billions)', fontsize=12)
plt.legend(title='Country')
plt.grid(True, linestyle='--', alpha=0.3)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()

# -------- Bar Chart: Population in Most Recent Year --------
latest_year = data['Year'].max()
latest_data = data[data['Year'] == latest_year].sort_values(by='Population', ascending=False)

plt.figure(figsize=(12, 6))
bars = sns.barplot(
    x='Country Name', y='Population', data=latest_data,
    palette='pastel', edgecolor='black'
)

# Add text labels on bars
for bar in bars.patches:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f'{int(bar.get_height() / 1e6):,}M',
        ha='center', va='bottom', fontsize=10, color='black'
    )

plt.title(f'🌐 Population by Country in {latest_year}', fontsize=16, weight='bold')
plt.xlabel('')
plt.ylabel('Population (in Millions)', fontsize=12)
plt.xticks(fontsize=11)
plt.yticks(fontsize=10)
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x / 1e6)}M'))
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()
