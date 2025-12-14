import joblib
from config import MODEL_PATH, PREPROC_PATH

model = joblib.load(MODEL_PATH)
preproc = joblib.load(PREPROC_PATH)

FEATURES = list(preproc.feature_names_in_)