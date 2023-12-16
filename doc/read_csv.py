import csv
import pandas as pd
head = ['rank', 'title', 'lifetime_gross', 'year']

df = pd.read_csv('./web_qtx.csv', names=head, encoding="ISO-8859-1")
print(df)