# Celestial Quantum Singularity Intelligence (CQSI)

> **"Security is not a binary state. It is a function of latency, cost, and physical constraints."**

## 📡 The Objective
CQSI is a sovereign **Premium Intelligence Gateway** designed to bridge the gap between raw decentralized machine intelligence (Bittensor) and high-velocity settlement rails (Solana/Base).

It rejects the standard "trusted relayer" model in favor of **Quantitative Constraint Engineering**—a design philosophy where physical limits (bandwidth, latency, compute) are treated as first-class inputs to price risk dynamically.

---

## 🏗 System Architecture

The system operates as a biological organism with three distinct components:

### 1. The Vortex Gateway (The Mouth) 🗣️
* **Function:** A sovereign API interface for institutional access to intelligence subnets.
* **Mechanism:** Enforces CNSA 2.0 compliance and manages "Lock-and-Mint" access rights via Solana NFTs.
* **Constraint:** No private key custody; users sign via wallet adapter.

### 2. The Nervous System (The Brain) 🧠
* **Function:** An off-chain Python agent implementing the **ASAS (Acceptance-Safe Atomic Settlement)** protocol.
* **Logic:**
    * **Latency Haircuts ($h(\tau)$):** Continuously monitors message propagation delays ($\tau$). As latency increases, the protocol automatically scales fees (haircuts) to price in the execution risk.
    * **Circuit Breakers:** Automatically halts outflows if:
        * Oracle price deviation ($\delta$) > 50%.
        * Latency ($\tau$) > 60 minutes.
* **Goal:** "Contained Degradation"—ensuring the system degrades gracefully under attack rather than failing catastrophically.

### 3. The Spinal Cord (The Bone) 🦴
* **Function:** Immutable smart contracts on **Solana** (Anchor) and **Base** (Solidity).
* **Physics:**
    * **Solana:** Utilizes **Merkle Mountain Ranges (MMR)** to compress state proofs into the 1232-byte transaction limit.
    * **Base:** Handles "Optimistic" finality constraints (7-day windows) by integrating "State Prover" sidecars for faster settlement.

---

## 📐 Quantitative Constraints (The Physics)

We engineer for the hard limits of reality:

| Constraint Vector | Limit | Engineering Solution | Source |
|-------------------|-------|----------------------|--------|
| **Solana MTU** | 1232 Bytes | Merkle Mountain Range (MMR) proofs | [Base Eng. Blog] |
| **Settlement Time** | 400ms vs 7 Days | Latency-Haircut Function $h(\tau)$ | [ASAS Paper] |
| **Risk Tolerance** | < 0.2% Bad Debt | Dynamic Slippage Bounds | [ASAS Paper] |

---

## 🛠️ Installation & Deployment

### Prerequisites
* Rust & Anchor CLI
* Python 3.10+ (for Nervous System)
* Solana CLI

### 1. Deploy the Spinal Cord (Solana)
```bash
cd spinal-cord
anchor build
anchor deploy
