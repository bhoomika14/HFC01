import pandas as pd
from datetime import datetime as dt

df = pd.read_csv("cleaned_dataset_2.csv")
df['sub_type'] = df['sub_type'].str.strip()
df['type'] = df['type'].str.strip()

df['type'] = df['type'].replace("Ransoware", "Ransomware")
df['type'] = df['type'].replace(["Fileless Malware", "Malware Threat"], "Malware")
df['type'] = df['type'].replace(["Phishing Attack", "SMS Phishing"], "Phishing")
df['sub_type'] = df['sub_type'].replace(["Phishing Attack", "SMS Phishing"], "Phishing")
df['type'] = df['type'].replace(["Supply Chain Attack", "Software Supply Chain"], "Supply Chain")

df.to_csv("cyber_risk_dataset.csv", index = False)

data = pd.read_csv("cyber_risk_dataset.csv")
filtered_df = data[(data['type'].isin(['Malware', 'Ransomware', 'Cloud Security', 'Phishing', 'AI threats', 'Supply Chain Attack']))]
filtered_df = filtered_df.reset_index(drop=True)

filtered_df['posted_date'] = pd.to_datetime(filtered_df['posted_date'])

unique_dates = filtered_df['posted_date'].unique()
unique_risk = filtered_df['type'].unique()

occurrences_dict = {}

for date in unique_dates:
    for risk_name in unique_risk:
        filtered_df2 = filtered_df[(filtered_df['posted_date'] == date) & (filtered_df['type'] == risk_name)]
        occurrences_count = filtered_df2.shape[0]
        occurrences_dict[(date, risk_name)] = occurrences_count

occurrences_df = pd.DataFrame(list(occurrences_dict.items()), columns=['risk_name', 'count'])
occurrences_df[['date', 'risk_name']] = pd.DataFrame(occurrences_df['risk_name'].tolist(), index=occurrences_df.index)

occurrences_df.to_csv("trends_by_date.csv", index = False)