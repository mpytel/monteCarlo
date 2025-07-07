# Physics Simulations in monteCarlo Framework

**Version 0.1.0** - *18 Highly Correlated Three-Variable Physics Simulations*

This document provides comprehensive documentation for all 18 physics simulations implemented in the monteCarlo framework. Each simulation represents a fundamental physics relationship with strong three-variable correlations, perfect for Monte Carlo analysis.

---

## Table of Contents

1. [Overview](#overview)
2. [Wave Physics](#wave-physics)
3. [Thermal Physics](#thermal-physics)
4. [Electromagnetic Physics](#electromagnetic-physics)
5. [Fluid Dynamics](#fluid-dynamics)
6. [Quantum Physics](#quantum-physics)
7. [Mechanics](#mechanics)
8. [Usage Examples](#usage-examples)
9. [Parameter Ranges](#parameter-ranges)
10. [Correlation Analysis](#correlation-analysis)

---

## Overview

The physics category contains 18 simulations across 6 subcategories, each implementing well-known physics equations with realistic parameter ranges. These simulations demonstrate:

- **Deterministic relationships** with parameter randomness
- **Strong correlations** between variables (perfect for Monte Carlo analysis)
- **Realistic parameter ranges** based on real-world applications
- **Comprehensive metadata** including units and equations

### Philosophy

Unlike other data sources in monteCarlo that explore inherent randomness, physics simulations explore **parameter uncertainty** within **deterministic relationships**. The randomness comes from:
- Measurement uncertainty
- Material property variation
- Environmental conditions
- Quantum uncertainty (where applicable)

---

## 🌊 Wave Physics

### 1. Wave Propagation
**Equation**: `v = f × λ` (velocity = frequency × wavelength)

```bash
monteCarlo fetchData physics_wave_propagation sound_waves samples=1000
```

**Variables**:
- `frequency`: 20-20,000 Hz (audio range)
- `wavelength`: 0.01-17 m
- `wave_speed`: Calculated from v = f × λ

**Applications**: Sound waves, light waves, water waves, seismic waves

**Correlation**: Perfect positive correlation between all three variables

### 2. Standing Wave
**Equation**: `f = (n/2L)√(T/μ)` (frequency depends on length, tension, density)

```bash
monteCarlo fetchData physics_standing_wave guitar_string samples=1000
```

**Variables**:
- `length`: 0.1-2.0 m (string length)
- `tension`: 10-1,000 N
- `linear_density`: 0.001-0.01 kg/m
- `frequency`: Calculated from standing wave equation

**Applications**: Musical instruments, cable vibrations, resonance analysis

**Correlation**: Inverse relationship with length, square root with tension

### 3. Doppler Effect
**Equation**: `f' = f(v±vo)/(v±vs)` (observed frequency with relative motion)

```bash
monteCarlo fetchData physics_doppler_effect ambulance_siren samples=1000
```

**Variables**:
- `source_velocity`: -50 to 50 m/s
- `observer_velocity`: -30 to 30 m/s
- `observed_frequency`: Calculated from Doppler equation

**Applications**: Radar detection, medical ultrasound, astronomy, emergency vehicles

**Correlation**: Linear relationship with relative velocities

---

## 🔥 Thermal Physics

### 4. Ideal Gas Law
**Equation**: `PV = nRT` (pressure, volume, temperature relationship)

```bash
monteCarlo fetchData physics_gas_law atmospheric_pressure samples=1000
```

**Variables**:
- `pressure`: Calculated from PV = nRT
- `volume`: 0.001-0.1 m³
- `temperature`: 200-400 K
- `n_moles`: 0.1-10 mol

**Applications**: Weather systems, engine combustion, gas storage, atmospheric science

**Correlation**: Inverse P-V relationship, linear P-T and V-T relationships

### 5. Heat Diffusion
**Equation**: `q = -k∇T` (Fourier's law of heat conduction)

```bash
monteCarlo fetchData physics_heat_diffusion building_insulation samples=1000
```

**Variables**:
- `temperature_gradient`: 1-100 K/m
- `thermal_conductivity`: 0.1-400 W/(m·K)
- `heat_flux`: Calculated from q = k∇T

**Applications**: Building insulation, CPU cooling, geothermal systems, cooking

**Correlation**: Perfect linear relationship between heat flux and gradient

### 6. Brownian Motion
**Equation**: `<x²> = 2Dt` (Einstein relation for diffusion)

```bash
monteCarlo fetchData physics_brownian_motion pollen_in_water samples=1000
```

**Variables**:
- `displacement`: Calculated from √(2Dt)
- `time`: 1-3600 s
- `diffusion_coefficient`: 1e-12 to 1e-9 m²/s

**Applications**: Particle tracking, molecular diffusion, financial modeling

**Correlation**: Square root relationship with time

---

## ⚡ Electromagnetic Physics

### 7. RC Circuit
**Equation**: `V(t) = V₀e^(-t/RC)` (exponential decay in RC circuits)

```bash
monteCarlo fetchData physics_rc_circuit capacitor_discharge samples=1000
```

**Variables**:
- `voltage`: Calculated from exponential decay
- `current`: V/R
- `time_constant`: RC
- `resistance`: 100-10,000 Ω
- `capacitance`: 1e-9 to 1e-3 F

**Applications**: Timing circuits, filters, camera flash, power supplies

**Correlation**: Exponential decay relationship

### 8. Electromagnetic Wave
**Equation**: `Z = E/H = √(μ/ε)` (wave impedance)

```bash
monteCarlo fetchData physics_em_wave radio_transmission samples=1000
```

**Variables**:
- `electric_field`: 0.1-100 V/m
- `magnetic_field`: Calculated from E/Z
- `wave_impedance`: √(μ/ε)

**Applications**: Radio transmission, microwave systems, optical fibers, antennas

**Correlation**: Constant ratio in free space (377Ω)

### 9. Photoelectric Effect
**Equation**: `KE = hf - φ` (Einstein's photoelectric equation)

```bash
monteCarlo fetchData physics_photoelectric solar_cell samples=1000
```

**Variables**:
- `photon_energy`: 0.5-10 eV
- `work_function`: 1-6 eV
- `kinetic_energy`: max(0, hf - φ)

**Applications**: Solar cells, photomultipliers, image sensors, photodiodes

**Correlation**: Linear above threshold, zero below threshold

---

## 🌊 Fluid Dynamics

### 10. Bernoulli Equation
**Equation**: `P + ½ρv² + ρgh = constant` (energy conservation in fluids)

```bash
monteCarlo fetchData physics_bernoulli airplane_wing samples=1000
```

**Variables**:
- `pressure`: Static pressure component
- `velocity`: 0.1-20 m/s
- `height`: 0-100 m
- `total_pressure`: Constant total energy

**Applications**: Aircraft design, venturi meters, pitot tubes, water flow

**Correlation**: Energy conservation relationship

### 11. Poiseuille Flow
**Equation**: `Q = πr⁴ΔP/(8μL)` (laminar flow in pipes)

```bash
monteCarlo fetchData physics_poiseuille blood_flow samples=1000
```

**Variables**:
- `flow_rate`: Calculated from Poiseuille equation
- `pressure_drop`: 100-10,000 Pa
- `pipe_radius`: 0.001-0.1 m
- `viscosity`: 0.001-0.1 Pa·s

**Applications**: Blood flow, oil pipelines, microfluidics, hydraulic systems

**Correlation**: Fourth power dependence on radius

### 12. Surface Tension
**Equation**: `F = γL cos(θ)` (wetting force from surface tension)

```bash
monteCarlo fetchData physics_surface_tension water_droplet samples=1000
```

**Variables**:
- `contact_angle`: 0-π rad
- `surface_energy`: 0.02-0.08 N/m
- `wetting_force`: Calculated from F = γL cos(θ)

**Applications**: Water droplets, soap bubbles, capillary action, wetting phenomena

**Correlation**: Cosine dependence on contact angle

---

## 🔬 Quantum Physics

### 13. Quantum Harmonic Oscillator
**Equation**: `E = ℏω(n + ½)` (quantized energy levels)

```bash
monteCarlo fetchData physics_harmonic_oscillator molecular_vibration samples=1000
```

**Variables**:
- `position`: From uncertainty principle
- `momentum`: From uncertainty principle
- `energy`: ℏω(n + ½)
- `quantum_number`: 0-9

**Applications**: Molecular vibrations, phonon modes, laser cavities, atomic traps

**Correlation**: Quantized energy levels, uncertainty principle

### 14. Blackbody Radiation
**Equation**: `B(λ,T) = 2hc²/λ⁵ × 1/(e^(hc/λkT)-1)` (Planck's law)

```bash
monteCarlo fetchData physics_blackbody stellar_radiation samples=1000
```

**Variables**:
- `temperature`: 300-6000 K
- `wavelength`: 1e-7 to 1e-5 m
- `intensity`: Calculated from Planck's law

**Applications**: Stellar radiation, thermal imaging, incandescent bulbs, cosmic background

**Correlation**: Peak wavelength inversely proportional to temperature

### 15. Radioactive Decay
**Equation**: `N(t) = N₀e^(-λt)` (exponential decay)

```bash
monteCarlo fetchData physics_particle_decay carbon_dating samples=1000
```

**Variables**:
- `initial_count`: 1,000-1,000,000 particles
- `time`: Variable based on decay constant
- `decay_constant`: 1e-8 to 1e-3 s⁻¹
- `remaining_count`: N₀e^(-λt)

**Applications**: Carbon dating, nuclear reactors, medical isotopes, cosmic rays

**Correlation**: Exponential decay with characteristic half-life

---

## 🌌 Mechanics

### 16. Orbital Mechanics
**Equation**: `v = √(GM/r)` (orbital velocity)

```bash
monteCarlo fetchData physics_orbital satellite_orbit samples=1000
```

**Variables**:
- `radius`: 1e6 to 1e12 m
- `velocity`: Calculated from √(GM/r)
- `central_mass`: 1e20 to 2e30 kg
- `orbital_period`: 2πr/v

**Applications**: Satellite orbits, planetary motion, space stations, asteroid trajectories

**Correlation**: Inverse square root relationship with radius

### 17. Gravitational Lensing
**Equation**: `α = 4GM/(c²b)` (deflection angle)

```bash
monteCarlo fetchData physics_gravitational_lens galaxy_cluster samples=1000
```

**Variables**:
- `deflection_angle`: Calculated from lensing equation
- `mass`: 1e30 to 1e42 kg
- `impact_parameter`: 1e15 to 1e20 m

**Applications**: Galaxy clusters, black holes, dark matter detection, quasar imaging

**Correlation**: Inverse relationship with impact parameter

### 18. Simple Pendulum
**Equation**: `T = 2π√(L/g)` (period of oscillation)

```bash
monteCarlo fetchData physics_pendulum grandfather_clock samples=1000
```

**Variables**:
- `length`: 0.1-10 m
- `period`: Calculated from 2π√(L/g)
- `gravitational_acceleration`: 9.7-9.9 m/s²

**Applications**: Clocks, seismometers, Foucault pendulums, metronomes

**Correlation**: Square root relationship with length

---

## Usage Examples

### Basic Data Generation
```bash
# Generate wave propagation data
monteCarlo fetchData physics_wave_propagation sound_waves samples=500

# Generate gas law data
monteCarlo fetchData physics_gas_law atmospheric_pressure samples=300

# Generate quantum oscillator data
monteCarlo fetchData physics_harmonic_oscillator molecular_vibration samples=400
```

### Monte Carlo Simulations
```bash
# Setup simulation with wave data
monteCarlo setupSim wave_analysis 5000 'frequency,wavelength,wave_speed' 'physics_wave_propagation_*'

# Run the simulation
monteCarlo runSim wave_analysis

# Create all visualizations
monteCarlo plotResults wave_analysis all
```

### Comprehensive Analysis
```bash
# Generate multiple physics datasets
monteCarlo fetchData physics_gas_law atmospheric_pressure samples=500
monteCarlo fetchData physics_orbital satellite_orbit samples=500
monteCarlo fetchData physics_photoelectric solar_cell samples=500

# Setup comparative simulations
monteCarlo setupSim thermal_analysis 3000 'pressure,volume,temperature' 'physics_gas_law_*'
monteCarlo setupSim orbital_analysis 3000 'radius,velocity,central_mass' 'physics_orbital_*'
monteCarlo setupSim quantum_analysis 3000 'photon_energy,work_function,kinetic_energy' 'physics_photoelectric_*'

# Run all simulations
monteCarlo runSim thermal_analysis
monteCarlo runSim orbital_analysis
monteCarlo runSim quantum_analysis

# Generate comprehensive visualizations
monteCarlo plotResults thermal_analysis all
monteCarlo plotResults orbital_analysis all
monteCarlo plotResults quantum_analysis all
```

---

## Parameter Ranges

### Realistic Ranges by Category

| Category | Typical Parameter Ranges | Real-World Context |
|----------|-------------------------|-------------------|
| **Wave** | f: 20-20kHz, λ: 1cm-17m | Audio frequencies, room acoustics |
| **Thermal** | T: 200-400K, P: 1-10⁵ Pa | Atmospheric to industrial conditions |
| **EM** | E: 0.1-100 V/m, f: 1-10¹⁵ Hz | Radio to optical frequencies |
| **Fluid** | v: 0.1-20 m/s, r: 1mm-10cm | Biological to industrial flow |
| **Quantum** | E: 0.5-10 eV, n: 0-9 | Molecular to atomic scales |
| **Mechanics** | r: 1Mm-1Tm, M: 10²⁰-10⁴² kg | Earth orbit to galactic scales |

---

## Correlation Analysis

### Expected Correlation Strengths

| Simulation | Primary Correlation | Strength | Type |
|------------|-------------------|----------|------|
| Wave Propagation | v ↔ f×λ | 1.00 | Perfect Linear |
| Gas Law | P ↔ T/V | 0.95+ | Strong Inverse |
| RC Circuit | V ↔ e^(-t/RC) | 0.90+ | Exponential |
| Orbital | v ↔ √(M/r) | 0.95+ | Power Law |
| Photoelectric | KE ↔ (hf-φ) | 0.98+ | Threshold Linear |
| Poiseuille | Q ↔ r⁴ | 0.99+ | Fourth Power |

### Monte Carlo Benefits

Physics simulations are ideal for Monte Carlo analysis because:

1. **Deterministic Core**: Known equations provide validation
2. **Parameter Uncertainty**: Real-world variation in inputs
3. **Strong Correlations**: Clear relationships to discover
4. **Realistic Ranges**: Based on actual applications
5. **Educational Value**: Demonstrates physics principles

---

## Advanced Features

### Metadata Integration
Each simulation includes:
- **Equation strings**: For display and documentation
- **Unit specifications**: Proper dimensional analysis
- **Application examples**: Real-world context
- **Randomness assessment**: Expected correlation levels

### Extensibility
The framework supports:
- **Custom parameter ranges**: Modify for specific applications
- **Additional physics**: Easy to add new simulations
- **Coupled systems**: Multi-physics simulations
- **Validation tools**: Compare with analytical solutions

---

## Conclusion

The 18 physics simulations provide a comprehensive foundation for exploring deterministic relationships with parameter uncertainty. They demonstrate the power of Monte Carlo methods in understanding how measurement uncertainty and parameter variation affect physical systems.

**Key Benefits**:
- ✅ **Educational**: Learn physics through simulation
- ✅ **Realistic**: Based on real-world applications  
- ✅ **Comprehensive**: Covers major physics domains
- ✅ **Validated**: Known equations provide ground truth
- ✅ **Extensible**: Easy to modify and expand

**Perfect for**:
- Engineering uncertainty analysis
- Physics education and research
- Monte Carlo method validation
- Parameter sensitivity studies
- Correlation analysis demonstrations

---

*monteCarlo Physics Simulations v0.1.0 - Where Deterministic Laws Meet Parameter Uncertainty*
