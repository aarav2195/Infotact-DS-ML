import streamlit as st
import plotly.graph_objects as go

from utils.prediction import (
    predict_property,
)

from utils.ui import (
    page_header,
    divider,
)


def render(
    nodes_df,
    model,
    feature_columns,
    properties,
):

    page_header(
        "What-If Valuation",
        icon="🧪",
        subtitle=(
            "Simulate property improvements while holding "
            "spatial context constant."
        ),
    )

    node_ids = (
        properties["node_id"]
        .sort_values()
        .tolist()
    )

    selected_node = st.selectbox(
        "Base Property",
        node_ids,
    )

    row = (
        properties[
            properties["node_id"]
            == selected_node
        ]
        .iloc[0]
        .copy()
    )

    current_prediction = float(
        model.predict(
            row[
                feature_columns
            ].to_frame().T
        )[0]
    )

    divider()

    st.subheader(
        "Scenario Controls"
    )

    left, right = st.columns(2)

    with left:

        bedrooms = st.number_input(
            "Bedrooms",
            min_value=0.0,
            max_value=20.0,
            value=float(
                row["bedrooms"]
            ),
            step=1.0,
        )

        bathrooms = st.number_input(
            "Bathrooms",
            min_value=0.0,
            max_value=20.0,
            value=float(
                row["bathrooms"]
            ),
            step=0.25,
        )

        sqft_living = st.number_input(
            "Living Area (sqft)",
            min_value=200.0,
            max_value=15000.0,
            value=float(
                row["sqft_living"]
            ),
            step=50.0,
        )

        sqft_lot = st.number_input(
            "Lot Area (sqft)",
            min_value=500.0,
            max_value=100000.0,
            value=float(
                row["sqft_lot"]
            ),
            step=100.0,
        )

    with right:

        floors = st.number_input(
            "Floors",
            min_value=1.0,
            max_value=5.0,
            value=float(
                row["floors"]
            ),
            step=0.5,
        )

        grade = st.slider(
            "Grade",
            min_value=1,
            max_value=13,
            value=int(
                row["grade"]
            ),
        )

        condition = st.slider(
            "Condition",
            min_value=1,
            max_value=5,
            value=int(
                row["condition"]
            ),
        )

        waterfront = st.selectbox(
            "Waterfront",
            [0, 1],
            index=int(
                row["waterfront"]
            ),
        )

    updated = row.copy()

    updated["bedrooms"] = bedrooms
    updated["bathrooms"] = bathrooms
    updated["sqft_living"] = sqft_living
    updated["sqft_lot"] = sqft_lot
    updated["floors"] = floors
    updated["grade"] = grade
    updated["condition"] = condition
    updated["waterfront"] = waterfront

    if "sqft_basement" in updated.index:

        updated["sqft_above"] = max(
            sqft_living
            - float(
                updated["sqft_basement"]
            ),
            0,
        )

    scenario_prediction = predict_property(
        model,
        updated[
            feature_columns
        ].to_dict(),
        feature_columns,
    )

    delta = (
        scenario_prediction
        - current_prediction
    )

    percent_change = (
        delta
        /
        current_prediction
    ) * 100

    divider()

    # ---------------------------------------------------------
    # RESULT CARDS
    # ---------------------------------------------------------

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Current Estimate",
            f"${current_prediction:,.0f}",
        )

    with c2:

        st.metric(
            "What-If Estimate",
            f"${scenario_prediction:,.0f}",
        )

    with c3:

        st.metric(
            "Estimated Change",
            f"${delta:+,.0f}",
            f"{percent_change:+.2f}%",
        )

    divider()

    # ---------------------------------------------------------
    # VISUAL COMPARISON
    # ---------------------------------------------------------

    fig = go.Figure()

    fig.add_bar(
        x=[
            "Current",
            "What-If",
        ],
        y=[
            current_prediction,
            scenario_prediction,
        ],
    )

    fig.update_layout(
        title="Valuation Scenario",
        yaxis_title="Estimated Price ($)",
        height=430,
        plot_bgcolor="#FBFAF6",
        paper_bgcolor="#FBFAF6",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    st.info(
        "This simulator modifies property characteristics while "
        "holding the existing spatial features constant. It is "
        "designed to estimate the valuation effect of property "
        "changes, not to represent a new geographic location."
    )