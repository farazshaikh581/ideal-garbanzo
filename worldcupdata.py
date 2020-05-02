#import codecademylib3_seaborn
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
df = pd.read_csv("WorldCupMatches.csv")
#print(df.head())
df['Total Goals'] =df['Home Team Goals'] + df['Away Team Goals']

sns.set_style("Whitegrid")
sns.set_context("poster", font_scale = 0.8))
f,ax = plt.subplot(figsize = (12, 7))
ax = sns.barplot(x = df['Year'], y = df['Total Goals'])
ax.set_title('Goals from 1930 to 2014')
plt.show()

df_goals = read_csv('goals.csv')
sns.set_context("notebook", font_scale = 1.25)
f, ax2 = plt.subplot(figsize = (12, 7))
ax2 = sns.boxplot(palette = "spectral", data = df_goals, x = df["year"], y = df["goals"])
ax2.set_title("Goals from years")
plt.show()

print(df.head())
