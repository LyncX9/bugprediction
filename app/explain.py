from app.model import model, FEATURES
import pandas as pd

def explain_prediction():
    clf = model.named_steps["clf"]
    imp = clf.feature_importances_
    return pd.Series(imp, index=FEATURES).sort_values(ascending=False)