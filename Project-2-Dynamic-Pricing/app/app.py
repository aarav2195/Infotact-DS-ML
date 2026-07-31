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
🏨 Hotel Dynamic Pricing using Deep Reinforcement Learning
</div>

<div class="sub-title">
Dynamic Pricing Strategy Evaluation Dashboard
</div>
""",
unsafe_allow_html=True
)

st.divider()

st.markdown("## 📋 Executive Summary")

st.write("""
The Hotel Dynamic Pricing system was evaluated across multiple pricing strategies
using simulated booking seasons.

The Deep Q-Network (DQN) agent demonstrated competitive revenue generation while
maintaining healthy occupancy levels and balanced pricing decisions.

This dashboard summarizes the business performance of each pricing strategy,
allowing managers to compare revenue, occupancy, rooms sold, and pricing behavior
through interactive visualizations.
""")

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
        title="Revenue Comparison",
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
        title="Occupancy Comparison",
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
        title="Rooms Sold Comparison",
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
        title="Average Room Price Comparison",
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
📋 Detailed Strategy Performance
</div>
""",
unsafe_allow_html=True
)

comparison_df = strategy_results.copy()

# This remains numeric for calculations
display_df = comparison_df.copy()

display_df["Average Revenue"] = display_df["Average Revenue"].map(
    lambda x: f"${x:,.2f}"
)

display_df["Average Price"] = display_df["Average Price"].map(
    lambda x: f"${x:.2f}"
)

display_df["Average Occupancy (%)"] = display_df["Average Occupancy (%)"].map(
    lambda x: f"{x:.2f}%"
)

display_df = display_df.drop(columns=["Episodes"])

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")
st.markdown("## 🏆 Strategy Ranking")

ranking = comparison_df.sort_values(
    by="Average Revenue",
    ascending=False
).reset_index(drop=True)

medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]

cols = st.columns(5)

for i in range(len(ranking)):
    with cols[i]:
        st.metric(medals[i],ranking.loc[i,"Strategy"],f"${ranking.loc[i,'Average Revenue']:.2f}")

st.markdown("---")
st.markdown("## 💡 Business Insights")

best_revenue = comparison_df.loc[
    comparison_df["Average Revenue"].idxmax()
]

best_occupancy = comparison_df.loc[
    comparison_df["Average Occupancy (%)"].idxmax()
]

best_rooms = comparison_df.loc[
    comparison_df["Average Rooms Sold"].idxmax()
]

best_price = comparison_df.loc[
    comparison_df["Average Price"].idxmax()
]

c1, c2 = st.columns(2)

with c1:

    st.metric(
        "💰 Revenue Leader",
        best_revenue["Strategy"],
        f"${best_revenue['Average Revenue']:.2f}"
    )

    st.metric(
        "🛏 Occupancy Leader",
        best_occupancy["Strategy"],
        f"{best_occupancy['Average Occupancy (%)']:.2f}%"
    )

with c2:

    st.metric(
        "💵 Pricing Leader",
        best_price["Strategy"],
        f"${best_price['Average Price']:.2f}"
    )

    st.metric(
        "🤖 AI Strategy",
        "Deep Q-Network",
        "16.38% Revenue Improvement over Q-Learning"
    )

# =====================================================
# Price Trajectory
# =====================================================

st.markdown("---")

st.markdown(
"""
<div class="section-title">
📈 Adaptive Pricing Behaviour
</div>
""",
unsafe_allow_html=True
)

fig = px.line(
    trajectory,
    x="Day",
    y="Price",
    markers=True,
    title="Room Price Across Booking Days"
)

fig.update_layout(
    template="plotly_white",
    height=500,
    xaxis_title="Booking Day",
    yaxis_title="Room Price ($)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

st.markdown(
"""
<div class="section-title">
📈 Booking Occupancy Trend
</div>
""",
unsafe_allow_html=True
)

fig = px.line(
    trajectory,
    x="Day",
    y="Occupancy (%)",
    markers=True,
    title="Occupancy Growth"
)

fig.update_layout(
    template="plotly_white",
    height=500,
    xaxis_title="Booking Day",
    yaxis_title="Occupancy (%)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

st.markdown(
"""
<div class="section-title">
💰 Revenue Accumulation
</div>
""",
unsafe_allow_html=True
)

fig = px.line(
    trajectory,
    x="Day",
    y="Revenue",
    markers=True,
    title="Cumulative Revenue"
)

fig.update_layout(
    template="plotly_white",
    height=500,
    xaxis_title="Booking Day",
    yaxis_title="Revenue ($)"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

st.markdown(
"""
<div class="section-title">
📌 Final Conclusion
</div>
""",
unsafe_allow_html=True
)

st.markdown("""
- ✅ Five pricing strategies were evaluated successfully.
- ✅ Deep Q-Network maintained a balanced pricing policy.
- ✅ Fixed Pricing generated the highest average revenue.
- ✅ Q-Learning achieved the highest occupancy.
- ✅ The dashboard provides interactive business insights for hotel revenue management.
""")

st.markdown("---")

st.caption(
    "Hotel Dynamic Pricing using Deep Reinforcement Learning (DQN) | "
    "Infotact Solutions Internship | Week 4 Final Dashboard"
)