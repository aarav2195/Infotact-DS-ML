import joblib
import pandas as pd
import streamlit as st

from config import (
    NODES_FILE,
    TARGETS_FILE,
    MODEL_COMPARISON_FILE,
    ERROR_ANALYSIS_FILE,
    PRICE_RANGE_FILE,
    DASHBOARD_PREDICTIONS_FILE,
    XGB_MODEL_FILE,
    BASELINE_GNN_PREDICTIONS_FILE,
    ATTENTION_GNN_PREDICTIONS_FILE,
)


@st.cache_data
def load_nodes():
    return pd.read_csv(
        NODES_FILE
    )


@st.cache_data
def load_targets():
    return pd.read_csv(
        TARGETS_FILE
    )


@st.cache_data
def load_model_comparison():
    return pd.read_csv(
        MODEL_COMPARISON_FILE
    )


@st.cache_data
def load_error_analysis():
    return pd.read_csv(
        ERROR_ANALYSIS_FILE
    )


@st.cache_data
def load_price_range_analysis():
    return pd.read_csv(
        PRICE_RANGE_FILE
    )


@st.cache_data
def load_dashboard_predictions():
    return pd.read_csv(
        DASHBOARD_PREDICTIONS_FILE
    )


@st.cache_data
def load_gnn_predictions():

    baseline = pd.read_csv(
        BASELINE_GNN_PREDICTIONS_FILE
    )

    attention = pd.read_csv(
        ATTENTION_GNN_PREDICTIONS_FILE
    )

    return baseline, attention


@st.cache_resource
def load_model():
    return joblib.load(
        XGB_MODEL_FILE
    )


def get_feature_columns(
    nodes_df
):
    return [
        col
        for col in nodes_df.columns
        if col not in [
            "node_id",
            "id"
        ]
    ]


@st.cache_data
def prepare_property_data():

    nodes = (
        load_nodes()
        .sort_values("node_id")
        .reset_index(drop=True)
    )

    targets = (
        load_targets()
        .sort_values("node_id")
        .reset_index(drop=True)
    )

    model = load_model()

    feature_columns = get_feature_columns(
        nodes
    )

    predictions = model.predict(
        nodes[feature_columns]
    )

    # Keep the complete feature dataframe.
    properties = nodes.copy()

    properties[
        "actual_price"
    ] = targets[
        "price"
    ].values

    properties[
        "predicted_price"
    ] = predictions

    properties[
        "prediction_error"
    ] = (
        properties["actual_price"]
        - properties["predicted_price"]
    )

    properties[
        "absolute_error"
    ] = (
        properties["prediction_error"]
        .abs()
    )

    properties[
        "percentage_error"
    ] = (
        properties["absolute_error"]
        /
        properties["actual_price"]
    ) * 100

    return properties