from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import time
import random

# In a production environment, you would import your local modules:
# from nervous_system.risk_engine import RiskEngine
# from spinal_cord.solana_client import check_subscription

app = FastAPI(
    title="Vortex Gateway (CQSI)",
    description="Sovereign Interface for High-Fidelity Intelligence",
    version="1.0.0"
)

# --- Simulation of Internal Systems ---
# (These act as placeholders until you run the full local environment)

def query_spinal_cord(user_key: str):
    """
    Simulates checking the Solana Blockchain for a valid license.
    In real deployment, this uses `solana-py` to check the PDA account.
    """
    # Mock validation: Accept keys that start with "valid_"
    if user_key.startswith("valid_"):
        return {"active": True, "expiry": time.time() + 86400}
    return {"active": False}

def query_nervous_system():
    """
     Simonulates the Risk Engine check.
    """
    # Mock latency check
    current_latency = random.randint(100, 4000) # Random simulated latency
    if current_latency > 3600:
        raise HTTPException(status_code=503, detail="Circuit Breaker Active: High Latency")
    return {"status": "GREEN", "haircut": 0.003}

# --- The API Endpoints ---

class IntelligenceRequest(BaseModel):
    subnet_id: int
    query_payload: dict

@app.get("/")
def health_check():
    """System Status Report"""
    risk_status = query_nervous_system()
    return {
        "system": "ONLINE",
        "sovereign_mode": True,
        "risk_status": risk_status
    }

@app.post("/v1/intelligence")
def get_intelligence(request: IntelligenceRequest, x_user_key: str = Header(...)):
    """
    The Core Product:
    1. Check Risk (Nervous System)
    2. Check Payment (Spinal Cord)
    3. Deliver Intelligence
    """
    
    # 1. Risk Check
    risk_metrics = query_nervous_system()
    
    # 2. Payment/Access Check
    subscription = query_spinal_cord(x_user_key)
    if not subscription["active"]:
        raise HTTPException(status_code=402, detail="Payment Required: Subscription Invalid")
        
    # 3. Deliver Asset (Simulated Bittensor Output)
    return {
        "meta": {
            "subnet": request.subnet_id,
            "latency_haircut_applied": risk_metrics["haircut"],
            "verification": "CNSA-2.0-SIGNED"
        },
        "data": {
            "insight": "Predictive Alpha Generated",
            "confidence": 0.9997
        }
    }
