import time

class RiskEngine:
    """
    Implements Acceptance-Safe Atomic Settlement (ASAS) logic.
    Source: ASAS-BridgeAMM: Trust-Minimized Cross-Chain Bridge AMM
    """

    def __init__(self):
        # --- SOVEREIGN CONFIGURATION (Feb 2026) ---
        
        # 1. RISK PARAMETERS (Derived from ASAS Paper)
        self.H_MIN = 0.003    # 0.3% Base Fee (Standard Operation)
        self.H_MAX = 0.05     # 5.0% Max Fee (Crisis Operation)
        
        # 2. TIME CONSTRAINTS (The "Pain Threshold")
        self.T_MIN = 900      # 15 Minutes (If slower than this, fee goes up)
        self.T_MAX = 14400    # 4 Hours (If slower than this, max fee applies)
        
        # 3. CIRCUIT BREAKER
        self.PRICE_DEV_THRESHOLD = 0.50 # Halt if Oracle price varies > 50%
        
        # 4. SUBSCRIPTION COST (The Revenue)
        self.MONTHLY_PRICE_SOL = 1.0  # User pays 1 SOL per month
        
        # System State
        self.system_status = "ONLINE"

    def calculate_latency(self, message_timestamp: int) -> int:
        """
        Calculates 'Tau' (Latency) - the observable delay in message propagation.
        """
        current_time = int(time.time())
        tau = current_time - message_timestamp
        return max(0, tau)

    def calculate_haircut(self, latency: int) -> float:
        """
        Calculates the dynamic haircut h(tau).
        Formula: h(tau) = h_min + (tau - T_min)/(T_max - T_min) * (h_max - h_min)
        """
        # Phase 1: Normal State (S_N)
        if latency <= self.T_MIN:
            return self.H_MIN
            
        # Phase 2: Restricted State (S_R)
        slope = (latency - self.T_MIN) / (self.T_MAX - self.T_MIN)
        haircut = self.H_MIN + slope * (self.H_MAX - self.H_MIN)
        
        # Phase 3: Halted/Critical (S_H) or max cap
        if latency >= self.T_MAX:
            return self.H_MAX
            
        return round(haircut, 5)

    def check_circuit_breaker(self, oracle_price_a: float, oracle_price_b: float) -> bool:
        """
        Checks for Price Deviation (Delta).
        If deviation > 50%, the system halts outflows.
        """
        if oracle_price_b == 0: return True 
        
        deviation = abs(oracle_price_a - oracle_price_b) / oracle_price_b
        
        if deviation > self.PRICE_DEV_THRESHOLD:
            self.system_status = "CRITICAL_HALT"
            return True 
            
        return False

# --- Self-Test (Runs when you execute the file) ---
if __name__ == "__main__":
    engine = RiskEngine()
    print(f"System Status: {engine.system_status}")
    print(f"Sovereign Price: {engine.MONTHLY_PRICE_SOL} SOL")
    print(f"Max Haircut: {engine.H_MAX * 100}%")
