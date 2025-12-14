import subprocess
import json
from config import HOTSPOT_CC_THRESHOLD

def extract_hotspots(file_path):
    cmd = f'python -m radon cc -s -j "{file_path}"'
    proc = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    if not proc.stdout.strip():
        return []

    data = json.loads(proc.stdout)
    funcs = []

    for _, items in data.items():
        for it in items:
            if it["type"] == "method" and it["complexity"] >= HOTSPOT_CC_THRESHOLD:
                funcs.append({
                    "function": it["name"],
                    "line": it["lineno"],
                    "complexity": it["complexity"]
                })

    return sorted(funcs, key=lambda x: -x["complexity"])