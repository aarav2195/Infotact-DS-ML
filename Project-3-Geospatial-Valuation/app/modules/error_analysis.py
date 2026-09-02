import streamlit as st
import plotly.express as px

from utils.ui import (
    page_header,
    divider,
)


def render(
    error_analysis,
    price_range_analysis,
):

    page_header(
        "Prediction Error Analysis",
        icon="⚠️",
        subtitle=(
            "Understand where the selected XGBoost model "
            "performs well and where valuation errors concentrate."
        ),
    )

    # ---------------------------------------------------------
    # BASIC ERROR SERIES
    # ---------------------------------------------------------

    abs_errors = (
        error_analysis[
            "xgboost_absolute_error"
        ]
    )

    percentage_errors = (
        error_analysis[
            "xgboost_percentage_error"
        ]
    )

    underpredicted = (
        error_analysis[
            "xgboost_prediction"
        ]
        <
        error_analysis[
            "actual_price"
        ]
    ).sum()

    overpredicted = (
        error_analysis[
            "xgboost_prediction"
        ]
        >
        error_analysis[
            "actual_price"
        ]
    ).sum()

    p90 = abs_errors.quantile(0.90)
    p95 = abs_errors.quantile(0.95)

    # ---------------------------------------------------------
    # KPI ROW
    # ---------------------------------------------------------

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "Mean Absolute Error",
            f"${abs_errors.mean():,.0f}",
        )

    with c2:

        st.metric(
            "Median Absolute Error",
            f"${abs_errors.median():,.0f}",
        )

    with c3:

        st.metric(
            "90th Percentile Error",
            f"${p90:,.0f}",
        )

    with c4:

        st.metric(
            "Mean MAPE",
            f"{percentage_errors.mean():.2f}%",
        )

    divider()

    # ---------------------------------------------------------
    # DIRECTIONAL ERROR
    # ---------------------------------------------------------

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Under-predicted",
            f"{underpredicted:,}",
        )

    with c2:

        st.metric(
            "Over-predicted",
            f"{overpredicted:,}",
        )

    with c3:

        st.metric(
            "95th Percentile Error",
            f"${p95:,.0f}",
        )

    divider()

    # ---------------------------------------------------------
    # DISTRIBUTIONS
    # ---------------------------------------------------------

    sample = error_analysis.sample(
        min(
            6000,
            len(error_analysis),
        ),
        random_state=42,
    )

    left, right = st.columns(2)

    with left:

        fig = px.histogram(
            sample,
            x="xgboost_absolute_error",
            nbins=60,
            title="Absolute Error Distribution",
        )

        fig.update_layout(
            height=420,
            plot_bgcolor="#FBFAF6",
            paper_bgcolor="#FBFAF6",
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    with right:

        fig = px.histogram(
            sample,
            x="xgboost_percentage_error",
            nbins=60,
            title="Percentage Error Distribution",
        )

        fig.update_layout(
            height=420,
            plot_bgcolor="#FBFAF6",
            paper_bgcolor="#FBFAF6",
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    divider()

    # ---------------------------------------------------------
    # ERROR VS PRICE
    # ---------------------------------------------------------

    fig = px.scatter(
        sample,
        x="actual_price",
        y="xgboost_absolute_error",
        hover_data=[
            "node_id",
            "xgboost_prediction",
        ],
        title="Absolute Prediction Error vs Actual Price",
    )

    fig.update_layout(
        height=460,
        plot_bgcolor="#FBFAF6",
        paper_bgcolor="#FBFAF6",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    divider()

    # ---------------------------------------------------------
    # PRICE RANGE
    # ---------------------------------------------------------

    st.subheader(
        "Error by Property Price Range"
    )

    st.dataframe(
        price_range_analysis,
        use_container_width=True,
        hide_index=True,
    )

    divider()

    # ---------------------------------------------------------
    # WORST PREDICTIONS
    # ---------------------------------------------------------

    st.subheader(
        "Highest-Error Properties"
    )

    top_errors = (
        error_analysis
        .sort_values(
            "xgboost_absolute_error",
            ascending=False,
        )
        .head(20)
    )

    display_columns = [
        "node_id",
        "actual_price",
        "xgboost_prediction",
        "xgboost_absolute_error",
        "xgboost_percentage_error",
    ]

    st.dataframe(
        top_errors[
            display_columns
        ],
        use_container_width=True,
        hide_index=True,
    )