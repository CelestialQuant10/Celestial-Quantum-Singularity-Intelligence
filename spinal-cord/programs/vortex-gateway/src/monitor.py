import time
import random
import os
import sys
import math

# --- TERMINAL MAGIC (Technique #14: Format Breaking) ---
class Console:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    PURPLE = "\033[95m"

    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

# --- THE SIMULATION ENGINE ---
def calculate_vortex_geometry(tick):
    # Simulating the Golden Ratio Vortex
    angle = tick * 0.1
    volatility = abs(math.sin(tick * 0.05))
    # The "Singularity" metric
    entropy = (math.cos(angle) * math.sin(angle * 1.618)) + 0.5
    return volatility, entropy

def draw_hud(tick, volatility, entropy, spinal_status):
    Console.clear()
    
    # 1. HEADER
    print(f"{Console.PURPLE}{Console.BOLD}")
    print(f"╔════════════════════════════════════════════════════════════╗")
    print(f"║   CELESTIAL QUANTUM SINGULARITY  //  SYSTEM MONITOR v1.0   ║")
    print(f"╚════════════════════════════════════════════════════════════╝{Console.RESET}")
    print("")

    # 2. NERVOUS SYSTEM (Sensors)
    print(f"{Console.CYAN}[ NERVOUS SYSTEM ]{Console.RESET}")
    print(f"  > Market Source:   SOL_MAINNET_BETA")
    bar_len = int(volatility * 20)
    bar = "█" * bar_len + "░" * (20 - bar_len)
    print(f"  > Volatility:      [{bar}] {volatility:.4f}")
    
    # 3. CELESTIAL CORE (Brain)
    print(f"\n{Console.YELLOW}[ CELESTIAL CORE ]{Console.RESET}")
    print(f"  > Vortex Entropy:  {entropy:.4f}")
    if entropy > 0.8:
        decision = f"{Console.GREEN}ACCUMULATE{Console.RESET}"
    elif entropy < 0.2:
        decision = f"{Console.RED}DISSIPATE{Console.RESET}"
    else:
        decision = "OBSERVE"
    print(f"  > Strategy:        {decision}")

    # 4. SPINAL CORD (On-Chain Execution)
    print(f"\n{Console.RED}[ SPINAL CORD (RUST) ]{Console.RESET}")
    print(f"  > Status:          {spinal_status}")
    print(f"  > Program ID:      Fg6PaFpoGXkYsidMpWTK6W2BeZ7FEfcYkg476zPFsLnS")
    
    # 5. DREAM STATE (Prediction)
    prediction = "STABLE" if volatility < 0.5 else "CRITICAL"
    print(f"\n{Console.PURPLE}[ DREAM STATE PREDICTION ]{Console.RESET}")
    print(f"  > T+10s Forecast:  {prediction}")

# --- THE HYBRID LOOP ---
def run_monitor():
    tick = 0
    spinal_state = "IDLE"
    
    while True:
        try:
            # Physics Calculation
            vol, ent = calculate_vortex_geometry(tick)
            
            # Simulated Spine Trigger
            if ent > 0.8 and vol < 0.7:
                spinal_state = f"{Console.GREEN}EXECUTING TX (Block {245000+tick}){Console.RESET}"
            elif vol > 0.9:
                 spinal_state = f"{Console.RED}REFLEX BLOCK (High Risk){Console.RESET}"
            else:
                spinal_state = "AWAITING SIGNAL..."

            draw_hud(tick, vol, ent, spinal_state)
            
            tick += 1
            time.sleep(0.2)
            
        except KeyboardInterrupt:
            print("\n🌌 SYSTEM SHUTDOWN.")
            sys.exit()

if __name__ == "__main__":
    run_monitor()
