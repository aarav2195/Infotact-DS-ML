import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import pydeck as pdk

from utils.spatial import find_neighbors

from utils.ui import (
    page_header,
    divider,
    render_html,
)


def render(
    properties,
    nodes_df,
):

    # =========================================================
    # PAGE HEADER
    # =========================================================

    page_header(
        "Neighborhood Intelligence",
        icon="🏘️",
        subtitle=(
            "Understand how a property compares with "
            "its surrounding spatial neighborhood."
        ),
    )

    # =========================================================
    # PROPERTY CONTROLS
    # =========================================================

    control_left, control_right = st.columns(
        [2.2, 1],
        gap="large",
    )

    with control_left:

        st.markdown(
            "### Select Property"
        )

        node_ids = (
            properties["node_id"]
            .sort_values()
            .tolist()
        )

        selected_node = st.selectbox(
            "Property",
            node_ids,
            label_visibility="collapsed",
        )

    with control_right:

        st.markdown(
            "### Neighborhood Size"
        )

        neighbor_count = st.slider(
            "Number of Neighbors",
            min_value=5,
            max_value=30,
            value=10,
            label_visibility="collapsed",
            help=(
                "Number of nearby properties included "
                "in neighborhood analysis."
            ),
        )

    selected = (
        properties[
            properties["node_id"]
            == selected_node
        ]
        .iloc[0]
    )

    # =========================================================
    # FIND NEIGHBORS
    # =========================================================

    neighbors = find_neighbors(
        properties,
        selected["lat"],
        selected["long"],
        n_neighbors=neighbor_count,
    )

    if neighbors.empty:

        st.warning(
            "No neighboring properties were found "
            "for this location."
        )

        return

    # =========================================================
    # STATISTICS
    # =========================================================

    selected_price = float(
        selected["actual_price"]
    )

    local_mean = float(
        neighbors["actual_price"].mean()
    )

    local_median = float(
        neighbors["actual_price"].median()
    )

    price_min = float(
        neighbors["actual_price"].min()
    )

    price_max = float(
        neighbors["actual_price"].max()
    )

    nearest_distance = float(
        neighbors["distance_km"].min()
    )

    average_distance = float(
        neighbors["distance_km"].mean()
    )

    premium_vs_median = (
        (
            selected_price
            - local_median
        )
        / local_median
    ) * 100

    # =========================================================
    # TOP KPI STRIP
    # =========================================================

    k1, k2, k3, k4 = st.columns(4)

    with k1:
        st.metric(
            "Selected Property",
            f"${selected_price:,.0f}",
        )

    with k2:
        st.metric(
            "Local Median",
            f"${local_median:,.0f}",
        )

    with k3:
        st.metric(
            "Vs Local Median",
            f"{premium_vs_median:+.1f}%",
        )

    with k4:
        st.metric(
            "Nearest Property",
            f"{nearest_distance:.2f} km",
        )

    divider()

    # =========================================================
    # MAIN ANALYSIS PANELS
    # =========================================================

    # Wider snapshot panel so long values fit.
    left, right = st.columns(
        [1.45, 1.0],
        gap="large",
    )

    # =========================================================
    # LEFT — PRICE ANALYSIS
    # =========================================================

    with left:

        with st.container(
            border=True,
            height=650,
        ):

            st.subheader(
                "Nearby Property Prices"
            )

            st.caption(
                "Observed prices across the nearest "
                "spatially connected properties."
            )

            chart_df = (
                neighbors[
                    [
                        "node_id",
                        "distance_km",
                        "actual_price",
                    ]
                ]
                .sort_values(
                    "distance_km"
                )
                .copy()
            )

            fig = go.Figure()

            fig.add_trace(
                go.Bar(
                    x=chart_df["distance_km"],
                    y=chart_df["actual_price"],
                    marker=dict(
                        color="#2D6265"
                    ),
                    hovertemplate=(
                        "<b>Distance:</b> %{x:.3f} km<br>"
                        "Actual Price: $%{y:,.0f}"
                        "<extra></extra>"
                    ),
                )
            )

            fig.add_hline(
                y=selected_price,
                line_dash="dash",
                line_color="#A34D40",
                annotation_text=(
                    f"Selected · ${selected_price:,.0f}"
                ),
                annotation_position="top left",
            )

            fig.update_layout(
                height=515,
                margin=dict(
                    l=15,
                    r=15,
                    t=10,
                    b=20,
                ),
                plot_bgcolor="#FBFAF6",
                paper_bgcolor="#FBFAF6",
                font=dict(
                    family="Manrope, sans-serif",
                    color="#27313D",
                ),
                xaxis=dict(
                    title="Distance from Selected Property (km)",
                    showgrid=False,
                ),
                yaxis=dict(
                    title="Actual Price ($)",
                    gridcolor="#DDD7CB",
                ),
                showlegend=False,
            )

            st.plotly_chart(
                fig,
                use_container_width=True,
                config={
                    "displayModeBar": False,
                },
            )

            st.caption(
                f"{len(neighbors)} nearby properties compared."
            )

    # =========================================================
    # RIGHT — NEIGHBORHOOD SNAPSHOT
    # =========================================================

    with right:

        with st.container(
            border=True,
            height=650,
        ):

            st.subheader(
                "Neighborhood Snapshot"
            )

            st.caption(
                "Compact summary of the selected property's "
                "local spatial context."
            )

            # -------------------------------------------------
            # ROW 1: MEAN + MEDIAN
            # -------------------------------------------------

            a, b = st.columns(
                [1, 1],
                gap="small",
            )

            with a:

                render_html(
                    f"""
                    <div class="gv-neighbor-stat">
                        <div class="gv-neighbor-label">
                            LOCAL MEAN
                        </div>
                        <div class="gv-neighbor-value">
                            ${local_mean:,.0f}
                        </div>
                    </div>
                    """
                )

            with b:

                render_html(
                    f"""
                    <div class="gv-neighbor-stat">
                        <div class="gv-neighbor-label">
                            LOCAL MEDIAN
                        </div>
                        <div class="gv-neighbor-value">
                            ${local_median:,.0f}
                        </div>
                    </div>
                    """
                )

            # -------------------------------------------------
            # ROW 2: FULL-WIDTH PRICE RANGE
            # -------------------------------------------------

            render_html(
                f"""
                <div class="gv-neighbor-stat gv-neighbor-wide">
                    <div class="gv-neighbor-label">
                        NEIGHBORHOOD PRICE RANGE
                    </div>
                    <div class="gv-neighbor-value gv-range-value-clean">
                        ${price_min:,.0f}
                        <span class="gv-range-separator">
                            –
                        </span>
                        ${price_max:,.0f}
                    </div>
                </div>
                """
            )

            # -------------------------------------------------
            # ROW 3: PROPERTIES + DISTANCE
            # -------------------------------------------------

            c, d = st.columns(
                [1, 1],
                gap="small",
            )

            with c:

                render_html(
                    f"""
                    <div class="gv-neighbor-stat">
                        <div class="gv-neighbor-label">
                            PROPERTIES COMPARED
                        </div>
                        <div class="gv-neighbor-value">
                            {len(neighbors)}
                        </div>
                    </div>
                    """
                )

            with d:

                render_html(
                    f"""
                    <div class="gv-neighbor-stat">
                        <div class="gv-neighbor-label">
                            AVERAGE DISTANCE
                        </div>
                        <div class="gv-neighbor-value">
                            {average_distance:.2f} km
                        </div>
                    </div>
                    """
                )

            # -------------------------------------------------
            # COMPARISON STRIP
            # -------------------------------------------------

            comparison_class = (
                "gv-positive"
                if premium_vs_median >= 0
                else "gv-negative"
            )

            comparison_text = (
                "above"
                if premium_vs_median >= 0
                else "below"
            )

            render_html(
                f"""
                <div class="gv-neighbor-comparison">
                    <div class="gv-neighbor-label">
                        SELECTED PROPERTY VS LOCAL MEDIAN
                    </div>

                    <div class="
                        gv-neighbor-comparison-value
                        {comparison_class}
                    ">
                        {premium_vs_median:+.1f}%
                    </div>

                    <div class="gv-neighbor-comparison-copy">
                        The selected property is
                        {abs(premium_vs_median):.1f}% {comparison_text}
                        the neighborhood median.
                    </div>
                </div>
                """
            )

            # -------------------------------------------------
            # COORDINATE REFERENCE
            # -------------------------------------------------

            render_html(
                f"""
                <div class="gv-neighbor-location">
                    <span>
                        SELECTED LOCATION
                    </span>

                    <strong>
                        {selected['lat']:.5f}
                    </strong>

                    <strong>
                        {selected['long']:.5f}
                    </strong>
                </div>
                """
            )

    divider()

    # =========================================================
    # SPATIAL NEIGHBORHOOD
    # =========================================================

    st.subheader(
        "Spatial Neighborhood"
    )

    st.caption(
        "The selected property is highlighted in red; "
        "nearby properties are shown in gold."
    )

    map_df = neighbors.copy()

    # ---------------------------------------------------------
    # NEIGHBOR LAYER
    # ---------------------------------------------------------

    neighbor_layer = pdk.Layer(
        "ScatterplotLayer",
        data=map_df,
        get_position="[long, lat]",
        get_radius=75,
        get_fill_color=[
            177,
            138,
            72,
            185,
        ],
        pickable=True,
        auto_highlight=True,
    )

    # ---------------------------------------------------------
    # SELECTED PROPERTY
    # ---------------------------------------------------------

    selected_df = pd.DataFrame(
        [
            {
                "lat": selected["lat"],
                "long": selected["long"],
                "node_id": selected_node,
                "actual_price": selected_price,
            }
        ]
    )

    selected_layer = pdk.Layer(
        "ScatterplotLayer",
        data=selected_df,
        get_position="[long, lat]",
        get_radius=155,
        get_fill_color=[
            163,
            77,
            64,
            230,
        ],
        stroked=True,
        get_line_color=[
            15,
            23,
            32,
            255,
        ],
        line_width_min_pixels=2,
        pickable=True,
    )

    view_state = pdk.ViewState(
        latitude=float(
            selected["lat"]
        ),
        longitude=float(
            selected["long"]
        ),
        zoom=11.5,
        pitch=0,
    )

    deck = pdk.Deck(
        layers=[
            neighbor_layer,
            selected_layer,
        ],
        initial_view_state=view_state,
        map_style="light",
        tooltip={
            "html":
                "<b>Property:</b> {node_id}<br/>"
                "<b>Price:</b> ${actual_price}<br/>"
                "<b>Distance:</b> {distance_km} km",
            "style": {
                "backgroundColor": "#10151F",
                "color": "#EFEAE0",
                "fontFamily": "Manrope, sans-serif",
            },
        },
    )

    st.pydeck_chart(
        deck,
        use_container_width=True,
        height=520,
    )

    divider()

    # =========================================================
    # NEAREST PROPERTIES
    # =========================================================

    st.subheader(
        "Nearest Properties"
    )

    st.caption(
        "Properties ranked by geographic distance "
        "from the selected property."
    )

    table_df = (
        neighbors[
            [
                "node_id",
                "distance_km",
                "actual_price",
                "predicted_price",
            ]
        ]
        .sort_values(
            "distance_km"
        )
        .copy()
        .rename(
            columns={
                "node_id": "Property ID",
                "distance_km": "Distance (km)",
                "actual_price": "Actual Price",
                "predicted_price": "Predicted Price",
            }
        )
    )

    st.dataframe(
        table_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Distance (km)": st.column_config.NumberColumn(
                format="%.3f km"
            ),
            "Actual Price": st.column_config.NumberColumn(
                format="$%,.0f"
            ),
            "Predicted Price": st.column_config.NumberColumn(
                format="$%,.0f"
            ),
        },
    )