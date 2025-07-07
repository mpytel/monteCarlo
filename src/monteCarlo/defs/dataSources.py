"""
Data Sources Registry - Discovering the Randomness of Web Information

This module defines available data sources for Monte Carlo analysis.
The philosophy: We don't know what patterns exist until we look.
Everything on the web has inherent randomness, but patterns emerge.
"""

import random
from typing import Dict, List, Any
from .logIt import printIt, lable

class DataSourceRegistry:
    """Registry of available data sources for Monte Carlo analysis"""
    
    def __init__(self):
        self.sources = {
            # Financial Markets - Classic randomness with emergent patterns
            "financial": {
                "description": "Financial markets - where randomness meets human psychology",
                "sources": {
                    "stocks": {
                        "description": "Stock prices (daily, hourly, minute data)",
                        "examples": ["AAPL", "GOOGL", "MSFT", "TSLA", "SPY"],
                        "columns": ["open", "high", "low", "close", "volume", "adj_close"],
                        "randomness": "High - affected by news, sentiment, algorithms",
                        "patterns": "Trends, seasonality, volatility clustering"
                    },
                    "crypto": {
                        "description": "Cryptocurrency prices - pure digital randomness",
                        "examples": ["BTC-USD", "ETH-USD", "ADA-USD", "DOT-USD"],
                        "columns": ["open", "high", "low", "close", "volume"],
                        "randomness": "Extreme - 24/7 global sentiment",
                        "patterns": "Pump/dump cycles, correlation with tech stocks"
                    },
                    "forex": {
                        "description": "Foreign exchange rates - economic randomness",
                        "examples": ["EURUSD=X", "GBPUSD=X", "USDJPY=X"],
                        "columns": ["open", "high", "low", "close"],
                        "randomness": "Medium - central bank policies",
                        "patterns": "Economic cycles, interest rate differentials"
                    },
                    "commodities": {
                        "description": "Commodity prices - supply/demand randomness",
                        "examples": ["GC=F", "CL=F", "SI=F", "NG=F"],
                        "columns": ["open", "high", "low", "close", "volume"],
                        "randomness": "High - weather, geopolitics, speculation",
                        "patterns": "Seasonal cycles, supply shocks"
                    }
                }
            },
            
            # Weather - Nature's randomness
            "weather": {
                "description": "Weather data - chaos theory in action",
                "sources": {
                    "current": {
                        "description": "Current weather conditions worldwide",
                        "examples": ["New York", "London", "Tokyo", "Sydney"],
                        "columns": ["temperature", "humidity", "pressure", "wind_speed", "visibility"],
                        "randomness": "High - butterfly effect, chaos systems",
                        "patterns": "Seasonal, geographic, climate zones"
                    },
                    "historical": {
                        "description": "Historical weather patterns",
                        "examples": ["temperature_trends", "precipitation", "extreme_events"],
                        "columns": ["temp_max", "temp_min", "precipitation", "wind", "humidity"],
                        "randomness": "Medium - climate patterns exist",
                        "patterns": "Seasonal cycles, climate change trends"
                    }
                }
            },
            
            # Social Media - Human behavior randomness
            "social": {
                "description": "Social media metrics - collective human randomness",
                "sources": {
                    "trends": {
                        "description": "Trending topics and hashtags",
                        "examples": ["#technology", "#finance", "#weather", "#news"],
                        "columns": ["mentions", "sentiment", "reach", "engagement"],
                        "randomness": "Extreme - viral unpredictability",
                        "patterns": "Viral cascades, sentiment waves"
                    },
                    "sentiment": {
                        "description": "Public sentiment analysis",
                        "examples": ["market_sentiment", "political_sentiment", "brand_sentiment"],
                        "columns": ["positive", "negative", "neutral", "volume"],
                        "randomness": "High - emotional responses",
                        "patterns": "Mood cycles, event-driven spikes"
                    }
                }
            },
            
            # Economic Indicators - Structured randomness
            "economic": {
                "description": "Economic indicators - policy meets randomness",
                "sources": {
                    "indicators": {
                        "description": "Key economic metrics",
                        "examples": ["GDP", "unemployment", "inflation", "interest_rates"],
                        "columns": ["value", "change", "forecast", "previous"],
                        "randomness": "Medium - policy-driven but unpredictable",
                        "patterns": "Business cycles, policy responses"
                    },
                    "employment": {
                        "description": "Employment statistics",
                        "examples": ["job_openings", "unemployment_rate", "wage_growth"],
                        "columns": ["rate", "change", "sector_breakdown"],
                        "randomness": "Medium - economic cycles",
                        "patterns": "Seasonal employment, industry trends"
                    }
                }
            },
            
            # News & Events - Information randomness
            "news": {
                "description": "News and events - information flow randomness",
                "sources": {
                    "headlines": {
                        "description": "News headline analysis",
                        "examples": ["financial_news", "tech_news", "world_news"],
                        "columns": ["sentiment", "keywords", "source", "timestamp"],
                        "randomness": "High - unpredictable events",
                        "patterns": "News cycles, topic clustering"
                    },
                    "events": {
                        "description": "Scheduled and unscheduled events",
                        "examples": ["earnings", "fed_meetings", "elections", "disasters"],
                        "columns": ["type", "impact", "surprise_factor", "market_reaction"],
                        "randomness": "Variable - some scheduled, some random",
                        "patterns": "Calendar effects, surprise impacts"
                    }
                }
            },
            
            # Internet Metrics - Digital randomness
            "internet": {
                "description": "Internet usage and digital behavior",
                "sources": {
                    "traffic": {
                        "description": "Website traffic patterns",
                        "examples": ["google_trends", "website_visits", "search_volume"],
                        "columns": ["volume", "geographic", "device_type", "time_spent"],
                        "randomness": "Medium - behavioral patterns exist",
                        "patterns": "Daily cycles, seasonal searches"
                    },
                    "domains": {
                        "description": "Domain registration and DNS data",
                        "examples": ["new_domains", "expired_domains", "dns_queries"],
                        "columns": ["registrations", "expirations", "query_volume"],
                        "randomness": "High - entrepreneurial activity",
                        "patterns": "Business cycles, tech trends"
                    }
                }
            },
            
            # Physics Simulations - Deterministic equations with parameter randomness
            "physics": {
                "description": "Physics simulations - deterministic laws with random parameters",
                "sources": {
                    # 🌊 Wave Physics
                    "wave_propagation": {
                        "description": "Wave propagation: v = f × λ (velocity, frequency, wavelength)",
                        "examples": ["sound_waves", "light_waves", "water_waves", "seismic_waves"],
                        "columns": ["frequency", "wavelength", "wave_speed"],
                        "randomness": "Low - deterministic relationship with parameter variation",
                        "patterns": "Perfect correlation: v = f × λ",
                        "equation": "wave_speed = frequency * wavelength",
                        "units": {"frequency": "Hz", "wavelength": "m", "wave_speed": "m/s"}
                    },
                    "standing_wave": {
                        "description": "Standing wave frequency: f = (n/2L)√(T/μ)",
                        "examples": ["guitar_string", "violin_string", "piano_wire", "cable_vibration"],
                        "columns": ["length", "tension", "linear_density"],
                        "randomness": "Low - deterministic with material property variation",
                        "patterns": "Inverse relationship with length, square root with tension",
                        "equation": "frequency = (harmonic/(2*length)) * sqrt(tension/linear_density)",
                        "units": {"length": "m", "tension": "N", "linear_density": "kg/m"}
                    },
                    "doppler_effect": {
                        "description": "Doppler effect: f' = f(v±vo)/(v±vs)",
                        "examples": ["ambulance_siren", "radar_detection", "astronomy_redshift", "ultrasound"],
                        "columns": ["source_velocity", "observer_velocity", "observed_frequency"],
                        "randomness": "Low - deterministic with velocity variations",
                        "patterns": "Linear relationship with relative velocities",
                        "equation": "observed_frequency = source_frequency * (sound_speed + observer_velocity) / (sound_speed + source_velocity)",
                        "units": {"source_velocity": "m/s", "observer_velocity": "m/s", "observed_frequency": "Hz"}
                    },
                    
                    # 🔥 Thermal Physics
                    "gas_law": {
                        "description": "Ideal gas law: PV = nRT",
                        "examples": ["atmospheric_pressure", "gas_cylinder", "weather_balloon", "engine_combustion"],
                        "columns": ["pressure", "volume", "temperature"],
                        "randomness": "Low - deterministic with measurement uncertainty",
                        "patterns": "Inverse P-V relationship, linear P-T and V-T",
                        "equation": "pressure * volume = n_moles * gas_constant * temperature",
                        "units": {"pressure": "Pa", "volume": "m³", "temperature": "K"}
                    },
                    "heat_diffusion": {
                        "description": "Heat diffusion: q = -k∇T (Fourier's law)",
                        "examples": ["building_insulation", "cpu_cooling", "geothermal", "cooking"],
                        "columns": ["temperature_gradient", "thermal_conductivity", "heat_flux"],
                        "randomness": "Low - deterministic with material property variation",
                        "patterns": "Linear relationship: heat flux proportional to gradient",
                        "equation": "heat_flux = thermal_conductivity * temperature_gradient",
                        "units": {"temperature_gradient": "K/m", "thermal_conductivity": "W/(m·K)", "heat_flux": "W/m²"}
                    },
                    "brownian_motion": {
                        "description": "Brownian motion: <x²> = 2Dt (Einstein relation)",
                        "examples": ["pollen_in_water", "nanoparticle_tracking", "molecular_diffusion", "stock_prices"],
                        "columns": ["displacement", "time", "diffusion_coefficient"],
                        "randomness": "Medium - stochastic process with deterministic statistics",
                        "patterns": "Square root relationship with time",
                        "equation": "mean_square_displacement = 2 * diffusion_coefficient * time",
                        "units": {"displacement": "m", "time": "s", "diffusion_coefficient": "m²/s"}
                    },
                    
                    # ⚡ Electromagnetic
                    "rc_circuit": {
                        "description": "RC circuit: V(t) = V₀e^(-t/RC)",
                        "examples": ["capacitor_discharge", "camera_flash", "timing_circuit", "filter_design"],
                        "columns": ["voltage", "current", "time_constant"],
                        "randomness": "Low - deterministic exponential decay",
                        "patterns": "Exponential decay with RC time constant",
                        "equation": "voltage = initial_voltage * exp(-time / time_constant)",
                        "units": {"voltage": "V", "current": "A", "time_constant": "s"}
                    },
                    "em_wave": {
                        "description": "EM wave impedance: Z = E/H = √(μ/ε)",
                        "examples": ["radio_transmission", "microwave_oven", "optical_fiber", "antenna_design"],
                        "columns": ["electric_field", "magnetic_field", "wave_impedance"],
                        "randomness": "Low - deterministic with medium property variation",
                        "patterns": "Constant ratio in free space (377Ω)",
                        "equation": "wave_impedance = electric_field / magnetic_field",
                        "units": {"electric_field": "V/m", "magnetic_field": "A/m", "wave_impedance": "Ω"}
                    },
                    "photoelectric": {
                        "description": "Photoelectric effect: KE = hf - φ",
                        "examples": ["solar_cell", "photomultiplier", "image_sensor", "photodiode"],
                        "columns": ["photon_energy", "work_function", "kinetic_energy"],
                        "randomness": "Low - deterministic quantum threshold effect",
                        "patterns": "Linear above threshold, zero below",
                        "equation": "kinetic_energy = max(0, photon_energy - work_function)",
                        "units": {"photon_energy": "eV", "work_function": "eV", "kinetic_energy": "eV"}
                    },
                    
                    # 🌊 Fluid Dynamics
                    "bernoulli": {
                        "description": "Bernoulli equation: P + ½ρv² + ρgh = constant",
                        "examples": ["airplane_wing", "venturi_meter", "pitot_tube", "water_flow"],
                        "columns": ["pressure", "velocity", "height"],
                        "randomness": "Low - deterministic with flow condition variation",
                        "patterns": "Energy conservation: pressure + kinetic + potential",
                        "equation": "total_pressure = static_pressure + 0.5 * density * velocity**2 + density * gravity * height",
                        "units": {"pressure": "Pa", "velocity": "m/s", "height": "m"}
                    },
                    "poiseuille": {
                        "description": "Poiseuille flow: Q = πr⁴ΔP/(8μL)",
                        "examples": ["blood_flow", "oil_pipeline", "microfluidics", "hydraulic_system"],
                        "columns": ["flow_rate", "pressure_drop", "pipe_radius"],
                        "randomness": "Low - deterministic with viscosity variation",
                        "patterns": "Fourth power dependence on radius",
                        "equation": "flow_rate = (pi * pipe_radius**4 * pressure_drop) / (8 * viscosity * length)",
                        "units": {"flow_rate": "m³/s", "pressure_drop": "Pa", "pipe_radius": "m"}
                    },
                    "surface_tension": {
                        "description": "Surface tension: F = γL cos(θ)",
                        "examples": ["water_droplet", "soap_bubble", "capillary_action", "wetting"],
                        "columns": ["contact_angle", "surface_energy", "wetting_force"],
                        "randomness": "Low - deterministic with surface property variation",
                        "patterns": "Cosine dependence on contact angle",
                        "equation": "wetting_force = surface_energy * contact_length * cos(contact_angle)",
                        "units": {"contact_angle": "rad", "surface_energy": "N/m", "wetting_force": "N"}
                    },
                    
                    # 🔬 Quantum Physics
                    "harmonic_oscillator": {
                        "description": "Quantum harmonic oscillator: E = ℏω(n + ½)",
                        "examples": ["molecular_vibration", "phonon_modes", "laser_cavity", "atomic_trap"],
                        "columns": ["position", "momentum", "energy"],
                        "randomness": "Medium - quantum uncertainty with deterministic energy levels",
                        "patterns": "Quantized energy levels, uncertainty principle",
                        "equation": "energy = hbar * frequency * (quantum_number + 0.5)",
                        "units": {"position": "m", "momentum": "kg·m/s", "energy": "J"}
                    },
                    "blackbody": {
                        "description": "Planck's law: B(λ,T) = 2hc²/λ⁵ × 1/(e^(hc/λkT)-1)",
                        "examples": ["stellar_radiation", "thermal_imaging", "incandescent_bulb", "cosmic_background"],
                        "columns": ["temperature", "wavelength", "intensity"],
                        "randomness": "Low - deterministic thermal radiation",
                        "patterns": "Peak wavelength inversely proportional to temperature",
                        "equation": "intensity = (2 * planck * light_speed**2 / wavelength**5) / (exp(planck * light_speed / (wavelength * boltzmann * temperature)) - 1)",
                        "units": {"temperature": "K", "wavelength": "m", "intensity": "W/(m²·sr·m)"}
                    },
                    "particle_decay": {
                        "description": "Radioactive decay: N(t) = N₀e^(-λt)",
                        "examples": ["carbon_dating", "nuclear_reactor", "medical_isotope", "cosmic_rays"],
                        "columns": ["initial_count", "time", "decay_constant"],
                        "randomness": "Medium - stochastic process with deterministic statistics",
                        "patterns": "Exponential decay with characteristic half-life",
                        "equation": "remaining_count = initial_count * exp(-decay_constant * time)",
                        "units": {"initial_count": "particles", "time": "s", "decay_constant": "1/s"}
                    },
                    
                    # 🌌 Mechanics
                    "orbital": {
                        "description": "Orbital mechanics: v = √(GM/r)",
                        "examples": ["satellite_orbit", "planetary_motion", "space_station", "asteroid_belt"],
                        "columns": ["radius", "velocity", "central_mass"],
                        "randomness": "Low - deterministic with orbital parameter variation",
                        "patterns": "Inverse square root relationship with radius",
                        "equation": "orbital_velocity = sqrt(gravitational_constant * central_mass / radius)",
                        "units": {"radius": "m", "velocity": "m/s", "central_mass": "kg"}
                    },
                    "gravitational_lens": {
                        "description": "Gravitational lensing: α = 4GM/(c²b)",
                        "examples": ["galaxy_cluster", "black_hole", "dark_matter", "quasar_imaging"],
                        "columns": ["deflection_angle", "mass", "impact_parameter"],
                        "randomness": "Low - deterministic general relativity effect",
                        "patterns": "Inverse relationship with impact parameter",
                        "equation": "deflection_angle = 4 * gravitational_constant * mass / (light_speed**2 * impact_parameter)",
                        "units": {"deflection_angle": "rad", "mass": "kg", "impact_parameter": "m"}
                    },
                    "pendulum": {
                        "description": "Simple pendulum: T = 2π√(L/g)",
                        "examples": ["grandfather_clock", "seismometer", "foucault_pendulum", "metronome"],
                        "columns": ["length", "period", "gravitational_acceleration"],
                        "randomness": "Low - deterministic with length variation",
                        "patterns": "Square root relationship with length",
                        "equation": "period = 2 * pi * sqrt(length / gravitational_acceleration)",
                        "units": {"length": "m", "period": "s", "gravitational_acceleration": "m/s²"}
                    }
                }
            },
            
            # Random Data Generators - Pure randomness for testing
            "synthetic": {
                "description": "Synthetic random data for testing theories",
                "sources": {
                    "pure_random": {
                        "description": "Mathematically random data",
                        "examples": ["normal", "uniform", "exponential", "poisson"],
                        "columns": ["value", "timestamp", "distribution_params"],
                        "randomness": "Perfect - mathematically defined",
                        "patterns": "Only statistical properties"
                    },
                    "correlated": {
                        "description": "Random data with defined correlations",
                        "examples": ["corr_0.5", "corr_0.8", "corr_negative"],
                        "columns": ["var1", "var2", "var3", "correlation_matrix"],
                        "randomness": "Controlled - defined relationships",
                        "patterns": "Designed correlations"
                    }
                }
            }
        }
    
    def list_categories(self):
        """List all available data categories"""
        printIt("🎲 Available Data Categories - Exploring Web Randomness", lable.INFO)
        printIt("=" * 60, lable.INFO)
        
        for category, info in self.sources.items():
            printIt(f"\n📊 {category.upper()}", lable.PASS)
            printIt(f"   {info['description']}", lable.INFO)
            printIt(f"   Sources: {len(info['sources'])} available", lable.STAT)
    
    def list_sources(self, category=None):
        """List sources in a category or all sources"""
        if category and category in self.sources:
            self._list_category_sources(category)
        else:
            printIt("🌐 All Available Data Sources", lable.INFO)
            printIt("=" * 60, lable.INFO)
            for cat in self.sources.keys():
                self._list_category_sources(cat)
                printIt("", lable.INFO)  # spacing
    
    def _list_category_sources(self, category):
        """List sources for a specific category"""
        cat_info = self.sources[category]
        printIt(f"\n📈 {category.upper()} - {cat_info['description']}", lable.PASS)
        
        for source_name, source_info in cat_info['sources'].items():
            printIt(f"\n  🔹 {source_name}", lable.INFO)
            printIt(f"     {source_info['description']}", lable.CONFIG)
            printIt(f"     Examples: {', '.join(source_info['examples'][:3])}", lable.CONFIG)
            printIt(f"     Columns: {', '.join(source_info['columns'][:4])}", lable.CONFIG)
            printIt(f"     Randomness: {source_info['randomness']}", lable.WARN)
            printIt(f"     Patterns: {source_info['patterns']}", lable.PASS)
    
    def get_random_suggestion(self):
        """Get a random data source suggestion - embrace the randomness!"""
        category = random.choice(list(self.sources.keys()))
        source_name = random.choice(list(self.sources[category]['sources'].keys()))
        source_info = self.sources[category]['sources'][source_name]
        
        printIt("🎯 Random Data Suggestion (Let randomness guide you!)", lable.INFO)
        printIt("=" * 50, lable.INFO)
        printIt(f"Category: {category}", lable.PASS)
        printIt(f"Source: {source_name}", lable.PASS)
        printIt(f"Description: {source_info['description']}", lable.CONFIG)
        
        # Random example
        example = random.choice(source_info['examples'])
        printIt(f"Try this: monteCarlo fetchData {category}_{source_name} {example}", lable.WARN)
        
        return category, source_name, example
    
    def get_source_info(self, category, source_name):
        """Get detailed information about a specific source"""
        if category in self.sources and source_name in self.sources[category]['sources']:
            return self.sources[category]['sources'][source_name]
        return None
    
    def search_sources(self, keyword):
        """Search for sources containing a keyword"""
        results = []
        keyword = keyword.lower()
        
        for category, cat_info in self.sources.items():
            for source_name, source_info in cat_info['sources'].items():
                # Search in description, examples, and columns
                searchable = (
                    source_info['description'].lower() + ' ' +
                    ' '.join(source_info['examples']).lower() + ' ' +
                    ' '.join(source_info['columns']).lower()
                )
                
                if keyword in searchable:
                    results.append((category, source_name, source_info))
        
        if results:
            printIt(f"🔍 Search results for '{keyword}':", lable.INFO)
            printIt("=" * 40, lable.INFO)
            for category, source_name, source_info in results:
                printIt(f"\n📊 {category}/{source_name}", lable.PASS)
                printIt(f"   {source_info['description']}", lable.CONFIG)
        else:
            printIt(f"No sources found for '{keyword}'", lable.WARN)
        
        return results

# Global instance
data_registry = DataSourceRegistry()
