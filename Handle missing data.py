import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Create dummy data
data = {
    'Age': [25, 30, None, 28, 35],
    'Gender': ['Female', 'Male', 'Male', 'Female', 'Male'],
    'Income': [50000, 60000, 45000, None, 70000]
    }
df = pd.DataFrame(data)
