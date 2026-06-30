# Week 4 Day 2 Report

## Objective

Perform Precision-Recall analysis and optimize the decision threshold of the predictive maintenance model.

## Completed Tasks

- Loaded the final LightGBM model from Week 3
- Generated failure probability predictions using `predict_proba()`
- Created Precision-Recall curve analysis
- Calculated Average Precision score
- Tested multiple decision thresholds
- Compared Precision, Recall, and F1 score
- Selected the best threshold based on F1 score

## Generated Output

Created:

data/processed/threshold_tuning_results.csv

Contains:

- Threshold values
- Precision scores
- Recall scores
- F1 scores

## Result

The threshold tuning process helps balance false alarms and missed machine failures during real-world deployment.

## Files Added

Notebook:

notebooks/13_precision_recall_threshold_tuning.ipynb

## Conclusion

Completed Precision-Recall evaluation and decision threshold optimization. The model is ready for final robustness testing.