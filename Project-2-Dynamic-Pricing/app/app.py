import os
import sys

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# ---------------------------------------------------
# Project Path
# ---------------------------------------------------

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

# ---------------------------------------------------
# Streamlit Page Config
# ---------------------------------------------------

st.set_page_config(
    page_title="Hotel Dynamic Pricing Dashboard",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# Custom CSS
# ---------------------------------------------------

st.markdown("""
<style>

/* Hide Streamlit branding */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}

/* Main background */
.stApp{
    background-color:#F7F9FC;
}

/* Main title */
.main-title{
    font-size:42px;
    font-weight:700;
    color:#0F172A;
    text-align:center;
    margin-bottom:5px;
}

.sub-title{
    text-align:center;
    color:#475569;
    font-size:18px;
    margin-bottom:30px;
}

/* KPI Cards */
.metric-card{
    background:#FFFFFF;
    padding:22px;
    border-radius:16px;
    text-align:center;
    border-top:5px solid #2563EB;
    box-shadow:0 6px 16px rgba(15,23,42,0.08);
    transition:0.3s ease;
}

.metric-card:hover{
    transform:translateY(-4px);
    box-shadow:0 10px 22px rgba(15,23,42,0.12);
}

.metric-title{
    color:#64748B;
    font-size:16px;
}

.metric-value{
    color:#0F172A;
    font-size:30px;
    font-weight:bold;
}

/* Section Titles */
.section-title{
    font-size:28px;
    color:#0F172A;
    margin-top:20px;
    margin-bottom:10px;
    font-weight:700;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#0F172A;
}

section[data-testid="stSidebar"] *{
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Dashboard Header
# ---------------------------------------------------

st.markdown(
    """
<div class="main-title">
🏨 Hotel Dynamic Pricing Dashboard
</div>

<div class="sub-title">
Deep Reinforcement Learning based Dynamic Pricing System
</div>
""",
unsafe_allow_html=True
)

st.divider()

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

st.sidebar.title("Navigation")

st.sidebar.markdown("---")

st.sidebar.markdown("### Project")

st.sidebar.write("Hotel Dynamic Pricing using Deep Reinforcement Learning")

st.sidebar.markdown("---")

st.sidebar.markdown("### Model")

st.sidebar.success("Deep Q-Network (DQN)")

st.sidebar.markdown("---")

st.sidebar.markdown("### Evaluation")

st.sidebar.write("1000 Simulated Booking Seasons")

st.sidebar.markdown("---")

# =====================================================
# Load Data
# =====================================================

DATA_DIR = os.path.join(PROJECT_ROOT, "data", "processed")

policy_path = os.path.join(DATA_DIR, "policy_evaluation.csv")
comparison_path = os.path.join(DATA_DIR, "final_strategy_comparison.csv")
trajectory_path = os.path.join(DATA_DIR, "price_trajectory.csv")


@st.cache_data
def load_data():
    evaluation = pd.read_csv(policy_path)
    comparison = pd.read_csv(comparison_path)
    trajectory_df = pd.read_csv(trajectory_path)
    return evaluation, comparison, trajectory_df


try:
    evaluation_results, strategy_results, trajectory = load_data()

except FileNotFoundError as e:
    st.error(f"Dataset not found:\n{e}")
    st.stop()

# =====================================================
# KPI Calculations
# =====================================================

average_revenue = evaluation_results["Revenue"].mean()

average_rooms = evaluation_results["Rooms Sold"].mean()

average_occupancy = evaluation_results["Occupancy (%)"].mean()

average_price = evaluation_results["Average Price"].mean()

# =====================================================
# Business Overview
# =====================================================

st.markdown(
"""
<div class="section-title">
📊 Business Overview
</div>
""",
unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">💰 Average Revenue</div>
        <div class="metric-value">${average_revenue:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">🛏 Average Rooms Sold</div>
        <div class="metric-value">{average_rooms:.1f}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📈 Average Occupancy</div>
        <div class="metric-value">{average_occupancy:.1f}%</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">💵 Average Price</div>
        <div class="metric-value">${average_price:.2f}</div>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# Strategy Comparison
# =====================================================

st.markdown(
"""
<div class="section-title">
📊 Strategy Performance Comparison
</div>
""",
unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    fig = px.bar(
        strategy_results,
        x="Strategy",
        y="Average Revenue",
        title="Average Revenue",
        text_auto=".2s",
        color="Strategy"
    )

    fig.update_layout(
        template="plotly_white",
        showlegend=False,
        height=420,
        margin=dict(l=20,r=20,t=60,b=20)
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    fig = px.bar(
        strategy_results,
        x="Strategy",
        y="Average Occupancy (%)",
        title="Average Occupancy",
        text_auto=".2f",
        color="Strategy"
    )

    fig.update_layout(
        template="plotly_white",
        showlegend=False,
        height=420,
        margin=dict(l=20,r=20,t=60,b=20)
    )

    st.plotly_chart(fig, use_container_width=True)

col3, col4 = st.columns(2)

with col3:

    fig = px.bar(
        strategy_results,
        x="Strategy",
        y="Average Rooms Sold",
        title="Average Rooms Sold",
        text_auto=".2f",
        color="Strategy"
    )

    fig.update_layout(
        template="plotly_white",
        showlegend=False,
        height=420,
        margin=dict(l=20,r=20,t=60,b=20)
    )

    st.plotly_chart(fig, use_container_width=True)

with col4:

    fig = px.bar(
        strategy_results,
        x="Strategy",
        y="Average Price",
        title="Average Price",
        text_auto=".2f",
        color="Strategy"
    )

    fig.update_layout(
        template="plotly_white",
        showlegend=False,
        height=420,
        margin=dict(l=20,r=20,t=60,b=20)
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.markdown(
"""
<div class="section-title">
📋 Strategy Comparison Table
</div>
""",
unsafe_allow_html=True
)

comparison_df = strategy_results.copy()

comparison_df.index = comparison_df.index + 1

st.dataframe(
    comparison_df,
    use_container_width=True,
    hide_index=True
)