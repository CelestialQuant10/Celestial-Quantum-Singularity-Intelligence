import numpy as np
from scipy.stats import gmean

class CelestialEngine:
    """
    CELESTIAL QUANTUM SINGULARITY (Classified)
    -------------------------------------------
    Architecture: Hybrid Quantum-Vortex
    Objective: Asymmetric Capital Allocation
    Logic: 3-6-9 Geometric Mean (Implosion Detection)
    """
    
    def __init__(self):
        # The Singularity Window (Tesla Standard)
        self.resonance_window = 9 

    def calculate_singularity(self, price_array):
        """
        Detects if the asset is entering a 'Singularity State' (Vacuum).
        """
        # Data Validation
        if len(price_array) < self.resonance_window:
            return {"status": "INITIALIZING", "probability": 0.0}

        # 1. QUANTUM FILTERING
        # Use Geometric Mean to filter out linear noise (entropy).
        # This reveals the "True Center" of the asset's energy.
        segment = np.array(price_array[-self.resonance_window:])
        singularity_point = gmean(segment)
        
        current_value = segment[-1]

        # 2. VORTEX CALCULATION (3-6-9)
        # Calculate deviation from the True Center.
        deviation = (current_value - singularity_point) / singularity_point

        # 3. INTELLIGENCE OUTPUT
        # If price is compressed 3% BELOW the Singularity Point -> Vacuum Implosion.
        if deviation < -0.03: 
            return {
                "signal": "ACQUIRE (IMPLOSION)", 
                "vector": "High-Probability Vacuum",
                "target_price": singularity_point
            }
        
        # If price is extended 6% ABOVE the Singularity Point -> Entropy Explosion.
        elif deviation > 0.06: 
            return {
                "signal": "LIQUIDATE (ENTROPY)", 
                "vector": "Overheated Structure",
                "target_price": singularity_point
            }
            
        return {"signal": "OBSERVE", "vector": "Equilibrium State"}
