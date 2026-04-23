import joblib
from src.preprocessing import load_data, preprocess
from src.model import build_model

data = load_data("data/customer_data.csv")
X, y = preprocess(data)

model = build_model()
model.fit(X, y)

joblib.dump(model, "models/model.pkl")

print("Model trained and saved successfully.")