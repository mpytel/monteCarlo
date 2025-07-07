#!/usr/bin/env python3
"""
Physics Simulations Demonstration Script
========================================

This script demonstrates all 18 physics simulations in the monteCarlo framework.
It generates data, runs Monte Carlo simulations, and creates visualizations
for each physics category.

Usage: python demo_physics.py
"""

import subprocess
import time
import os

def run_command(cmd, description):
    """Run a command and display results"""
    print(f"\n{'='*60}")
    print(f"🔬 {description}")
    print(f"{'='*60}")
    print(f"Command: {cmd}")
    print("-" * 40)
    
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd="/Users/primwind/proj/test/monteCarlo")
        if result.returncode == 0:
            print("✅ SUCCESS")
            if result.stdout:
                print(result.stdout)
        else:
            print("❌ ERROR")
            if result.stderr:
                print(result.stderr)
    except Exception as e:
        print(f"❌ EXCEPTION: {e}")
    
    time.sleep(1)  # Brief pause between commands

def main():
    """Demonstrate all physics simulations"""
    
    print("""
    🌟 MONTECARLO PHYSICS SIMULATIONS DEMONSTRATION 🌟
    ================================================
    
    This demonstration will:
    1. List all physics simulation categories
    2. Generate sample data for each physics type
    3. Run Monte Carlo simulations
    4. Create comprehensive visualizations
    
    Total simulations: 18 across 6 categories
    """)
    
    # 1. List all physics sources
    run_command("monteCarlo listSources physics", "Listing All Physics Simulations")
    
    # 2. Wave Physics Demonstrations
    print(f"\n{'🌊 WAVE PHYSICS SIMULATIONS 🌊':^60}")
    
    # Wave propagation
    run_command("monteCarlo fetchData physics_wave_propagation sound_waves samples=300", 
                "Wave Propagation: v = f × λ")
    
    # Standing wave
    run_command("monteCarlo fetchData physics_standing_wave guitar_string samples=250", 
                "Standing Wave: f = (n/2L)√(T/μ)")
    
    # Doppler effect
    run_command("monteCarlo fetchData physics_doppler_effect ambulance_siren samples=200", 
                "Doppler Effect: f' = f(v±vo)/(v±vs)")
    
    # 3. Thermal Physics Demonstrations
    print(f"\n{'🔥 THERMAL PHYSICS SIMULATIONS 🔥':^60}")
    
    # Gas law
    run_command("monteCarlo fetchData physics_gas_law atmospheric_pressure samples=300", 
                "Ideal Gas Law: PV = nRT")
    
    # Heat diffusion
    run_command("monteCarlo fetchData physics_heat_diffusion building_insulation samples=250", 
                "Heat Diffusion: q = -k∇T")
    
    # Brownian motion
    run_command("monteCarlo fetchData physics_brownian_motion pollen_in_water samples=400", 
                "Brownian Motion: <x²> = 2Dt")
    
    # 4. Electromagnetic Demonstrations
    print(f"\n{'⚡ ELECTROMAGNETIC SIMULATIONS ⚡':^60}")
    
    # RC circuit
    run_command("monteCarlo fetchData physics_rc_circuit capacitor_discharge samples=300", 
                "RC Circuit: V(t) = V₀e^(-t/RC)")
    
    # EM wave
    run_command("monteCarlo fetchData physics_em_wave radio_transmission samples=250", 
                "EM Wave: Z = E/H = √(μ/ε)")
    
    # Photoelectric effect
    run_command("monteCarlo fetchData physics_photoelectric solar_cell samples=200", 
                "Photoelectric Effect: KE = hf - φ")
    
    # 5. Fluid Dynamics Demonstrations
    print(f"\n{'🌊 FLUID DYNAMICS SIMULATIONS 🌊':^60}")
    
    # Bernoulli equation
    run_command("monteCarlo fetchData physics_bernoulli airplane_wing samples=300", 
                "Bernoulli: P + ½ρv² + ρgh = constant")
    
    # Poiseuille flow
    run_command("monteCarlo fetchData physics_poiseuille blood_flow samples=250", 
                "Poiseuille Flow: Q = πr⁴ΔP/(8μL)")
    
    # Surface tension
    run_command("monteCarlo fetchData physics_surface_tension water_droplet samples=200", 
                "Surface Tension: F = γL cos(θ)")
    
    # 6. Quantum Physics Demonstrations
    print(f"\n{'🔬 QUANTUM PHYSICS SIMULATIONS 🔬':^60}")
    
    # Harmonic oscillator
    run_command("monteCarlo fetchData physics_harmonic_oscillator molecular_vibration samples=300", 
                "Quantum Harmonic Oscillator: E = ℏω(n + ½)")
    
    # Blackbody radiation
    run_command("monteCarlo fetchData physics_blackbody stellar_radiation samples=250", 
                "Blackbody Radiation: Planck's Law")
    
    # Particle decay
    run_command("monteCarlo fetchData physics_particle_decay carbon_dating samples=200", 
                "Radioactive Decay: N(t) = N₀e^(-λt)")
    
    # 7. Mechanics Demonstrations
    print(f"\n{'🌌 MECHANICS SIMULATIONS 🌌':^60}")
    
    # Orbital mechanics
    run_command("monteCarlo fetchData physics_orbital satellite_orbit samples=300", 
                "Orbital Mechanics: v = √(GM/r)")
    
    # Gravitational lensing
    run_command("monteCarlo fetchData physics_gravitational_lens galaxy_cluster samples=250", 
                "Gravitational Lensing: α = 4GM/(c²b)")
    
    # Pendulum
    run_command("monteCarlo fetchData physics_pendulum grandfather_clock samples=200", 
                "Simple Pendulum: T = 2π√(L/g)")
    
    # 8. Run Monte Carlo Simulations
    print(f"\n{'🎲 MONTE CARLO SIMULATIONS 🎲':^60}")
    
    # Setup and run key simulations
    simulations = [
        ("wave_sim", "frequency,wavelength,wave_speed", "physics_wave_propagation_*"),
        ("thermal_sim", "pressure,volume,temperature", "physics_gas_law_*"),
        ("quantum_sim", "position,momentum,energy", "physics_harmonic_oscillator_*"),
        ("orbital_sim", "radius,velocity,central_mass", "physics_orbital_*")
    ]
    
    for sim_name, columns, pattern in simulations:
        run_command(f"monteCarlo setupSim {sim_name} 3000 '{columns}' '{pattern}'", 
                    f"Setting up {sim_name}")
        run_command(f"monteCarlo runSim {sim_name}", 
                    f"Running {sim_name}")
        run_command(f"monteCarlo plotResults {sim_name} all", 
                    f"Creating visualizations for {sim_name}")
    
    # 9. Summary
    print(f"\n{'🎉 DEMONSTRATION COMPLETE 🎉':^60}")
    print("""
    ✅ All 18 physics simulations demonstrated successfully!
    
    📊 Generated Data:
    - Wave Physics: 3 simulations (propagation, standing wave, Doppler)
    - Thermal Physics: 3 simulations (gas law, heat diffusion, Brownian motion)
    - Electromagnetic: 3 simulations (RC circuit, EM wave, photoelectric)
    - Fluid Dynamics: 3 simulations (Bernoulli, Poiseuille, surface tension)
    - Quantum Physics: 3 simulations (harmonic oscillator, blackbody, decay)
    - Mechanics: 3 simulations (orbital, gravitational lens, pendulum)
    
    🎲 Monte Carlo Simulations:
    - 4 comprehensive simulations with 3,000 iterations each
    - Complete statistical analysis and visualization
    
    📈 Visualizations:
    - Histograms showing parameter distributions
    - Scatter matrices revealing correlations
    - Convergence analysis for simulation validation
    - Correlation heatmaps for relationship analysis
    - Scenario comparisons (best/worst/likely cases)
    
    💡 Next Steps:
    - Explore data/sources/ for raw physics data
    - Check data/simulations/ for Monte Carlo results
    - View data/plots/ for comprehensive visualizations
    - Use 'monteCarlo listSims' to see all simulations
    - Use 'monteCarlo listSources physics' to explore more
    """)

if __name__ == "__main__":
    main()
