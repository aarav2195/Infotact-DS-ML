import streamlit as st
import pydeck as pdk

from utils.ui import (
    page_header,
    divider,
)


def render(
    properties,
    error_analysis,
):

    page_header(
        "Interactive Property Map",
        icon="🗺️",
        subtitle=(
            "Explore property values, model predictions, "
            "and valuation performance geographically."
        ),
    )

    # ---------------------------------------------------------
    # CONTROLS
    # ---------------------------------------------------------

    c1, c2, c3 = st.columns(
        [1.1, 1.3, 1]
    )

    with c1:

        dataset_choice = st.selectbox(
            "Dataset",
            [
                "All Properties",
                "Evaluation Test Set",
            ],
        )

    with c2:

        metric_choice = st.selectbox(
            "Map Metric",
            [
                "Predicted Price",
                "Actual Price",
                "Absolute Error",
                "Percentage Error",
            ],
        )

    with c3:

        max_points = st.slider(
            "Map Points",
            min_value=500,
            max_value=min(
                15000,
                len(properties),
            ),
            value=min(
                5000,
                len(properties),
            ),
            step=500,
        )

    # ---------------------------------------------------------
    # DATASET
    # ---------------------------------------------------------

    if (
        dataset_choice
        == "Evaluation Test Set"
    ):

        map_df = error_analysis.merge(
            properties[
                [
                    "node_id",
                    "lat",
                    "long",
                ]
            ],
            on="node_id",
            how="left",
        )

        metric_columns = {
            "Predicted Price":
                "xgboost_prediction",

            "Actual Price":
                "actual_price",

            "Absolute Error":
                "xgboost_absolute_error",

            "Percentage Error":
                "xgboost_percentage_error",
        }

    else:

        map_df = properties.copy()

        metric_columns = {
            "Predicted Price":
                "predicted_price",

            "Actual Price":
                "actual_price",

            "Absolute Error":
                "absolute_error",

            "Percentage Error":
                "percentage_error",
        }

    map_df = map_df.dropna(
        subset=[
            "lat",
            "long",
        ]
    )

    if len(map_df) > max_points:

        map_df = map_df.sample(
            max_points,
            random_state=42,
        )

    value_column = metric_columns[
        metric_choice
    ]

    map_df[
        "display_value"
    ] = map_df[
        value_column
    ]

    # ---------------------------------------------------------
    # SUMMARY
    # ---------------------------------------------------------

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Properties Displayed",
            f"{len(map_df):,}",
        )

    with c2:

        if (
            "Error"
            in metric_choice
            or "Percentage"
            in metric_choice
        ):

            suffix = (
                "%"
                if "Percentage"
                in metric_choice
                else ""
            )

            st.metric(
                "Mean Metric",
                f"{map_df['display_value'].mean():,.2f}{suffix}",
            )

        else:

            st.metric(
                "Mean Value",
                f"${map_df['display_value'].mean():,.0f}",
            )

    with c3:

        if (
            "Error"
            in metric_choice
            or "Percentage"
            in metric_choice
        ):

            suffix = (
                "%"
                if "Percentage"
                in metric_choice
                else ""
            )

            st.metric(
                "Maximum Metric",
                f"{map_df['display_value'].max():,.2f}{suffix}",
            )

        else:

            st.metric(
                "Maximum Value",
                f"${map_df['display_value'].max():,.0f}",
            )

    divider()

    # ---------------------------------------------------------
    # MAP
    # ---------------------------------------------------------

    layer = pdk.Layer(
        "ScatterplotLayer",
        data=map_df,
        get_position="[long, lat]",
        get_radius=75,
        get_fill_color=[
            44,
            98,
            101,
            160,
        ],
        pickable=True,
        auto_highlight=True,
    )

    view_state = pdk.ViewState(
        latitude=float(
            map_df["lat"].mean()
        ),
        longitude=float(
            map_df["long"].mean()
        ),
        zoom=9.2,
    )

    deck = pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        map_style="light",
        tooltip={
            "html":
                "<b>Property:</b> {node_id}<br/>"
                "<b>Actual:</b> ${actual_price}<br/>"
                "<b>Predicted:</b> ${predicted_price}<br/>"
                "<b>Absolute Error:</b> ${absolute_error}<br/>"
                "<b>Metric:</b> {display_value}",
            "style": {
                "backgroundColor": "#10151F",
                "color": "#EFEAE0",
                "fontFamily": "DM Mono, monospace",
                "fontSize": "12px",
            },
        },
    )

    st.pydeck_chart(
        deck,
        use_container_width=True,
    )

    divider()

    st.subheader(
        "Mapped Property Records"
    )

    table_columns = [
        "node_id",
        "lat",
        "long",
        "actual_price",
        "predicted_price",
        "absolute_error",
        "percentage_error",
    ]

    table_columns = [
        col
        for col in table_columns
        if col in map_df.columns
    ]

    st.dataframe(
        map_df[
            table_columns
        ],
        use_container_width=True,
        hide_index=True,
    )