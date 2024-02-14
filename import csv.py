import pandas as pd

df = pd.read_csv('data.csv')

data = {
    'Age': df['Age'].tolist(),
    'Years Trying': df['Years Trying'].tolist(),
    'Ovulation Problem': df['Ovulation Problem'].tolist(),
    'Fertility Problem': df['Fertility Problem'].tolist(),
    'Pregnant Before': df['Pregnant Before'].tolist(),
    'Tubes Issue': df['Tubes issue'].tolist(),
    'Male Fertility Issue': df['Male fertility issue'].tolist(),
    'Success Rate': [float(rate.strip('%')) for rate in df['Success Rate'].tolist()]
}

print(data)
