import pandas as pd


def predict_property(
    model,
    feature_row,
    feature_columns,
):

    input_df = pd.DataFrame(
        [feature_row],
        columns=feature_columns,
    )

    prediction = model.predict(
        input_df
    )[0]

    return float(prediction)


def get_local_feature_contributions(
    model,
    feature_row,
    feature_columns,
):

    import xgboost as xgb

    input_df = pd.DataFrame(
        [feature_row],
        columns=feature_columns,
    )

    booster = model.get_booster()

    matrix = xgb.DMatrix(
        input_df,
        feature_names=feature_columns,
    )

    contributions = booster.predict(
        matrix,
        pred_contribs=True,
    )[0]

    feature_values = contributions[:-1]

    result = pd.DataFrame({
        "feature": feature_columns,
        "contribution": feature_values,
    })

    result[
        "abs_contribution"
    ] = (
        result["contribution"]
        .abs()
    )

    return (
        result
        .sort_values(
            "abs_contribution",
            ascending=False,
        )
        .reset_index(drop=True)
    )