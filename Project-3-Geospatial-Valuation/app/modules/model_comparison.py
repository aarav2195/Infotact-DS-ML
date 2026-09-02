import streamlit as st
import plotly.express as px

from utils.ui import (
    page_header,
    divider,
    render_html,
)


def render(
    model_comparison,
):

    page_header(
        "Model Comparison",
        icon="📊",
        subtitle=(
            "Controlled held-out test performance across "
            "all valuation models."
        ),
    )

    comparison = (
        model_comparison
        .sort_values("MAPE")
        .reset_index(drop=True)
    )

    best = comparison.iloc[0]

    render_html(
        f"""
        <div class="gv-hero">
            <div class="gv-hero-kicker">
                CURRENT CHAMPION
            </div>
            <div class="gv-hero-title">
                {best['Model']}
            </div>
            <div class="gv-hero-copy">
                Lowest test MAPE in the controlled
                model comparison.
            </div>
            <div class="gv-hero-badge">
                {best['MAPE']:.2f}% TEST MAPE
            </div>
        </div>
        """
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Test MAPE",
            f"{best['MAPE']:.2f}%",
        )

    with c2:
        st.metric(
            "Test RMSE",
            f"${best['RMSE']:,.0f}",
        )

    with c3:
        st.metric(
            "Test R²",
            f"{best['R2']:.4f}",
        )

    divider()

    left, right = st.columns(2)

    with left:

        fig = px.bar(
            comparison,
            x="Model",
            y="MAPE",
            title="MAPE Ranking",
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

        fig = px.bar(
            comparison,
            x="Model",
            y="RMSE",
            title="RMSE Ranking",
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

    fig = px.bar(
        comparison,
        x="Model",
        y="R2",
        title="R² Comparison",
    )

    fig.update_layout(
        height=360,
        plot_bgcolor="#FBFAF6",
        paper_bgcolor="#FBFAF6",
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    st.subheader(
        "Performance Summary"
    )

    display_df = comparison.copy()

    display_df["RMSE"] = (
        display_df["RMSE"]
        .map(lambda x: f"${x:,.0f}")
    )

    display_df["MAE"] = (
        display_df["MAE"]
        .map(lambda x: f"${x:,.0f}")
    )

    display_df["MAPE"] = (
        display_df["MAPE"]
        .map(lambda x: f"{x:.2f}%")
    )

    display_df["R2"] = (
        display_df["R2"]
        .map(lambda x: f"{x:.4f}")
    )

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True,
    )

    st.caption(
        "The current deployment candidate is selected using "
        "the lowest test MAPE."
    )