import pandas as pd
df = pd.read_csv('cyber_risk_dataset.csv')
df['sub_type'] = df['sub_type'].str.strip()
df['type'] = df['type'].str.strip()
df['type'].unique()

df['type'] = df['type'].replace("Ransoware", "Ransomware")
df['type'] = df['type'].replace(["Fileless Malware", "Malware Threat"], "Malware")
df['type'] = df['type'].replace(["Phishing Attack", "SMS Phishing"], "Phishing")
df['sub_type'] = df['sub_type'].replace(["Phishing Attack", "SMS Phishing"], "Phishing")
df['type'] = df['type'].replace(["Supply Chain Attacks", "Software Supply Chain"], "Supply Chain")

#groupby date
df['risk_frequency'] = (df.groupby(['type'])['posted_date'].transform('count'))