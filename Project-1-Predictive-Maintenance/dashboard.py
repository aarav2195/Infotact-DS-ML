import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Predictive Maintenance Dashboard",
    page_icon="🏭",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main{
    background-color:#F5F7FA;
}

.block-container{
    padding-top:1rem;
}

h1{
    color:#0E4C92;
}

.metric-container{
    background:white;
    border-radius:10px;
    padding:15px;
    box-shadow:0px 3px 8px rgba(0,0,0,0.08);
}

div[data-testid="stMetric"]{
    background:white;
    padding:18px;
    border-radius:10px;
    border-left:6px solid #0E4C92;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------

PROJECT_ROOT = Path(__file__).parent

model = joblib.load(
    PROJECT_ROOT /
    "models" /
    "final_lightgbm_model.pkl"
)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("🏭 Predictive Maintenance Dashboard")

st.write(
"""
Monitor industrial machine health using a trained
**LightGBM Machine Learning model**.
"""
)

st.divider()

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.header("Machine Sensor Inputs")

air_temp = st.sidebar.slider(
    "Air Temperature (K)",
    290.0,
    320.0,
    298.0,
    0.1
)

process_temp = st.sidebar.slider(
    "Process Temperature (K)",
    295.0,
    340.0,
    308.0,
    0.1
)

rpm = st.sidebar.slider(
    "Rotational Speed (RPM)",
    1000,
    3000,
    1500
)

torque = st.sidebar.slider(
    "Torque (Nm)",
    5.0,
    120.0,
    40.0,
    0.5
)

tool_wear = st.sidebar.slider(
    "Tool Wear (min)",
    0,
    300,
    20
)

predict = st.sidebar.button(
    "Predict Machine Health",
    use_container_width=True
)

# ---------------------------------------------------
# FEATURE ENGINEERING
# ---------------------------------------------------

load_density = torque / 100

temperature_difference = process_temp - air_temp

temperature_ratio = process_temp / air_temp

load_stress = torque * load_density

rpm_torque_interaction = rpm * torque

tool_wear_mean_10 = tool_wear

air_temp_mean_10 = air_temp

# ---------------------------------------------------
# MODEL INPUT
# ---------------------------------------------------

input_df = pd.DataFrame({

    "rpm_torque_interaction":[rpm_torque_interaction],

    "Rotational_speed_rpm":[rpm],

    "load_stress":[load_stress],

    "Torque_Nm":[torque],

    "load_density":[load_density],

    "Tool_wear_min":[tool_wear],

    "temperature_ratio":[temperature_ratio],

    "tool_wear_mean_10":[tool_wear_mean_10],

    "temperature_difference":[temperature_difference],

    "air_temp_mean_10":[air_temp_mean_10]

})

# ---------------------------------------------------
# MACHINE INPUT SUMMARY
# ---------------------------------------------------

st.subheader("Current Machine Parameters")

col1,col2,col3,col4,col5 = st.columns(5)

col1.metric("Air Temp",f"{air_temp:.1f} K")

col2.metric("Process Temp",f"{process_temp:.1f} K")

col3.metric("RPM",rpm)

col4.metric("Torque",f"{torque:.1f}")

col5.metric("Tool Wear",tool_wear)

st.divider()

# ---------------------------------------------------
# ENGINEERED FEATURES
# ---------------------------------------------------

st.subheader("Automatically Generated Features")

feature_table = pd.DataFrame({

"Feature":[
"RPM × Torque",
"Load Density",
"Load Stress",
"Temperature Ratio",
"Temperature Difference"
],

"Value":[
round(rpm_torque_interaction,2),
round(load_density,3),
round(load_stress,2),
round(temperature_ratio,3),
round(temperature_difference,2)
]

})

st.dataframe(
feature_table,
use_container_width=True,
hide_index=True
)

st.divider()

# ---------------------------------------------------
# PREDICTION
# ---------------------------------------------------

if predict:

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        machine_status = "⚠ HIGH RISK"
        color = "red"
    else:
        machine_status = "✅ HEALTHY"
        color = "green"

    # ---------------------------------------------------
    # KPI CARDS
    # ---------------------------------------------------

    st.header("Prediction Summary")

    kpi1, kpi2, kpi3 = st.columns(3)

    kpi1.metric(
        "Failure Probability",
        f"{probability*100:.2f}%"
    )

    kpi2.metric(
        "Prediction",
        machine_status
    )

    kpi3.metric(
        "ML Model",
        "LightGBM"
    )

    st.divider()

    # ---------------------------------------------------
    # RISK INDICATOR
    # ---------------------------------------------------

    st.subheader("Machine Risk Indicator")

    st.progress(float(probability))

    if probability < 0.20:

        st.success("🟢 Low Risk")

    elif probability < 0.40:

        st.info("🟡 Moderate Risk")

    elif probability < 0.70:

        st.warning("🟠 High Risk")

    else:

        st.error("🔴 Critical Risk")

    st.write(f"Estimated Failure Probability : **{probability*100:.2f}%**")

    st.divider()

    # ---------------------------------------------------
    # MACHINE HEALTH REPORT
    # ---------------------------------------------------

    st.subheader("Machine Health Report")

    report = pd.DataFrame({

        "Parameter":[

            "Machine Status",

            "Failure Probability",

            "Air Temperature",

            "Process Temperature",

            "Rotational Speed",

            "Torque",

            "Tool Wear"

        ],

        "Value":[

            machine_status,

            f"{probability*100:.2f}%",

            air_temp,

            process_temp,

            rpm,

            torque,

            tool_wear

        ]

    })

    st.dataframe(
        report,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # ---------------------------------------------------
    # SENSOR VISUALIZATION
    # ---------------------------------------------------

    st.subheader("Sensor Values")

    sensor_df = pd.DataFrame({

        "Sensor":[

            "Air Temp",

            "Process Temp",

            "RPM",

            "Torque",

            "Tool Wear"

        ],

        "Value":[

            air_temp,

            process_temp,

            rpm,

            torque,

            tool_wear

        ]

    })

    st.bar_chart(
        sensor_df.set_index("Sensor")
    )

    st.divider()

    # ---------------------------------------------------
    # ENGINEERED FEATURE VISUALIZATION
    # ---------------------------------------------------

    st.subheader("Engineered Features")

    engineered_df = pd.DataFrame({

        "Feature":[

            "RPM × Torque",

            "Load Density",

            "Load Stress",

            "Temperature Ratio",

            "Temperature Difference"

        ],

        "Value":[

            rpm_torque_interaction,

            load_density,

            load_stress,

            temperature_ratio,

            temperature_difference

        ]

    })

    st.bar_chart(
        engineered_df.set_index("Feature")
    )

    st.divider()

    # ---------------------------------------------------
    # MAINTENANCE RECOMMENDATION
    # ---------------------------------------------------

    st.subheader("Maintenance Recommendation")

    if prediction == 1:

        st.error("""
Immediate maintenance is recommended.

• Inspect spindle and bearings

• Check motor condition

• Verify torque transmission

• Inspect tool wear

• Reduce operational load

• Schedule preventive maintenance immediately
""")

    else:

        st.success("""
Machine is operating normally.

Recommended actions:

• Continue production

• Follow preventive maintenance schedule

• Monitor tool wear periodically

• Continue sensor monitoring
""")

    st.divider()

# ---------------------------------------------------
# DOWNLOAD REPORT
# ---------------------------------------------------

    st.subheader("Prediction Report")

    download_df = pd.DataFrame({

        "Parameter":[
            "Air Temperature (K)",
            "Process Temperature (K)",
            "Rotational Speed (RPM)",
            "Torque (Nm)",
            "Tool Wear (min)",
            "Failure Probability",
            "Prediction"
        ],

        "Value":[
            air_temp,
            process_temp,
            rpm,
            torque,
            tool_wear,
            f"{probability*100:.2f}%",
            machine_status
        ]

    })

    csv = download_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Prediction Report",
        data=csv,
        file_name="prediction_report.csv",
        mime="text/csv",
        use_container_width=True
    )

    st.divider()

    # ---------------------------------------------------
    # ABOUT MODEL
    # ---------------------------------------------------

    st.subheader("Model Information")

    info1, info2 = st.columns(2)

    with info1:

        st.info("""
### Machine Learning Model

- LightGBM Classifier
- Stratified 5-Fold Cross Validation
- SMOTE for Class Imbalance
- Binary Classification
""")

    with info2:

        st.info("""
### Engineered Features

- RPM × Torque
- Load Density
- Load Stress
- Temperature Ratio
- Temperature Difference
""")

    st.divider()

    # ---------------------------------------------------
    # FEATURE IMPORTANCE (PROJECT SUMMARY)
    # ---------------------------------------------------

    st.subheader("Important Features Used by the Model")

    importance = pd.DataFrame({

        "Feature":[
            "RPM × Torque",
            "Rotational Speed",
            "Load Stress",
            "Torque",
            "Load Density",
            "Tool Wear",
            "Temperature Ratio",
            "Temperature Difference",
            "Air Temperature"
        ],

        "Relative Importance":[
            100,
            92,
            86,
            81,
            74,
            66,
            52,
            48,
            44
        ]

    })

    st.bar_chart(
        importance.set_index("Feature")
    )

    st.divider()

    # ---------------------------------------------------
    # FINAL CONCLUSION
    # ---------------------------------------------------

    st.success(
        "Prediction completed successfully. "
        "The dashboard analyzed the machine telemetry, "
        "generated engineered features, and evaluated "
        "machine health using the trained LightGBM model."
    )

else:

    st.info(
        "👈 Enter machine sensor values in the sidebar and click "
        "'Predict Machine Health' to analyze the machine."
    )

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.divider()

st.markdown(
"""
### 📌 Project Overview

This dashboard demonstrates an end-to-end **Predictive Maintenance System**
developed during the **Infotact Data Science & Machine Learning Internship**.

### Workflow

Industrial IoT Telemetry

⬇

Signal Processing

⬇

Feature Engineering

⬇

Contextual Data Fusion

⬇

LightGBM Model

⬇

Failure Prediction

⬇

Maintenance Recommendation

---

**Dataset:** AI4I 2020 Predictive Maintenance Dataset

**Libraries Used**

- Python
- Pandas
- NumPy
- Scikit-learn
- LightGBM
- Imbalanced-learn (SMOTE)
- Streamlit

---

**Developed by:** Aarav Shah

**Internship:** Infotact Solutions
"""
)