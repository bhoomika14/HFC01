import pandas as pd
from datetime import datetime as dt

filtered_df['date'] = pd.to_datetime(filtered_df['posted_date'])
filtered_df['month'] = filtered_df['date'].dt.month
count_by_month = filtered_df.groupby(['month', 'type']).size().reset_index(name='count')
count_by_month.to_csv("trends_by_month.csv", index = False)