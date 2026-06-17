# Week 2 Day 3 Report

## Project

Predictive Maintenance using Industrial IoT Telemetry

## Objective

The objective of Day 3 was to perform feature engineering on the context-fused industrial telemetry dataset.

The external contextual features generated during data fusion were enhanced by creating additional derived features to improve machine failure prediction capability.

---

## Dataset Used

Input Dataset:

- context_fused_dataset.csv

This dataset contains:

- Internal sensor telemetry data
- Rolling statistical features
- External contextual information

External features included:

- Ambient Temperature
- Load Density

---

## Feature Engineering Performed

### 1. Temperature Difference Feature

Created a new feature by calculating the difference between process temperature and air temperature.

Purpose:

To identify machine thermal stress conditions.

Formula:

Process Temperature - Air Temperature


---

### 2. Temperature Ratio Feature

Created a temperature ratio feature.

Purpose:

To capture relative temperature changes during machine operation.


---

### 3. Load Stress Feature

Created a load stress feature by combining torque and load density.

Purpose:

To represent the effect of external load conditions on machine performance.


---

### 4. RPM-Torque Interaction Feature

Created an interaction feature between rotational speed and torque.

Purpose:

To represent machine operational intensity.


---

### 5. Contextual Rolling Features

Generated rolling window features for external contextual data.

Created:

- Ambient Temperature Rolling Mean
- Load Density Rolling Mean


Window size used:

10 operational records

Purpose:

To smooth environmental variations and capture operational trends.

---

## Data Processing

Steps performed:

- Loaded context fused dataset
- Generated derived features
- Applied rolling window calculations
- Removed missing values created by rolling operations
- Saved final feature dataset

---

## Final Dataset Contains

- Original telemetry features
- Rolling sensor features
- External contextual features
- Derived interaction features


---

## Conclusion

Contextual feature engineering was successfully completed.

The final enriched dataset combines machine telemetry information with environmental and operational context.

This dataset is ready for further machine learning model development and evaluation.