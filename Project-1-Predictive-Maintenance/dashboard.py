import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load Model
# -----------------------------

model = joblib.load(r"E:\AARAV\Infotact-DS-ML\Project-1-Predictive-Maintenance\models\final_lightgbm_model.pkl")

st.title("🛠 Predictive Maintenance Dashboard")

st.write("Enter the machine parameters below.")

# -----------------------------
# User Inputs
# -----------------------------

air_temp = st.number_input("Air Temperature (K)", value=298.0)

process_temp = st.number_input("Process Temperature (K)", value=308.0)

rpm = st.number_input("Rotational Speed (RPM)", value=1500)

torque = st.number_input("Torque (Nm)", value=40.0)

tool_wear = st.number_input("Tool Wear (min)", value=20)

# -----------------------------
# Feature Engineering
# -----------------------------

load_density = torque / 100

temperature_difference = process_temp - air_temp

temperature_ratio = process_temp / air_temp

load_stress = torque * load_density

rpm_torque_interaction = rpm * torque

tool_wear_mean_10 = tool_wear

air_temp_mean_10 = air_temp

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict"):

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

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:

        st.error("⚠ High Risk of Machine Failure")

    else:

        st.success("✅ Machine Operating Normally")

    st.metric("Failure Probability", f"{probability*100:.2f}%")

    st.progress(float(probability))

    if prediction == 1:

        st.warning("""
### Recommendation

- Schedule preventive maintenance.
- Inspect bearings and spindle.
- Check torque and RPM.
- Inspect tool wear.
""")

    else:

        st.info("""
### Recommendation

- Continue normal operation.
- Perform routine maintenance.
- Monitor machine regularly.
""")