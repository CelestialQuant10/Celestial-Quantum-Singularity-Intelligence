import time
import math
import random
import sys
import os

# --- TERMINAL QUANTUM VISUALIZER ---
class Console:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

def draw_vortex(entropy):
    """Generates a text-based vortex representation based on entropy."""
    chars = " .:-=+*#%@"
    size = int(entropy * 10)
    if size >= len(chars): size = len(chars) - 1
    return chars[size] * 10

def dashboard_loop():
    tick = 0
    sol_price = 145.00
    
    while True:
        Console.clear()
        
        # 1. GENERATE DATA (Simulating 'nervous-system' input)
        volatility = abs(math.sin(tick * 0.1))
        latency = random.randint(10, 150)
        vortex_entropy = (math.cos(tick * 0.05) * math.sin(tick * 0.1)) + 0.5
        
        # 2. DECISION LOGIC (Simulating 'celestial_core')
        status = "OBSERVING"
        color = Console.BLUE
        
        if vortex_entropy > 0.8:
            status = "⚡ EXECUTE REFLEX"
            color = Console.GREEN
            # This is where we would trigger the 'spinal-cord' Rust program
            
        elif latency > 120:
            status = "🛡️ DEFENSE BLOCK"
            color = Console.RED

        # 3. RENDER THE GLASS COCKPIT
        print(f"{Console.PURPLE}╔════════════════════════════════════════════════════╗{Console.END}")
        print(f"{Console.PURPLE}║   CELESTIAL QUANTUM SINGULARITY // SYSTEM HUD      ║{Console.END}")
        print(f"{Console.PURPLE}╚════════════════════════════════════════════════════╝{Console.END}")
        print("")
        
        # SENSORY MODULE
        print(f"{Console.CYAN}[ NERVOUS SYSTEM ]{Console.END}")
        print(f"  > LATENCY:      {latency}ms")
        print(f"  > VOLATILITY:   {volatility:.4f} φ")
        
        # CORE MODULE
        print(f"\n{Console.YELLOW}[ CELESTIAL CORE ]{Console.END}")
        print(f"  > ENTROPY:      [{draw_vortex(vortex_entropy)}] {vortex_entropy:.4f}")
        print(f"  > STRATEGY:     {color}{status}{Console.END}")

        # SPINAL MODULE (Blockchain)
        print(f"\n{Console.RED}[ SPINAL CORD (SOLANA) ]{Console.END}")
        if status == "⚡ EXECUTE REFLEX":
            print(f"  > TX SIGNATURE: {Console.GREEN}Confirmed (Block {245910 + tick}){Console.END}")
            print(f"  > GAS COST:     0.000005 SOL")
        else:
            print(f"  > STATUS:       IDLE")

        print(f"\n{Console.DARKCYAN}------------------------------------------------------{Console.END}")
        print(f"SYSTEM TIME: {time.time()}")
        
        tick += 1
        time.sleep(0.2)

if __name__ == "__main__":
    try:
        dashboard_loop()
    except KeyboardInterrupt:
        print("\n🌑 SINGULARITY HIBERNATING.")
