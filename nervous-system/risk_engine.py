import time

class RiskEngine:
    """
    Implements Acceptance-Safe Atomic Settlement (ASAS) logic.
    Source: ASAS-BridgeAMM: Trust-Minimized Cross-Chain Bridge AMM
    """

    def __init__(self):
        # [span_5](start_span)defined in Section IV.B of ASAS paper[span_5](end_span)
        self.H_MIN = 0.003  # 0.3% Minimum Haircut (Normal Operation)
        self.H_MAX = 0.05   # 5.0% Maximum Haircut (Restricted Mode)
        
        # [span_6](start_span)defined in Section IV.B Eq (3)[span_6](end_span)
        self.T_MIN = 900    # 15 minutes (Standard finality buffer)
        self.T_MAX = 14400  # 4 hours (Max timeout before halt)
        
        # [span_7](start_span)defined in Section III.B[span_7](end_span)
        self.PRICE_DEV_THRESHOLD = 0.50 # 50% deviation triggers Circuit Breaker

    def calculate_latency(self, message_timestamp: int) -> int:
        """
        Calculates 'Tau' (Latency) - the observable delay in message propagation.
        [span_8](start_span)See Section II.D: Latency as a First-Class Risk Signal[span_8](end_span).
        """
        current_time = int(time.time())
        tau = current_time - message_timestamp
        return max(0, tau)

    def calculate_haircut(self, latency: int) -> float:
        """
        Calculates the dynamic haircut h(tau).
        Formula: h(tau) = h_min + (tau - T_min)/(T_max - T_min) * (h_max - h_min)
        [span_9](start_span)See Equation (3) in ASAS paper[span_9](end_span).
        """
        # [span_10](start_span)Phase 1: Normal State (S_N)[span_10](end_span)
        if latency <= self.T_MIN:
            return self.H_MIN
            
        # [span_11](start_span)Phase 2: Restricted State (S_R)[span_11](end_span)
        # Linearly interpolate the risk premium
        slope = (latency - self.T_MIN) / (self.T_MAX - self.T_MIN)
        haircut = self.H_MIN + slope * (self.H_MAX - self.H_MIN)
        
        # [span_12](start_span)Phase 3: Halted/Critical (S_H) or max cap[span_12](end_span)
        if latency >= self.T_MAX:
            return self.H_MAX
            
        return round(haircut, 5)

    def check_circuit_breaker(self, oracle_price_a: float, oracle_price_b: float) -> bool:
        """
        Checks for Price Deviation (Delta).
        If deviation > 50%, the system halts outflows.
        [span_13](start_span)[span_14](start_span)See Section III.B.2[span_13](end_span)[span_14](end_span).
        """
        if oracle_price_b == 0: return True # Prevent div by zero
        
        deviation = abs(oracle_price_a - oracle_price_b) / oracle_price_b
        
        if deviation > self.PRICE_DEV_THRESHOLD:
            print(f"CRITICAL: Price deviation {deviation:.2%} exceeds limit.")
            return True # TRIGGER HALT
            
        return False

# --- Quick Test ---
if __name__ == "__main__":
    engine = RiskEngine()
    
    # Simulate a fast message (10 mins)
    lat = 600
    fee = engine.calculate_haircut(lat)
    print(f"Latency: {lat}s -> Fee: {fee:.2%}") 
    # [span_15](start_span)Expect 0.30%[span_15](end_span)

    # Simulate a delayed/suspicious message (2 hours)
    lat_slow = 7200
    fee_slow = engine.calculate_haircut(lat_slow)
    print(f"Latency: {lat_slow}s -> Fee: {fee_slow:.2%}") 
    # [span_16](start_span)Expect approx 2.65% (midpoint of curve)[span_16](end_span)
