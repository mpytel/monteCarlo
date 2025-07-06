"""
Visualizer - Making Randomness Visible

This module creates visualizations for Monte Carlo simulation results using matplotlib.
Philosophy: Patterns in randomness become clear when we can see them.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd
import json
import os
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
from scipy import stats
from .logIt import printIt, lable
from .monteCarloEngine import monte_carlo_engine

class MonteCarloVisualizer:
    """Creates visualizations for Monte Carlo simulation results"""
    
    def __init__(self, data_dir="/Users/primwind/proj/test/monteCarlo/data"):
        self.data_dir = data_dir
        self.simulations_dir = os.path.join(data_dir, "simulations")
        self.plots_dir = os.path.join(data_dir, "plots")
        
        # Ensure plots directory exists
        os.makedirs(self.plots_dir, exist_ok=True)
        
        # Set matplotlib style for better-looking plots
        plt.style.use('default')
        self.colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', 
                      '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
    
    def plot_results(self, sim_name: str, plot_type: str = 'histogram') -> bool:
        """Create plots for simulation results"""
        printIt(f"📊 Creating {plot_type} plots for simulation '{sim_name}'", lable.INFO)
        
        # Load simulation results
        results = self._load_simulation_results(sim_name)
        if not results:
            printIt(f"Could not load results for simulation '{sim_name}'", lable.ERROR)
            return False
        
        try:
            if plot_type == 'histogram':
                return self._plot_histograms(sim_name, results)
            elif plot_type == 'scatter':
                return self._plot_scatter_matrix(sim_name, results)
            elif plot_type == 'convergence':
                return self._plot_convergence(sim_name, results)
            elif plot_type == 'correlation':
                return self._plot_correlation_matrix(sim_name, results)
            elif plot_type == 'scenarios':
                return self._plot_scenarios(sim_name, results)
            elif plot_type == 'all':
                # Create all plot types
                success = True
                for ptype in ['histogram', 'scatter', 'convergence', 'correlation', 'scenarios']:
                    success &= self.plot_results(sim_name, ptype)
                return success
            else:
                printIt(f"Unknown plot type: {plot_type}", lable.WARN)
                printIt("Available types: histogram, scatter, convergence, correlation, scenarios, all", lable.INFO)
                return False
                
        except Exception as e:
            printIt(f"Error creating plots: {str(e)}", lable.ERROR)
            return False
    
    def _plot_histograms(self, sim_name: str, results: Dict) -> bool:
        """Create histogram plots for each variable"""
        columns = results.get('columns', [])
        data = results.get('data', {})
        statistics = results.get('statistics', {})
        
        if not columns or not data:
            printIt("No data available for histogram plots", lable.WARN)
            return False
        
        # Calculate subplot layout
        n_cols = min(3, len(columns))
        n_rows = (len(columns) + n_cols - 1) // n_cols
        
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(5*n_cols, 4*n_rows))
        if n_rows == 1 and n_cols == 1:
            axes = [axes]
        elif n_rows == 1 or n_cols == 1:
            axes = axes.flatten()
        else:
            axes = axes.flatten()
        
        fig.suptitle(f'Monte Carlo Simulation Results: {sim_name}', fontsize=16, fontweight='bold')
        
        for i, col in enumerate(columns):
            if col in data and i < len(axes):
                ax = axes[i]
                values = np.array(data[col])
                
                # Create histogram
                n_bins = min(50, len(values) // 20)
                counts, bins, patches = ax.hist(values, bins=n_bins, alpha=0.7, 
                                              color=self.colors[i % len(self.colors)], 
                                              edgecolor='black', linewidth=0.5)
                
                # Add statistics
                if col in statistics:
                    stats_data = statistics[col]
                    mean_val = stats_data['mean']
                    std_val = stats_data['std']
                    
                    # Add vertical lines for key statistics
                    ax.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_val:.3f}')
                    ax.axvline(mean_val - std_val, color='orange', linestyle=':', alpha=0.7, label=f'-1σ: {mean_val-std_val:.3f}')
                    ax.axvline(mean_val + std_val, color='orange', linestyle=':', alpha=0.7, label=f'+1σ: {mean_val+std_val:.3f}')
                    
                    # Add percentile shading
                    q5 = np.percentile(values, 5)
                    q95 = np.percentile(values, 95)
                    ax.axvspan(q5, q95, alpha=0.2, color='green', label='90% Confidence')
                
                ax.set_title(f'{col}\nRandomness Distribution', fontweight='bold')
                ax.set_xlabel('Value')
                ax.set_ylabel('Frequency')
                ax.legend(fontsize=8)
                ax.grid(True, alpha=0.3)
        
        # Hide unused subplots
        for i in range(len(columns), len(axes)):
            axes[i].set_visible(False)
        
        plt.tight_layout()
        
        # Save plot
        filename = f"{sim_name}_histograms.png"
        filepath = os.path.join(self.plots_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        printIt(f"📈 Histogram plots saved to: {filepath}", lable.PASS)
        return True
    
    def _plot_scatter_matrix(self, sim_name: str, results: Dict) -> bool:
        """Create scatter plot matrix for variable relationships"""
        columns = results.get('columns', [])
        data = results.get('data', {})
        
        if len(columns) < 2:
            printIt("Need at least 2 variables for scatter matrix", lable.WARN)
            return False
        
        # Limit to first 5 variables for readability
        plot_columns = columns[:5]
        n_vars = len(plot_columns)
        
        fig, axes = plt.subplots(n_vars, n_vars, figsize=(3*n_vars, 3*n_vars))
        fig.suptitle(f'Variable Relationships: {sim_name}', fontsize=16, fontweight='bold')
        
        for i, col1 in enumerate(plot_columns):
            for j, col2 in enumerate(plot_columns):
                ax = axes[i, j] if n_vars > 1 else axes
                
                if i == j:
                    # Diagonal: histogram
                    values = np.array(data[col1])
                    ax.hist(values, bins=30, alpha=0.7, color=self.colors[i % len(self.colors)])
                    ax.set_title(f'{col1}')
                else:
                    # Off-diagonal: scatter plot
                    values1 = np.array(data[col1])
                    values2 = np.array(data[col2])
                    
                    # Sample data for performance if too many points
                    if len(values1) > 5000:
                        indices = np.random.choice(len(values1), 5000, replace=False)
                        values1 = values1[indices]
                        values2 = values2[indices]
                    
                    ax.scatter(values1, values2, alpha=0.5, s=1, 
                              color=self.colors[(i+j) % len(self.colors)])
                    
                    # Calculate and display correlation
                    correlation = np.corrcoef(values1, values2)[0, 1]
                    ax.set_title(f'r = {correlation:.3f}')
                    
                    # Add trend line if correlation is significant
                    if abs(correlation) > 0.1:
                        z = np.polyfit(values1, values2, 1)
                        p = np.poly1d(z)
                        ax.plot(sorted(values1), p(sorted(values1)), "r--", alpha=0.8)
                
                if i == n_vars - 1:
                    ax.set_xlabel(col2)
                if j == 0:
                    ax.set_ylabel(col1)
                
                ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Save plot
        filename = f"{sim_name}_scatter_matrix.png"
        filepath = os.path.join(self.plots_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        printIt(f"🔗 Scatter matrix saved to: {filepath}", lable.PASS)
        return True
    
    def _plot_convergence(self, sim_name: str, results: Dict) -> bool:
        """Plot convergence analysis for Monte Carlo simulation"""
        # This would require convergence data from the simulation
        # For now, create a placeholder convergence plot
        
        columns = results.get('columns', [])
        iterations = results.get('iterations', 10000)
        
        fig, axes = plt.subplots(2, 1, figsize=(12, 8))
        fig.suptitle(f'Monte Carlo Convergence Analysis: {sim_name}', fontsize=16, fontweight='bold')
        
        # Simulate convergence data (in real implementation, this would come from the simulation)
        x = np.arange(100, iterations + 1, 100)
        
        for i, col in enumerate(columns[:3]):  # Show first 3 variables
            # Simulate running mean convergence
            true_mean = 0  # Would be actual mean from results
            running_means = true_mean + np.random.normal(0, 1/np.sqrt(x), len(x))
            
            axes[0].plot(x, running_means, label=f'{col}', color=self.colors[i % len(self.colors)])
            axes[0].axhline(true_mean, color=self.colors[i % len(self.colors)], linestyle='--', alpha=0.7)
        
        axes[0].set_title('Running Mean Convergence')
        axes[0].set_xlabel('Iteration')
        axes[0].set_ylabel('Running Mean')
        axes[0].legend()
        axes[0].grid(True, alpha=0.3)
        
        # Standard error convergence
        theoretical_se = 1 / np.sqrt(x)  # Theoretical standard error
        axes[1].plot(x, theoretical_se, 'k-', label='Theoretical SE', linewidth=2)
        axes[1].fill_between(x, 0, theoretical_se, alpha=0.3, color='gray')
        
        axes[1].set_title('Standard Error Convergence')
        axes[1].set_xlabel('Iteration')
        axes[1].set_ylabel('Standard Error')
        axes[1].legend()
        axes[1].grid(True, alpha=0.3)
        axes[1].set_yscale('log')
        
        plt.tight_layout()
        
        # Save plot
        filename = f"{sim_name}_convergence.png"
        filepath = os.path.join(self.plots_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        printIt(f"📉 Convergence plot saved to: {filepath}", lable.PASS)
        return True
    
    def _plot_correlation_matrix(self, sim_name: str, results: Dict) -> bool:
        """Create correlation matrix heatmap"""
        columns = results.get('columns', [])
        data = results.get('data', {})
        
        if len(columns) < 2:
            printIt("Need at least 2 variables for correlation matrix", lable.WARN)
            return False
        
        # Calculate correlation matrix
        df_data = pd.DataFrame({col: data[col] for col in columns if col in data})
        corr_matrix = df_data.corr()
        
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Create heatmap
        im = ax.imshow(corr_matrix, cmap='RdBu_r', aspect='auto', vmin=-1, vmax=1)
        
        # Add colorbar
        cbar = plt.colorbar(im, ax=ax)
        cbar.set_label('Correlation Coefficient', rotation=270, labelpad=20)
        
        # Set ticks and labels
        ax.set_xticks(range(len(columns)))
        ax.set_yticks(range(len(columns)))
        ax.set_xticklabels(columns, rotation=45, ha='right')
        ax.set_yticklabels(columns)
        
        # Add correlation values as text
        for i in range(len(columns)):
            for j in range(len(columns)):
                text = ax.text(j, i, f'{corr_matrix.iloc[i, j]:.2f}',
                             ha="center", va="center", color="black", fontweight='bold')
        
        ax.set_title(f'Correlation Matrix: {sim_name}', fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        
        # Save plot
        filename = f"{sim_name}_correlation_matrix.png"
        filepath = os.path.join(self.plots_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        printIt(f"🔥 Correlation matrix saved to: {filepath}", lable.PASS)
        return True
    
    def _plot_scenarios(self, sim_name: str, results: Dict) -> bool:
        """Create scenario analysis plots"""
        scenarios = results.get('scenarios', [])
        columns = results.get('columns', [])
        
        if not scenarios or not columns:
            printIt("No scenario data available for plotting", lable.WARN)
            return False
        
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Prepare data for plotting
        scenario_names = [s['name'].replace('_', ' ').title() for s in scenarios]
        x_pos = np.arange(len(scenario_names))
        
        # Plot each variable as grouped bars
        bar_width = 0.8 / len(columns)
        
        for i, col in enumerate(columns):
            values = [s['values'][col] for s in scenarios if col in s['values']]
            if values:
                positions = x_pos + (i - len(columns)/2 + 0.5) * bar_width
                bars = ax.bar(positions, values, bar_width, 
                             label=col, color=self.colors[i % len(self.colors)], alpha=0.8)
                
                # Add value labels on bars
                for bar, value in zip(bars, values):
                    height = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width()/2., height,
                           f'{value:.2f}', ha='center', va='bottom', fontsize=8)
        
        ax.set_xlabel('Scenarios')
        ax.set_ylabel('Values')
        ax.set_title(f'Scenario Analysis: {sim_name}', fontsize=14, fontweight='bold')
        ax.set_xticks(x_pos)
        ax.set_xticklabels(scenario_names)
        ax.legend()
        ax.grid(True, alpha=0.3, axis='y')
        
        plt.tight_layout()
        
        # Save plot
        filename = f"{sim_name}_scenarios.png"
        filepath = os.path.join(self.plots_dir, filename)
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        printIt(f"🎭 Scenario plot saved to: {filepath}", lable.PASS)
        return True
    
    def _load_simulation_results(self, sim_name: str) -> Optional[Dict]:
        """Load simulation results from disk"""
        filepath = os.path.join(self.simulations_dir, f"{sim_name}_results.json")
        
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r') as f:
                    return json.load(f)
            except Exception as e:
                printIt(f"Error loading results: {str(e)}", lable.ERROR)
                return None
        else:
            printIt(f"Results file not found: {filepath}", lable.WARN)
            return None
    
    def list_plots(self) -> List[str]:
        """List all available plot files"""
        if not os.path.exists(self.plots_dir):
            return []
        
        plot_files = [f for f in os.listdir(self.plots_dir) if f.endswith('.png')]
        return sorted(plot_files)
    
    def show_plot_info(self):
        """Display information about available plots"""
        plots = self.list_plots()
        
        if not plots:
            printIt("No plots found", lable.INFO)
            return
        
        printIt(f"📊 Available plots ({len(plots)} total):", lable.INFO)
        printIt("=" * 50, lable.INFO)
        
        # Group by simulation name
        sim_plots = {}
        for plot in plots:
            sim_name = plot.split('_')[0]
            if sim_name not in sim_plots:
                sim_plots[sim_name] = []
            sim_plots[sim_name].append(plot)
        
        for sim_name, plot_list in sim_plots.items():
            printIt(f"\n🎯 {sim_name}:", lable.PASS)
            for plot in plot_list:
                plot_type = plot.replace(f"{sim_name}_", "").replace(".png", "")
                printIt(f"   {plot_type}", lable.DEBUG)

# Global instance
visualizer = MonteCarloVisualizer()
