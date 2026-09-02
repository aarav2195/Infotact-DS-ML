import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from utils.ui import (
    page_header,
    divider,
    render_html,
)


def render(properties, model_comparison):

    page_header(
        "GeoValuation AI",
        icon="◈",
        subtitle=(
            "Real-estate valuation, spatial intelligence, "
            "and predictive diagnostics."
        ),
    )

    best = (
        model_comparison
        .sort_values("MAPE")
        .iloc[0]
    )

    render_html(
        f"""
        <div class="gv-hero">
            <div class="gv-hero-kicker">
                SPATIAL VALUATION ENGINE
            </div>
            <div class="gv-hero-title">
                Understand value<br>
                through property + place.
            </div>
            <div class="gv-hero-copy">
                Explore predicted prices, neighborhood context,
                spatial disparities, model performance, and
                property-level explanations from one valuation workspace.
            </div>
            <div class="gv-hero-badge">
                DEPLOYMENT CANDIDATE · {best['Model']} ·
                {best['MAPE']:.2f}% TEST MAPE
            </div>
        </div>
        """
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Properties",
            f"{len(properties):,}",
        )

    with c2:
        st.metric(
            "Median Market Price",
            f"${properties['actual_price'].median():,.0f}",
        )

    with c3:
        st.metric(
            "Predicted Market Price",
            f"${properties['predicted_price'].median():,.0f}",
        )

    with c4:
        st.metric(
            "Champion MAPE",
            f"{best['MAPE']:.2f}%",
        )

    divider()

    left, right = st.columns(2)

    with left:

        sample = properties.sample(
            min(6000, len(properties)),
            random_state=42,
        )

        fig = px.histogram(
            sample,
            x="actual_price",
            nbins=55,
            title="Observed Property Price Distribution",
        )

        fig.update_layout(
            height=410,
            margin=dict(l=10, r=10, t=55, b=10),
            plot_bgcolor="#FBFAF6",
            paper_bgcolor="#FBFAF6",
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    with right:

        sample = properties.sample(
            min(6000, len(properties)),
            random_state=42,
        )

        fig = px.scatter(
            sample,
            x="actual_price",
            y="predicted_price",
            hover_data=["node_id"],
            title="Observed vs Predicted Value",
        )

        lower = min(
            sample["actual_price"].min(),
            sample["predicted_price"].min(),
        )

        upper = max(
            sample["actual_price"].max(),
            sample["predicted_price"].max(),
        )

        fig.add_shape(
            type="line",
            x0=lower,
            y0=lower,
            x1=upper,
            y1=upper,
            line=dict(
                color="#A34D40",
                dash="dash",
            ),
        )

        fig.update_layout(
            height=410,
            margin=dict(l=10, r=10, t=55, b=10),
            plot_bgcolor="#FBFAF6",
            paper_bgcolor="#FBFAF6",
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
        )

    st.markdown(
        '<div class="gv-card">',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="gv-card-title">Model Performance</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="gv-card-caption">Held-out evaluation summary</div>',
        unsafe_allow_html=True,
    )

    display_df = model_comparison.copy()

    display_df["RMSE"] = display_df["RMSE"].map(
        lambda x: f"${x:,.0f}"
    )

    display_df["MAE"] = display_df["MAE"].map(
        lambda x: f"${x:,.0f}"
    )

    display_df["MAPE"] = display_df["MAPE"].map(
        lambda x: f"{x:.2f}%"
    )

    display_df["R2"] = display_df["R2"].map(
        lambda x: f"{x:.4f}"
    )

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="gv-footnote">
            The current deployment candidate is
            <strong>{best['Model']}</strong>.
            Model selection is based on the lowest test MAPE.
        </div>
        """,
        unsafe_allow_html=True,
    )