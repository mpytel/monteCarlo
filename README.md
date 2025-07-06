# monteCarlo
**Version 0.1.0** - *Understanding Randomness Through Simulation*

A comprehensive Monte Carlo simulation framework for analyzing randomness patterns in web data. Built upon a dynamic command-line foundation, monteCarlo explores the philosophical question: *"How can we statistically understand the randomness of information available on the web? Indeed patterns will emerge. But the existence of these patterns are ultimately random."*

## Philosophy & Purpose

monteCarlo embraces uncertainty as a fundamental aspect of information. Rather than assuming we know what data exists or what patterns to expect, this framework:

- **Discovers data sources randomly** - Let chance guide exploration
- **Analyzes inherent randomness** - Measure chaos in real-world data  
- **Simulates thousands of scenarios** - Use Monte Carlo methods to understand uncertainty
- **Visualizes emergent patterns** - Make randomness visible through comprehensive plots
- **Compares different types of chaos** - From financial markets to weather systems to pure mathematics

The framework demonstrates that even in apparent randomness, statistical patterns emerge - and the discovery of these patterns is itself a random process.

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Core Philosophy](#core-philosophy)
3. [Architecture Overview](#architecture-overview)
4. [Data Source Discovery](#data-source-discovery)
5. [Monte Carlo Simulation Engine](#monte-carlo-simulation-engine)
6. [Visualization System](#visualization-system)
7. [Command Reference](#command-reference)
8. [Data Sources](#data-sources)
9. [Example Workflows](#example-workflows)
10. [Randomness Analysis](#randomness-analysis)
11. [Installation](#installation)
12. [Project Structure](#project-structure)
13. [Extending the Framework](#extending-the-framework)
14. [Contributing](#contributing)

---

## Quick Start

```bash
# Install the package
pip install -e .

# Discover what data is available (embrace the unknown)
monteCarlo listSources

# Get a random suggestion (let randomness guide you)
monteCarlo listSources random

# Fetch data from a random source
monteCarlo fetchData financial_stocks AAPL

# Setup a Monte Carlo simulation (use quotes for wildcard patterns)
monteCarlo setupSim stock_chaos 10000 'Open,High,Low,Close' 'financial_stocks_AAPL_*'

# Run the simulation
monteCarlo runSim stock_chaos

# Visualize the randomness patterns
monteCarlo plotResults stock_chaos all

# View all your explorations
monteCarlo listSims
```

## Core Philosophy

### The Randomness Paradox
monteCarlo is built on the understanding that:

1. **Web information appears random** - Stock prices, weather, social media, news
2. **Patterns exist within randomness** - Statistical structures emerge from chaos
3. **Pattern discovery is random** - We can't predict what we'll find
4. **Monte Carlo reveals truth** - Thousands of simulations expose underlying reality

### Design Principles

- **Embrace Uncertainty**: Don't assume you know what data exists
- **Random Discovery**: Let chance guide your exploration
- **Statistical Truth**: Use simulation to understand reality
- **Visual Patterns**: Make randomness visible through plots
- **Colorful Feedback**: Intuitive interface guides exploration

## Architecture Overview

monteCarlo extends a dynamic command-line framework with specialized Monte Carlo capabilities:

```
┌─────────────────────────────────────────────────────────────┐
│                    monteCarlo Framework                     │
├─────────────────────────────────────────────────────────────┤
│  Data Discovery → Fetching → Analysis → Simulation → Viz   │
├─────────────────────────────────────────────────────────────┤
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────┐ │
│ │   Sources   │ │   Fetcher   │ │   Engine    │ │  Plots  │ │
│ │ 7 Categories│ │ Multi-type  │ │ Statistics  │ │ 5 Types │ │
│ │ Random Disc.│ │ Randomness  │ │ Scenarios   │ │ Analysis│ │
│ └─────────────┘ └─────────────┘ └─────────────┘ └─────────┘ │
└─────────────────────────────────────────────────────────────┘
```

### Core Components

1. **Data Source Registry** - Comprehensive catalog of web randomness
2. **Data Fetcher** - Multi-source data collection with randomness analysis
3. **Monte Carlo Engine** - Statistical simulation and scenario generation
4. **Visualization System** - Comprehensive plotting with matplotlib
5. **Command Framework** - Dynamic, extensible command system

## Data Source Discovery

### Available Categories

monteCarlo provides access to 7 categories of web data, each with different randomness characteristics:

| Category | Description | Randomness Level | Example Sources |
|----------|-------------|------------------|-----------------|
| **Financial** | Markets, economics, trading | High | Stocks, Crypto, Forex, Commodities |
| **Weather** | Climate, atmospheric data | Extreme | Current conditions, Historical patterns |
| **Social** | Social media, sentiment | Extreme | Trends, Sentiment analysis |
| **Economic** | Indicators, employment | Medium | GDP, Unemployment, Inflation |
| **News** | Information flow | High | Headlines, Events |
| **Internet** | Digital behavior | Medium | Traffic, Domain data |
| **Synthetic** | Pure mathematical | Perfect | Normal, Uniform, Exponential |

### Discovery Commands

```bash
# See all categories
monteCarlo listSources

# Explore specific category
monteCarlo listSources financial

# Get random suggestion (philosophical approach)
monteCarlo listSources random

# Search for specific data
monteCarlo listSources search crypto
```

## Monte Carlo Simulation Engine

### Simulation Process

1. **Data Analysis** - Detect distributions, calculate randomness scores
2. **Parameter Fitting** - Fit statistical distributions to real data
3. **Scenario Generation** - Create thousands of random scenarios
4. **Statistical Analysis** - Calculate comprehensive statistics
5. **Relationship Modeling** - Analyze correlations and dependencies

### Randomness Scoring

monteCarlo calculates randomness scores for all data:

- **0.0 - 1.0**: Low randomness, strong patterns (e.g., financial OHLC data)
- **1.0 - 2.0**: Moderate randomness, some patterns (e.g., weather temperature)
- **2.0+**: High randomness, chaotic behavior (e.g., pure mathematical distributions)

### Simulation Types

```bash
# Basic simulation
monteCarlo setupSim my_sim 10000 'column1,column2' dataset_name

# Weather chaos analysis
monteCarlo setupSim weather_chaos 5000 'temperature,humidity,pressure' 'weather_*'

# Financial pattern analysis  
monteCarlo setupSim market_patterns 15000 'Open,High,Low,Close' 'financial_*'

# Pure randomness study
monteCarlo setupSim pure_random 8000 'value' 'synthetic_*'
```

## Visualization System

### Plot Types

monteCarlo generates 5 types of comprehensive visualizations:

1. **Histograms** - Distribution analysis with statistical overlays
2. **Scatter Matrix** - Relationship exploration between variables
3. **Correlation Heatmap** - Correlation strength visualization
4. **Convergence Analysis** - Monte Carlo convergence verification
5. **Scenario Comparison** - Best/worst/likely case analysis

### Visualization Commands

```bash
# Single plot type
monteCarlo plotResults simulation_name histogram

# All plot types
monteCarlo plotResults simulation_name all

# View generated plots
monteCarlo listPlots
```

### Plot Features

- **Statistical Overlays**: Mean, standard deviation, confidence intervals
- **Color Coding**: Intuitive color schemes for different data types
- **High Resolution**: 300 DPI plots suitable for analysis and presentation
- **Automatic Layout**: Intelligent subplot arrangement
- **Comprehensive Legends**: Clear labeling and statistical information

## Command Reference

### Data Discovery & Fetching
```bash
monteCarlo listSources [category|all|random|search <term>]
monteCarlo fetchData <source_type> <identifier> [options]
```

### Simulation Management
```bash
monteCarlo setupSim <name> <iterations> <columns> [dataset]
monteCarlo runSim <simulation_name>
monteCarlo listSims [status_filter]
```

**Important**: When using wildcard patterns in dataset names (e.g., `'financial_stocks_AAPL_*'`), always use quotes to prevent shell expansion. The framework will automatically resolve wildcards to the newest matching file.

### Visualization
```bash
monteCarlo plotResults <sim_name> [plot_type]
# plot_type: histogram, scatter, convergence, correlation, scenarios, all
```

### Framework Commands
```bash
monteCarlo newCmd <name> [args...]     # Create new commands
monteCarlo modCmd <name> [args...]     # Modify existing commands  
monteCarlo rmCmd <name> [args...]      # Remove commands
monteCarlo -h                          # Help system
```

## Data Sources

### Financial Data (via yfinance)
- **Stocks**: AAPL, GOOGL, MSFT, TSLA, SPY
- **Crypto**: BTC-USD, ETH-USD, ADA-USD, DOT-USD
- **Forex**: EURUSD=X, GBPUSD=X, USDJPY=X
- **Commodities**: GC=F (Gold), CL=F (Oil), SI=F (Silver)

### Synthetic Data
- **Distributions**: Normal, Uniform, Exponential, Poisson
- **Configurable**: Sample size, parameters
- **Pure Randomness**: Mathematical distributions for comparison

### Weather Data
- **Synthetic Generation**: Realistic weather patterns
- **Multiple Variables**: Temperature, humidity, pressure, wind
- **Seasonal Patterns**: Built-in cyclical behavior

## Example Workflows

### 1. Exploring Financial Randomness

```bash
# Discover financial sources
monteCarlo listSources financial

# Fetch stock data
monteCarlo fetchData financial_stocks AAPL

# Setup simulation (use quotes for wildcard patterns)
monteCarlo setupSim apple_analysis 10000 'Open,High,Low,Close' 'financial_stocks_AAPL_*'

# Run simulation
monteCarlo runSim apple_analysis

# Create all visualizations
monteCarlo plotResults apple_analysis all
```

### 2. Weather Chaos Analysis

```bash
# Get random suggestion
monteCarlo listSources random

# Fetch weather data (if suggested)
monteCarlo fetchData weather_historical precipitation

# Setup chaos simulation (use quotes for wildcard patterns)
monteCarlo setupSim weather_chaos 5000 'temperature,humidity,pressure' 'weather_*'

# Execute simulation
monteCarlo runSim weather_chaos

# Visualize chaos patterns
monteCarlo plotResults weather_chaos all
```

### 3. Comparative Randomness Study

```bash
# Fetch different data types
monteCarlo fetchData financial_forex USDJPY=X
monteCarlo fetchData synthetic_pure_random normal samples=2000

# Setup comparative simulations (use quotes for wildcard patterns)
monteCarlo setupSim forex_patterns 8000 'Open,Close' 'financial_forex_*'
monteCarlo setupSim pure_randomness 8000 'value' 'synthetic_*'

# Run both simulations
monteCarlo runSim forex_patterns
monteCarlo runSim pure_randomness

# Compare results
monteCarlo listSims completed
monteCarlo plotResults forex_patterns histogram
monteCarlo plotResults pure_randomness histogram
```

## Randomness Analysis

### Metrics Calculated

For each dataset and simulation, monteCarlo calculates:

- **Basic Statistics**: Mean, median, standard deviation, min/max
- **Distribution Properties**: Skewness, kurtosis, percentiles
- **Randomness Score**: Custom metric combining entropy and autocorrelation
- **Variability Measures**: Coefficient of variation, range analysis
- **Pattern Detection**: Trend analysis, cyclical behavior

### Interpretation Guide

| Randomness Score | Interpretation | Examples |
|------------------|----------------|----------|
| 0.0 - 0.5 | Highly structured, predictable patterns | Financial OHLC relationships |
| 0.5 - 1.0 | Some structure with random elements | Economic indicators |
| 1.0 - 2.0 | Moderate randomness with emergent patterns | Weather temperature |
| 2.0+ | High randomness, chaotic behavior | Pure mathematical distributions |

## Installation

### Requirements
- Python 3.10+
- Dependencies automatically installed:
  - numpy >= 1.21.0
  - matplotlib >= 3.5.0
  - pandas >= 1.3.0
  - scipy >= 1.7.0
  - yfinance >= 0.1.70
  - requests >= 2.25.0
  - beautifulsoup4 >= 4.9.0

### Installation Steps

```bash
# Clone or download the repository
git clone <repository-url>
cd monteCarlo

# Install in development mode
pip install -e .

# Verify installation
monteCarlo listSources
```

## Project Structure

```
monteCarlo/
├── src/monteCarlo/
│   ├── main.py                    # Entry point
│   ├── classes/
│   │   ├── argParse.py           # Enhanced argument parsing
│   │   └── optSwitches.py        # Option handling
│   ├── commands/
│   │   ├── commands.json         # Command definitions
│   │   ├── commands.py           # Command management
│   │   ├── cmdSwitchbord.py      # Command routing
│   │   ├── listSources.py        # Data source discovery
│   │   ├── fetchData.py          # Data fetching
│   │   ├── setupSim.py           # Simulation setup
│   │   ├── runSim.py             # Simulation execution
│   │   ├── plotResults.py        # Visualization
│   │   ├── listSims.py           # Simulation management
│   │   └── templates/            # Command templates
│   └── defs/
│       ├── logIt.py              # Colored logging
│       ├── dataSources.py        # Source registry
│       ├── dataFetcher.py        # Data collection
│       ├── monteCarloEngine.py   # Simulation engine
│       └── visualizer.py         # Plotting system
├── data/
│   ├── sources/                  # Raw data storage
│   ├── processed/                # Cleaned data
│   ├── simulations/              # Simulation results
│   └── plots/                    # Generated visualizations
├── pyproject.toml                # Package configuration
└── README.md                     # This file
```

## Extending the Framework

### Adding New Data Sources

1. **Update dataSources.py**: Add new source definitions
2. **Extend dataFetcher.py**: Implement fetching logic
3. **Test Integration**: Verify randomness analysis works

### Creating Custom Commands

```bash
# Use the built-in command creation system
monteCarlo newCmd myCommand arg1 arg2

# Choose from templates:
# - simple: Basic command structure
# - classCall: Object-oriented approach  
# - async: Asynchronous operations
```

### Custom Visualization Types

Extend `visualizer.py` to add new plot types:

```python
def _plot_custom_analysis(self, sim_name: str, results: Dict) -> bool:
    # Your custom visualization logic
    pass
```

## Contributing

monteCarlo embraces the philosophy that contributions, like patterns in randomness, emerge organically:

1. **Fork the repository**
2. **Let randomness guide your exploration** - Use `monteCarlo listSources random`
3. **Create meaningful simulations** - Add new data sources or analysis types
4. **Share your discoveries** - Submit pull requests with new insights
5. **Document patterns found** - Update examples with interesting results

### Development Philosophy

- **Embrace uncertainty** in development decisions
- **Let data guide features** rather than assumptions
- **Maintain colorful, intuitive interfaces**
- **Preserve the philosophical approach** to randomness exploration

## License

MIT License - Because knowledge, like randomness, should be freely shared.

## Author

**Primwind** - Original framework architect  
**Enhanced by AI** - Monte Carlo simulation capabilities

*"In the randomness of web information, patterns emerge. In the emergence of patterns, randomness persists. monteCarlo explores this beautiful paradox."*

---

**monteCarlo v0.1.0** - *Where Chaos Meets Understanding*
