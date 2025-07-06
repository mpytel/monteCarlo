"""
Monte Carlo Engine - Understanding Randomness Through Simulation

This module implements Monte Carlo simulation methods to analyze the randomness
and patterns in web data. Philosophy: Run thousands of scenarios to understand
the true nature of uncertainty in information.
"""

import numpy as np
import pandas as pd
import json
import os
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
from scipy import stats
from .logIt import printIt, lable
from .dataFetcher import data_fetcher

class MonteCarloEngine:
    """Core Monte Carlo simulation engine"""
    
    def __init__(self, data_dir="/Users/primwind/proj/test/monteCarlo/data"):
        self.data_dir = data_dir
        self.simulations_dir = os.path.join(data_dir, "simulations")
        self.relationships_dir = os.path.join(data_dir, "relationships")
        
        # Ensure directories exist
        os.makedirs(self.simulations_dir, exist_ok=True)
        os.makedirs(self.relationships_dir, exist_ok=True)
        
        self.simulations = {}  # Active simulations in memory
        self.relationships = {}  # Column relationships
    
    def setup_simulation(self, name: str, iterations: int, columns: List[str], 
                        dataset: str = None, **kwargs) -> bool:
        """Setup a new Monte Carlo simulation"""
        printIt(f"🎲 Setting up simulation '{name}' with {iterations} iterations", lable.INFO)
        
        # Load data if dataset specified
        data = None
        actual_dataset_name = dataset
        if dataset:
            # Check if dataset contains wildcards
            if '*' in dataset or '?' in dataset:
                actual_dataset_name = self._resolve_dataset_pattern(dataset)
                if not actual_dataset_name:
                    printIt(f"No datasets found matching pattern: {dataset}", lable.ERROR)
                    return False
                printIt(f"Resolved pattern '{dataset}' to '{actual_dataset_name}'", lable.INFO)
            
            data = data_fetcher.load_data(actual_dataset_name)
            if data is None:
                printIt(f"Could not load dataset: {actual_dataset_name}", lable.ERROR)
                return False
        
        # Validate columns
        if data is not None:
            available_cols = data.select_dtypes(include=[np.number]).columns.tolist()
            invalid_cols = [col for col in columns if col not in available_cols]
            if invalid_cols:
                printIt(f"Invalid columns: {invalid_cols}", lable.WARN)
                printIt(f"Available columns: {available_cols}", lable.INFO)
                columns = [col for col in columns if col in available_cols]
        
        if not columns:
            printIt("No valid columns specified", lable.ERROR)
            return False
        
        # Create simulation configuration
        sim_config = {
            'name': name,
            'iterations': iterations,
            'columns': columns,
            'dataset': actual_dataset_name,  # Store the resolved name
            'created': datetime.now().isoformat(),
            'status': 'configured',
            'parameters': kwargs,
            'data_stats': {},
            'relationships': {}
        }
        
        # Analyze data statistics if available
        if data is not None:
            for col in columns:
                if col in data.columns:
                    col_data = data[col].dropna()
                    sim_config['data_stats'][col] = {
                        'mean': float(col_data.mean()),
                        'std': float(col_data.std()),
                        'min': float(col_data.min()),
                        'max': float(col_data.max()),
                        'distribution': self._detect_distribution(col_data),
                        'randomness_score': self._calculate_randomness_score(col_data)
                    }
        
        # Save configuration
        self.simulations[name] = sim_config
        self._save_simulation_config(name, sim_config)
        
        printIt(f"✅ Simulation '{name}' configured successfully", lable.PASS)
        printIt(f"   Columns: {', '.join(columns)}", lable.DEBUG)
        printIt(f"   Iterations: {iterations:,}", lable.DEBUG)
        
        return True
    
    def _resolve_dataset_pattern(self, pattern: str) -> str:
        """Resolve wildcard patterns to actual dataset names"""
        import glob
        import os
        
        # Construct the full path pattern
        sources_dir = os.path.join(self.data_dir, "sources")
        full_pattern = os.path.join(sources_dir, f"{pattern}.csv")
        
        # Find matching files
        matches = glob.glob(full_pattern)
        
        if not matches:
            return None
        
        if len(matches) > 1:
            # Sort by modification time, newest first
            matches.sort(key=os.path.getmtime, reverse=True)
            printIt(f"Multiple matches found, using newest: {os.path.basename(matches[0])}", lable.INFO)
        
        # Return just the filename without extension
        return os.path.basename(matches[0]).replace('.csv', '')
    
    def run_simulation(self, name: str) -> bool:
        """Execute a Monte Carlo simulation"""
        if name not in self.simulations:
            # Try to load from disk
            if not self._load_simulation_config(name):
                printIt(f"Simulation '{name}' not found", lable.ERROR)
                return False
        
        sim_config = self.simulations[name]
        printIt(f"🚀 Running Monte Carlo simulation '{name}'...", lable.INFO)
        
        iterations = sim_config['iterations']
        columns = sim_config['columns']
        
        # Initialize results storage
        results = {
            'iterations': iterations,
            'columns': columns,
            'data': {},
            'statistics': {},
            'correlations': {},
            'scenarios': []
        }
        
        # Generate random scenarios
        printIt(f"Generating {iterations:,} random scenarios...", lable.DEBUG)
        
        for col in columns:
            if col in sim_config['data_stats']:
                stats = sim_config['data_stats'][col]
                distribution = stats['distribution']
                
                # Generate random values based on detected distribution
                if distribution == 'normal':
                    values = np.random.normal(stats['mean'], stats['std'], iterations)
                elif distribution == 'uniform':
                    values = np.random.uniform(stats['min'], stats['max'], iterations)
                elif distribution == 'exponential':
                    # Use mean as scale parameter
                    scale = stats['mean'] if stats['mean'] > 0 else 1.0
                    values = np.random.exponential(scale, iterations)
                else:
                    # Default to normal distribution
                    values = np.random.normal(stats['mean'], stats['std'], iterations)
                
                results['data'][col] = values.tolist()
            else:
                # Generate pure random data if no statistics available
                values = np.random.normal(0, 1, iterations)
                results['data'][col] = values.tolist()
        
        # Apply relationships between columns
        results = self._apply_relationships(results, sim_config)
        
        # Calculate simulation statistics
        results['statistics'] = self._calculate_simulation_statistics(results)
        
        # Calculate correlations
        results['correlations'] = self._calculate_correlations(results)
        
        # Generate scenario analysis
        results['scenarios'] = self._generate_scenarios(results)
        
        # Save results
        results['completed'] = datetime.now().isoformat()
        results['execution_time'] = 'calculated'  # Would calculate actual time
        
        self._save_simulation_results(name, results)
        
        # Update simulation status
        sim_config['status'] = 'completed'
        sim_config['last_run'] = datetime.now().isoformat()
        self.simulations[name] = sim_config
        self._save_simulation_config(name, sim_config)  # Save updated config
        
        printIt(f"✅ Simulation '{name}' completed successfully", lable.PASS)
        self._display_simulation_summary(name, results)
        
        return True
    
    def _detect_distribution(self, data: pd.Series) -> str:
        """Detect the most likely statistical distribution"""
        from scipy import stats as scipy_stats
        
        try:
            # Test for normality
            _, p_normal = scipy_stats.normaltest(data)
            
            # Test for uniformity
            _, p_uniform = scipy_stats.kstest(data, 'uniform')
            
            # Simple heuristics based on shape
            skewness = scipy_stats.skew(data)
            kurtosis = scipy_stats.kurtosis(data)
            
            if p_normal > 0.05:
                return 'normal'
            elif abs(skewness) < 0.5 and abs(kurtosis) < 0.5:
                return 'uniform'
            elif skewness > 1.0:
                return 'exponential'
            else:
                return 'normal'  # Default
                
        except:
            return 'normal'
    
    def _calculate_randomness_score(self, data: pd.Series) -> float:
        """Calculate a randomness score for the data"""
        try:
            # Combine multiple randomness measures
            
            # 1. Entropy measure
            hist, _ = np.histogram(data, bins=min(50, len(data)//10 + 1))
            hist = hist[hist > 0]
            prob = hist / np.sum(hist)
            entropy = -np.sum(prob * np.log2(prob))
            
            # 2. Autocorrelation measure
            autocorr = data.autocorr(lag=1) if len(data) > 1 else 0
            
            # 3. Runs test (simplified)
            median = data.median()
            runs = np.sum(np.diff(data > median) != 0) + 1
            expected_runs = 2 * np.sum(data > median) * np.sum(data <= median) / len(data) + 1
            runs_score = abs(runs - expected_runs) / expected_runs if expected_runs > 0 else 0
            
            # Combine scores (higher = more random)
            randomness_score = (entropy / 10.0) + (1 - abs(autocorr)) + (1 - runs_score)
            
            return float(np.clip(randomness_score, 0, 3))
            
        except:
            return 1.0  # Default moderate randomness
    
    def _apply_relationships(self, results: Dict, sim_config: Dict) -> Dict:
        """Apply defined relationships between columns"""
        # For now, return as-is
        # In full implementation, would apply correlation matrices, 
        # causal relationships, etc.
        return results
    
    def _calculate_simulation_statistics(self, results: Dict) -> Dict:
        """Calculate comprehensive statistics for simulation results"""
        from scipy import stats as scipy_stats
        
        statistics = {}
        
        for col, values in results['data'].items():
            values_array = np.array(values)
            
            statistics[col] = {
                'mean': float(np.mean(values_array)),
                'median': float(np.median(values_array)),
                'std': float(np.std(values_array)),
                'min': float(np.min(values_array)),
                'max': float(np.max(values_array)),
                'q25': float(np.percentile(values_array, 25)),
                'q75': float(np.percentile(values_array, 75)),
                'skewness': float(scipy_stats.skew(values_array)),
                'kurtosis': float(scipy_stats.kurtosis(values_array)),
                'var': float(np.var(values_array))
            }
        
        return statistics
    
    def _calculate_correlations(self, results: Dict) -> Dict:
        """Calculate correlations between simulated columns"""
        correlations = {}
        columns = list(results['data'].keys())
        
        for i, col1 in enumerate(columns):
            for j, col2 in enumerate(columns[i+1:], i+1):
                corr = np.corrcoef(results['data'][col1], results['data'][col2])[0, 1]
                correlations[f"{col1}_vs_{col2}"] = float(corr)
        
        return correlations
    
    def _generate_scenarios(self, results: Dict) -> List[Dict]:
        """Generate key scenario analyses"""
        scenarios = []
        
        # Best case scenario (95th percentile)
        best_case = {}
        for col, values in results['data'].items():
            best_case[col] = float(np.percentile(values, 95))
        scenarios.append({'name': 'best_case', 'percentile': 95, 'values': best_case})
        
        # Worst case scenario (5th percentile)
        worst_case = {}
        for col, values in results['data'].items():
            worst_case[col] = float(np.percentile(values, 5))
        scenarios.append({'name': 'worst_case', 'percentile': 5, 'values': worst_case})
        
        # Most likely scenario (median)
        most_likely = {}
        for col, values in results['data'].items():
            most_likely[col] = float(np.median(values))
        scenarios.append({'name': 'most_likely', 'percentile': 50, 'values': most_likely})
        
        return scenarios
    
    def _display_simulation_summary(self, name: str, results: Dict):
        """Display a summary of simulation results"""
        printIt(f"\n📊 Simulation Results Summary for '{name}'", lable.INFO)
        printIt("=" * 60, lable.INFO)
        
        # Display statistics for each column
        for col in results['columns']:
            if col in results['statistics']:
                stats = results['statistics'][col]
                printIt(f"\n🎯 {col.upper()}:", lable.PASS)
                printIt(f"   Mean: {stats['mean']:.4f} ± {stats['std']:.4f}", lable.DEBUG)
                printIt(f"   Range: [{stats['min']:.4f}, {stats['max']:.4f}]", lable.DEBUG)
                printIt(f"   Median: {stats['median']:.4f}", lable.DEBUG)
                
                # Randomness assessment
                cv = abs(stats['std'] / stats['mean']) if stats['mean'] != 0 else float('inf')
                if cv > 1.0:
                    printIt(f"   Assessment: High variability (CV: {cv:.2f})", lable.WARN)
                elif cv > 0.5:
                    printIt(f"   Assessment: Moderate variability (CV: {cv:.2f})", lable.INFO)
                else:
                    printIt(f"   Assessment: Low variability (CV: {cv:.2f})", lable.PASS)
        
        # Display key scenarios
        printIt(f"\n🎭 Key Scenarios:", lable.INFO)
        for scenario in results['scenarios']:
            printIt(f"   {scenario['name'].replace('_', ' ').title()} ({scenario['percentile']}th percentile):", lable.DEBUG)
            for col, value in scenario['values'].items():
                printIt(f"     {col}: {value:.4f}", lable.DEBUG)
    
    def _save_simulation_config(self, name: str, config: Dict):
        """Save simulation configuration to disk"""
        filepath = os.path.join(self.simulations_dir, f"{name}_config.json")
        with open(filepath, 'w') as f:
            json.dump(config, f, indent=2, default=str)
    
    def _save_simulation_results(self, name: str, results: Dict):
        """Save simulation results to disk"""
        filepath = os.path.join(self.simulations_dir, f"{name}_results.json")
        with open(filepath, 'w') as f:
            json.dump(results, f, indent=2, default=str)
    
    def _load_simulation_config(self, name: str) -> bool:
        """Load simulation configuration from disk"""
        filepath = os.path.join(self.simulations_dir, f"{name}_config.json")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                config = json.load(f)
                self.simulations[name] = config
                return True
        return False
    
    def list_simulations(self) -> Dict[str, Dict]:
        """List all available simulations"""
        simulations = {}
        
        # Load from memory
        simulations.update(self.simulations)
        
        # Load from disk
        if os.path.exists(self.simulations_dir):
            for filename in os.listdir(self.simulations_dir):
                if filename.endswith('_config.json'):
                    name = filename.replace('_config.json', '')
                    if name not in simulations:
                        self._load_simulation_config(name)
                        if name in self.simulations:
                            simulations[name] = self.simulations[name]
        
        return simulations

# Global instance
monte_carlo_engine = MonteCarloEngine()
