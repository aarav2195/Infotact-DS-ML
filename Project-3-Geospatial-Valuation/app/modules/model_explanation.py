import streamlit as st
import plotly.express as px

from utils.prediction import (
    get_local_feature_contributions,
)

from utils.ui import (
    page_header,
    divider,
    render_html
)


def render(
    nodes_df,
    model,
    feature_columns,
):

    page_header(
        "Prediction Explanation",
        icon="🔍",
        subtitle=(
            "Inspect the local feature contributions "
            "behind an individual XGBoost valuation."
        ),
    )

    # ---------------------------------------------------------
    # PROPERTY SELECTION
    # ---------------------------------------------------------

    node_ids = (
        nodes_df["node_id"]
        .sort_values()
        .tolist()
    )

    selected_node = st.selectbox(
        "Select Property",
        node_ids,
    )

    row = (
        nodes_df[
            nodes_df["node_id"]
            == selected_node
        ]
        .iloc[0]
    )

    prediction = float(
        model.predict(
            row[
                feature_columns
            ].to_frame().T
        )[0]
    )

    # ---------------------------------------------------------
    # PREDICTION HERO
    # ---------------------------------------------------------

    render_html(
        f"""
        <div class="gv-hero">
            <div class="gv-hero-kicker">MODEL EXPLANATION</div>
            <div class="gv-hero-title">${prediction:,.0f}</div>
            <div class="gv-hero-copy">
                Local explanation for property
                <strong>#{selected_node}</strong>.
                Positive contributions increase the prediction,
                while negative contributions decrease it.
            </div>
            <div class="gv-hero-badge">
                XGBOOST LOCAL CONTRIBUTIONS
            </div>
        </div>
        """
    )

    contribution_df = (
        get_local_feature_contributions(
            model,
            row[
                feature_columns
            ].to_dict(),
            feature_columns,
        )
    )

    top_positive = (
        contribution_df[
            contribution_df[
                "contribution"
            ] > 0
        ]
        .head(6)
    )

    top_negative = (
        contribution_df[
            contribution_df[
                "contribution"
            ] < 0
        ]
        .sort_values(
            "contribution"
        )
        .head(6)
    )

    divider()

    # ---------------------------------------------------------
    # DRIVER PANELS
    # ---------------------------------------------------------

    left, right = st.columns(
        [1, 1],
        gap="large",
    )

    with left:

        with st.container(
            border=True
        ):

            st.subheader(
                "Upward Drivers"
            )

            st.caption(
                "Features contributing positively "
                "to estimated value."
            )

            if top_positive.empty:

                st.info(
                    "No positive contributions found."
                )

            else:

                for _, item in top_positive.iterrows():

                    feature_col, value_col = st.columns(
                        [2.2, 1]
                    )

                    with feature_col:

                        st.write(
                            item["feature"]
                        )

                    with value_col:

                        st.markdown(
                            f"""
                            <div class="gv-contribution-positive">
                                +{item['contribution']:,.2f}
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )

    with right:

        with st.container(
            border=True
        ):

            st.subheader(
                "Downward Drivers"
            )

            st.caption(
                "Features contributing negatively "
                "to estimated value."
            )

            if top_negative.empty:

                st.info(
                    "No negative contributions found."
                )

            else:

                for _, item in top_negative.iterrows():

                    feature_col, value_col = st.columns(
                        [2.2, 1]
                    )

                    with feature_col:

                        st.write(
                            item["feature"]
                        )

                    with value_col:

                        st.markdown(
                            f"""
                            <div class="gv-contribution-negative">
                                {item['contribution']:,.2f}
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
    divider()

    # ---------------------------------------------------------
    # CONTRIBUTION CHART
    # ---------------------------------------------------------

    top = (
        contribution_df
        .head(14)
        .sort_values(
            "contribution"
        )
    )

    fig = px.bar(
        top,
        x="contribution",
        y="feature",
        orientation="h",
        title="Top Local Feature Contributions",
        color="contribution",
        color_continuous_scale=[
            "#A6493B",
            "#EFEAE0",
            "#2C5A5E",
        ],
        color_continuous_midpoint=0,
    )

    fig.update_layout(
        height=540,
        plot_bgcolor="#FBFAF6",
        paper_bgcolor="#FBFAF6",
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20,
        ),
        coloraxis_showscale=False,
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
    )

    divider()

    # ---------------------------------------------------------
    # DETAIL TABLE
    # ---------------------------------------------------------

    st.subheader(
        "Contribution Detail"
    )

    display_df = (
        contribution_df[
            [
                "feature",
                "contribution",
            ]
        ]
        .head(20)
        .copy()
    )

    display_df["contribution"] = (
        display_df["contribution"]
        .map(
            lambda x: f"{x:+,.2f}"
        )
    )

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True,
    )

    st.caption(
        "Positive values push the valuation upward; "
        "negative values push it downward."
    )