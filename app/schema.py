from pydantic import BaseModel
from typing import List

class Hotspot(BaseModel):
    function: str
    line: int
    complexity: int

class PredictionResult(BaseModel):
    label: str
    probability: float
    hotspots: List[Hotspot]
    explanation: dict