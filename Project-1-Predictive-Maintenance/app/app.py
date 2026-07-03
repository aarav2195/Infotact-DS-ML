import sys
from pathlib import Path

#Add src directory to Python Path
project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(project_root / "src"))

from inference import predict_machine_failure
from utils import get_recommendation

MODEL_PATH = project_root / "models" / "final_lightgbm_model.pkl"
DATA_PATH = project_root / "data" / "processed" / "model_ready_dataset.csv"

results = predict_machine_failure(MODEL_PATH,DATA_PATH)

print("=" * 60)
print("    Predictive Maintenance Inference System")
print("=" * 60)

prediction = results.loc[0, "Prediction"]
confidence = results.loc[0, "Failure Probability"] * 100

status = "Machine failure" if prediction == 1 else "Normal Operation"

print(f"Machine Status       : {status}")
print(f"Prediction           : {prediction}")
print(f"Failure Probability  : {confidence:.2f}%")
print(f"Recommendation       : {get_recommendation(prediction)}")

print("=" * 60)
print("Inference completed successfully.")
print("=" * 60)