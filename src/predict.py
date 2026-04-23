import joblib

def predict_customer(features):
    model = joblib.load("models/model.pkl")
    prediction = model.predict([features])
    return prediction[0]