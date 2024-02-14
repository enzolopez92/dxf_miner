import pandas as pd
import numpy as np
import statsmodels.api as sm

# Create a pandas DataFrame from the given data
data = {
    'Age': [18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 27, 27, 27, 27, 27, 27, 27, 27, 29, 29, 29, 29, 29, 29, 29, 35, 35, 35, 35, 35, 35, 35, 35, 40, 40, 40, 40, 40, 40, 40, 45, 45, 45, 45, 45, 45, 45, 45, 50, 50, 50],
    'Years Trying': [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 5, 10, 20, 0, 5, 5, 10, 20, 20, 5, 5, 5, 5, 0, 1, 5, 7, 5, 5, 10, 15, 0, 2, 9, 9, 0, 1, 0, 10, 20, 5, 5, 5, 5, 5, 5, 0, 1, 1, 0, 0, 5, 10, 20, 0, 5, 20],
    'Ovulation Problem': ['no', 'yes', 'no', 'no', 'no', 'no', 'no', 'yes', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'yes', 'no', 'no'],
    'Fertility Problem': ['no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no'],
    'Pregnant Before': ['no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'],
    'Tubes issue': ['no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'yes', 'yes', 'yes'],
    'Male fertility issue': ['no', 'no', 'no', 'no', 'no', 'yes', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'yes', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no', 'no'],
    'Success Rate': [0.3921, 0.4039, 0.4066, 0.4107, 0.3696, 0.3684, 0.3465, 0.4185, 0.4113, 0.3616, 0.3627, 0.3576, 0.3244, 0.2634, 0.4388, 0.4029, 0.4029, 0.368, 0.3024, 0.3024, 0.4148, 0.4175, 0.4216, 0.3801, 0.4522, 0.4449, 0.4017, 0.416, 0.3918, 0.4036, 0.3807, 0.3466, 0.4607, 0.4461, 0.3958, 0.3958, 0.4492, 0.4446, 0.3938, 0.326, 0.2647, 0.3706, 0.3731, 0.3771, 0.3374, 0.3364, 0.1803, 0.176, 0.1833, 0.1877, 0.1744, 0.1595, 0.1407, 0.1087, 0.0386, 0.0334, 0.0351, 0.0354, 0.036, 0.036, 0.0251, 0.0217, 0.0072, 0.0062, 0.004]
}

df = pd.DataFrame(data)

# Convert categorical variables to numeric using one-hot encoding
df = pd.get_dummies(df, columns=['Ovulation Problem', 'Fertility Problem', 'Pregnant Before', 'Tubes issue', 'Male fertility issue'])

# Convert success rate to decimal
df['Success Rate'] = df['Success Rate'] / 100

# Define independent and dependent variables
X = df.drop('Success Rate', axis=1)
y = df['Success Rate']

# Fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Print the model coefficients
print('Intercept:', model.intercept_)
print('Coefficients:', model.coef_)
