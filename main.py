from src.predict import predict_customer

if __name__ == "__main__":
    result = predict_customer([30, 50000, 2])
    print("Prediction (1=Churn, 0=Stay):", result)