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
        self.MONTHLY_PRICE_SOL = 1.0 
