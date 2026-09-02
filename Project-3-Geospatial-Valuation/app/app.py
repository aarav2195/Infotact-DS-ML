import sys
from pathlib import Path

import streamlit as st

APP_DIR = Path(__file__).resolve().parent

if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from config import APP_TITLE, APP_SUBTITLE

from utils.data_loader import (
    load_nodes,
    load_model,
    load_model_comparison,
    load_error_analysis,
    load_price_range_analysis,
    prepare_property_data,
    get_feature_columns,
)

from utils.ui import inject_css

from modules import (
    overview,
    prediction,
    property_map,
    neighborhood,
    spatial_disparity,
    model_comparison,
    error_analysis,
    what_if,
    model_explanation,
)


st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)


inject_css()


@st.cache_resource
def load_everything():

    nodes = load_nodes()
    model = load_model()
    comparison = load_model_comparison()
    errors = load_error_analysis()
    price_ranges = load_price_range_analysis()
    properties = prepare_property_data()
    features = get_feature_columns(nodes)

    return (
        nodes,
        model,
        comparison,
        errors,
        price_ranges,
        properties,
        features,
    )


try:

    (
        nodes_df,
        model,
        comparison_df,
        error_df,
        price_range_df,
        properties_df,
        feature_columns,
    ) = load_everything()

except Exception as exc:

    st.error("Dashboard initialization failed.")
    st.exception(exc)
    st.stop()


best_model = (
    comparison_df
    .sort_values("MAPE")
    .iloc[0]
)

best_model_name = best_model["Model"]


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.markdown(
        f"""
        <div class="gv-brand">
            <div class="gv-brand-mark">GV</div>
            <div>
                <div class="gv-brand-title">
                    GeoValuation AI
                </div>
                <div class="gv-brand-subtitle">
                    Spatial Intelligence
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="gv-sidebar-rule"></div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="gv-nav-label">ANALYTICS</div>',
        unsafe_allow_html=True,
    )

    page = st.radio(
        "Navigation",
        [
            "Overview",
            "Property Prediction",
            "Interactive Property Map",
            "Neighborhood Intelligence",
            "Spatial Price Disparity",
            "Model Comparison",
            "Error Analysis",
            "What-If Valuation",
            "Prediction Explanation",
        ],
        label_visibility="collapsed",
    )

    st.markdown(
        '<div class="gv-sidebar-rule"></div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="gv-nav-label">SYSTEM STATUS</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="gv-status">
            <div class="gv-status-row">
                <span>Data</span>
                <strong>{len(properties_df):,} properties</strong>
            </div>
            <div class="gv-status-row">
                <span>Features</span>
                <strong>{len(feature_columns)}</strong>
            </div>
            <div class="gv-status-row">
                <span>Champion</span>
                <strong>{best_model_name}</strong>
            </div>
            <div class="gv-status-row">
                <span>Test MAPE</span>
                <strong>{best_model['MAPE']:.2f}%</strong>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="gv-sidebar-footer">
            <span class="gv-live-dot"></span>
            VALUATION ENGINE ONLINE
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# ROUTING
# ---------------------------------------------------------

if page == "Overview":

    overview.render(
        properties_df,
        comparison_df,
    )

elif page == "Property Prediction":

    prediction.render(
        nodes_df,
        model,
        feature_columns,
        properties_df,
    )

elif page == "Interactive Property Map":

    property_map.render(
        properties_df,
        error_df,
    )

elif page == "Neighborhood Intelligence":

    neighborhood.render(
        properties_df,
        nodes_df,
    )

elif page == "Spatial Price Disparity":

    spatial_disparity.render(
        properties_df,
    )

elif page == "Model Comparison":

    model_comparison.render(
        comparison_df,
    )

elif page == "Error Analysis":

    error_analysis.render(
        error_df,
        price_range_df,
    )

elif page == "What-If Valuation":

    what_if.render(
        nodes_df,
        model,
        feature_columns,
        properties_df,
    )

elif page == "Prediction Explanation":

    model_explanation.render(
        nodes_df,
        model,
        feature_columns,
    )