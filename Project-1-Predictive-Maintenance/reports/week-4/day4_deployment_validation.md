# Week 4 Day 4 Report

## Objective

Validate the predictive maintenance model under different sensor noise levels to evaluate deployment robustness.

## Completed Tasks

- Loaded the trained LightGBM model
- Applied multiple synthetic noise levels to the test dataset
- Evaluated Accuracy, Precision, Recall, and F1 Score
- Compared model performance across noise levels
- Visualized the effect of increasing noise on model robustness

## Generated Output

- deployment_validation_results.csv

## Result

The model maintained stable performance at lower noise levels, while higher noise levels caused a gradual decline in prediction performance. This analysis demonstrates the robustness of the predictive maintenance model under realistic sensor disturbances.

## Conclusion

Completed deployment validation under multiple sensor noise conditions.