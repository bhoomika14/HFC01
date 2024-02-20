import pandas as pd
df = pd.read_csv('cleaned_dataset_2.csv')
df['risk_frequency'] = df.groupby('sub_type')['sub_type'].transform('count')