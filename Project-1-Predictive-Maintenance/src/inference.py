import joblib
import pandas as pd

from preprocessing import prepare_features

def predict_machine_failure(model_path,data_path):
    """
    Load model and perform prediction.
    """

    model = joblib.load(model_path)

    df = pd.read_csv(data_path)

    X = prepare_features(df)

    probabilities = model.predict_proba(X)

    predictions = model.predict(X)

    result = pd.DataFrame({
        "Prediction": predictions,
        "Failure Probability": probabilities[:, 1]
    })

    return result