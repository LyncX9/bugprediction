import pandas as pd
from app.model import FEATURES

def build_feature_vector(stats: dict) -> pd.DataFrame:
    row = {f: float(stats.get(f, 0)) for f in FEATURES}
    return pd.DataFrame([row])