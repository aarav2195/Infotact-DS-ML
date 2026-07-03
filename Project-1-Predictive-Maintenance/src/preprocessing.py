import pandas as pd

def prepare_features(df):
    """
    Prepare input features before prediction.
    """

    if "Machine failure" in df.columns:
        df = df.drop(columns=["Machine failure"])

    leakage_columns = [
        "TWF",
        "HDF",
        "PWF",
        "OSF",
        "RNF"
    ]

    df = df.drop(columns=[col for col in leakage_columns if col in df.columns],errors="ignore")

    df.columns = (
        df.columns
        .str.replace("[", "", regex=False)
        .str.replace("]", "", regex=False)
        .str.replace("{", "", regex=False)
        .str.replace("}", "", regex=False)
        .str.replace(":", "", regex=False)
        .str.replace(",", "", regex=False)
    )

    return df                