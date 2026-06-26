# Week 3 Day 5 Report

## Objective

Analyze final LightGBM model behaviour.

## Completed Tasks

- Generated predictions from final model
- Identified incorrect predictions
- Calculated feature importance
- Analyzed important sensor features

## Generated Files

- feature_importance.csv

## Feature Importance Findings

The most influential features were:

1. temperature_difference
2. rpm_torque_interaction
3. air_temp_mean_10
4. rotational speed
5. tool wear

Temperature-related and mechanical stress-related features contributed most to failure prediction.

UDI showed high importance due to dataset ordering effects and would be removed in production deployment.

## Conclusion

Completed model analysis before moving to next phase.