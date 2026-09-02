import streamlit as st
import plotly.express as px
import pydeck as pdk

from utils.ui import (
    page_header,
    divider,
)


def render(
    properties,
):

    page_header(
        "Spatial Price Disparity",
        icon="📍",
        subtitle=(
            "Explore geographic patterns in model "
            "over- and under-prediction."
        ),
    )

    metric = st.selectbox(
        "Spatial Metric",
        [
            "Prediction Error",
            "Absolute Error",
            "Percentage Error",
        ],
    )

    if metric == "Prediction Error":

        column = "prediction_error"

    elif metric == "Absolute Error":

        column = "absolute_error"

    else:

        column = "percentage_error"

    sample_size = st.slider(
        "Map Points",
        500,
        min(
            10000,
            len(properties)
        ),
        min(
            5000,
            len(properties)
        ),
        step=500,
    )

    plot_df = (
        properties
        .sample(
            min(
                sample_size,
                len(properties)
            ),
            random_state=42,
        )
        .copy()
    )

    plot_df[
        "display_metric"
    ] = plot_df[column]

    # ---------------------------------------------------------
    # KPI ROW
    # ---------------------------------------------------------

    overpredicted = (
        properties[
            "prediction_error"
        ] < 0
    ).sum()

    underpredicted = (
        properties[
            "prediction_error"
        ] > 0
    ).sum()

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "Mean Absolute Error",
            f"${properties['absolute_error'].mean():,.0f}",
        )

    with c2:

        st.metric(
            "Median Prediction Error",
            f"${properties['prediction_error'].median():,.0f}",
        )

    with c3:

        st.metric(
            "Over-predicted",
            f"{overpredicted:,}",
        )

    with c4:

        st.metric(
            "Under-predicted",
            f"{underpredicted:,}",
        )

    divider()

    left, right = st.columns(2)

    with left:

        fig = px.histogram(
            properties.sample(
                min(
                    6000,
                    len(properties)
                ),
                random_state=42,
            ),
            x="prediction_error",
            nbins=60,
            title="Prediction Error Distribution",
        )

        fig.add_vline(
            x=0,
            line_dash="dash",
        )

        fig.update_layout(
            height=410,
            plot_bgcolor="#FBFAF6",
            paper_bgcolor="#FBFAF6",
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    with right:

        fig = px.scatter(
            plot_df,
            x="actual_price",
            y="prediction_error",
            hover_data=["node_id"],
            title="Prediction Error vs Actual Price",
        )

        fig.add_hline(
            y=0,
            line_dash="dash",
        )

        fig.update_layout(
            height=410,
            plot_bgcolor="#FBFAF6",
            paper_bgcolor="#FBFAF6",
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    divider()

    st.subheader(
        "Spatial Error Map"
    )

    plot_df[
        "display_metric"
    ] = plot_df[column]

    layer = pdk.Layer(
        "ScatterplotLayer",
        data=plot_df,
        get_position="[long, lat]",
        get_radius=85,
        get_fill_color=[
            163,
            77,
            64,
            165,
        ],
        pickable=True,
        auto_highlight=True,
    )

    view_state = pdk.ViewState(
        latitude=float(
            plot_df["lat"].mean()
        ),
        longitude=float(
            plot_df["long"].mean()
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
                "<b>Metric:</b> {display_metric}",
            "style": {
                "backgroundColor": "#10151F",
                "color": "#EFEAE0",
            },
        },
    )

    st.pydeck_chart(
        deck,
        use_container_width=True,
    )