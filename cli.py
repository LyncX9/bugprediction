import sys
from app.model import model
from app.features import build_feature_vector
from app.hotspot import extract_hotspots
from config import BUG_THRESHOLD

if len(sys.argv) < 2:
    print("Usage: bugpredict <file.py>")
    sys.exit(1)

file_path = sys.argv[1]

hotspots = extract_hotspots(file_path)

stats = {
    "radon_total_complexity": sum(h["complexity"] for h in hotspots),
    "radon_num_items": len(hotspots),
    "pylint_msgs_count": 0,
    "pylint_rc": 0,
    "bandit_issues_count": 0,
    "bandit_rc": 0,
}

X = build_feature_vector(stats)
proba = model.predict_proba(X)[0][1]
label = "BUG-FIX LIKELY" if proba >= BUG_THRESHOLD else "NON-BUG"

print("\n=== Bug Prediction ===")
print("File:", file_path)
print("Label:", label)
print("Probability:", round(float(proba), 4))

if hotspots:
    print("\n⚠️ Risky Functions:")
    for h in hotspots[:10]:
        print(f"- {h['function']} (line {h['line']}, CC={h['complexity']})")
else:
    print("\nNo high-risk functions detected.")
print("\nDone.")