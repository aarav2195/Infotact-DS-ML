from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

APP_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data" / "processed"
WEEK3_DIR = DATA_DIR / "week-3"
GNN_DIR = WEEK3_DIR / "gnn"

MODEL_DIR = BASE_DIR / "models"

ASSETS_DIR = APP_DIR / "assets"

NODES_FILE = (WEEK3_DIR / "final_graph_nodes.csv")

TARGETS_FILE = (WEEK3_DIR / "final_graph_targets.csv")

MODEL_COMPARISON_FILE = (GNN_DIR / "final_model_comparison.csv")

ERROR_ANALYSIS_FILE = (GNN_DIR / "final_prediction_error_analysis.csv")

PRICE_RANGE_FILE = (GNN_DIR / "final_price_range_analysis.csv")

DASHBOARD_PREDICTIONS_FILE = (GNN_DIR / "dashboard_predictions.csv")

XGB_MODEL_FILE = (MODEL_DIR / "xgboost_comparison.pkl")

BASELINE_GNN_PREDICTIONS_FILE = (GNN_DIR / "baseline_gnn_predictions.csv")

ATTENTION_GNN_PREDICTIONS_FILE = (GNN_DIR / "attention_gnn_predictions.csv")

STYLE_FILE = (ASSETS_DIR / "style.css")

EARTH_RADIUS_KM = 6371.0088

APP_TITLE = ("GeoValuation AI")

APP_SUBTITLE = ("Geospatial Real Estate Valuation & Spatial Intelligence")