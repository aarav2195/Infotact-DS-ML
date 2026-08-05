# Day 3 Report – Spatial Feature Engineering

## Objective

Perform spatial feature engineering using geographical coordinates to capture neighborhood characteristics and prepare the dataset for future graph-based learning models.

---

## Tasks Completed

- Loaded the cleaned housing dataset.
- Converted latitude and longitude into radians.
- Constructed a BallTree using the Haversine distance metric.
- Identified the five nearest neighboring properties for every house.
- Calculated the nearest neighbor distance.
- Computed the average neighborhood distance.
- Engineered the Neighborhood Average Price feature.
- Calculated the Neighborhood Price Difference feature.
- Estimated local housing density within a 2 km radius.
- Created the Price Density feature.
- Analyzed spatial relationships through correlation analysis and visualizations.
- Exported the processed spatial feature dataset.

---

## Spatial Features Generated

- Nearest Neighbor Distance (km)
- Average Neighbor Distance (km)
- Neighborhood Average Price
- Neighborhood Price Difference
- Nearby Houses (2 km)
- Price Density

---

## Key Observations

- Properties located within high-value neighborhoods generally exhibit higher market prices.
- Local neighborhood characteristics provide valuable contextual information beyond traditional property attributes.
- The engineered spatial features will serve as important inputs for baseline machine learning models and future graph-based learning approaches.

---

## Deliverables

- BallTree-based neighbor search
- Haversine distance calculations
- Spatial feature engineering
- Neighborhood statistics
- Spatial feature dataset (`spatial_features.csv`)

---

## Status

**Week 1 – Day 3 completed successfully.**