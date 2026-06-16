# Week 2 Day 2 Report

## Project

Predictive Maintenance using Industrial IoT Telemetry

---

## Objective

Perform an ablation study to compare the impact of external contextual features on machine failure prediction.

---

## Work Completed

### Baseline Model

Created a model using only internal sensor telemetry features.

Features used:

- Air temperature
- Process temperature
- Rotational speed
- Torque
- Tool wear
- Rolling statistical features

---

### Context Enhanced Model

Created another model by adding external contextual features.

Added features:

- Ambient temperature
- Load density

External context data was merged with telemetry data using timestamps.

---

## Model Used

Algorithm:

Random Forest Classifier

Target:

Machine failure

---

## Evaluation

Compared both models using:

- Accuracy
- F1 Score

Generated comparison results using ablation analysis.

---

## Conclusion

The ablation study was performed to evaluate whether adding external contextual information improves predictive maintenance performance.

The comparison between sensor-only features and sensor plus contextual features helps identify the contribution of additional data sources.

---

## Next Step

Continue with:

- Model optimization
- Feature improvement
- Final predictive maintenance pipeline