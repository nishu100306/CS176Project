from IPython.display import display
import pandas as pd
before = pd.read_csv("Before_Covid.csv")
during = pd.read_csv("During_Covid.csv")
after = pd.read_csv("After_Covid.csv")

df = pd.merge(before, after, how = 'outer')
df = pd.merge(df, during, how = 'outer')
df.drop('open_time', axis=1, inplace=True)
display(df.head().to_markdown())
