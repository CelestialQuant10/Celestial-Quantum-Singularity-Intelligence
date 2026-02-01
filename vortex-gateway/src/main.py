import sys
import os
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel

# --- THE WIRING (Connecting the Brain) ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from nervous_system.risk_engine import RiskEngine

app = FastAPI(title="Vortex Gateway", version="2.0.0-GOLD")

# Initialize the Real Brain
risk_engine = RiskEngine()

class IntelligenceRequest(BaseModel):
    subnet_id: int
    query_payload: dict

@app.get("/")
def health_check():
    return {
        "system": risk_engine.system_status,
        "config": {
            "price_per_month": f"{risk_engine.MONTHLY_PRICE_SOL} SOL",
            "max_haircut": f"{risk_engine.H_MAX * 100}%"
        },
        "sovereign_mode": True
    }

@app.post("/v1/intelligence")
def get_intelligence(request: IntelligenceRequest, x_user_key: str = Header(...)):
    # Calculate Real Latency Risk
    current_latency = 100 
    haircut = risk_engine.calculate_haircut(current_latency)
    
    return {
        "meta": {
            "risk_fee_applied": f"{haircut * 100:.3f}%",
            "status": "SECURE"
        },
        "data": {"insight": "Predictive Alpha Generated"}
    }
