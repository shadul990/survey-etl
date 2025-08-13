# 01 - EDA and data cleaning

Planned steps:
1. Read raw CSV and show head()
2. Missing values & duplicates summary
3. Value distribution by location
4. Status counts (ok vs check)
5. Cleaning steps (drop duplicates, forward-fill, convert types)
6. Save cleaned CSV (`data/cleaned_sample.csv`)

Example snippet:
```python
import pandas as pd
raw = pd.read_csv('data/raw_sample.csv')
raw.info()
cleaned = raw.drop_duplicates().fillna(method='ffill')
cleaned['value'] = pd.to_numeric(cleaned['value'], errors='coerce')
cleaned.to_csv('data/cleaned_sample.csv', index=False)
