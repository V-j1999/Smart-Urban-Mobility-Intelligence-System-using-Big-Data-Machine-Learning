import pandas as pd
import glob
import joblib
from sklearn.ensemble import RandomForestRegressor

# Load processed CSV files
files = glob.glob("data/processed/*.csv")
df = pd.concat([pd.read_csv(f) for f in files])

X = df[['hour', 'day']]
y = df['count']

model = RandomForestRegressor()
model.fit(X, y)

joblib.dump(model, "ml/model.pkl")

print("✅ Model trained and saved")
