"""
List Plots Command - Display Generated Visualizations

This command lists all generated visualization plots with details about
their simulation source, plot type, file size, and creation time.
"""

import os
import glob
from datetime import datetime
from ..defs.logIt import printIt, lable, cStr, color

def listPlots(argParse):
    """List all generated visualization plots"""
    args = argParse.args
    theCmd = args.commands[0]
    theArgs = args.arguments
    
    # Get plots directory
    plots_dir = "/Users/primwind/proj/test/monteCarlo/data/plots"
    
    if not os.path.exists(plots_dir):
        printIt("📁 No plots directory found", lable.WARN)
        printIt("Generate some plots first:", lable.INFO)
        printIt("   monteCarlo plotResults simulation_name all", lable.STEP)
        return
    
    # Get filter if provided
    filter_term = theArgs[0].lower() if len(theArgs) > 0 else None
    
    # Find all plot files
    plot_files = glob.glob(os.path.join(plots_dir, "*.png"))
    
    if not plot_files:
        printIt("📁 No plots found", lable.WARN)
        printIt("Generate some plots first:", lable.INFO)
        printIt("   monteCarlo plotResults simulation_name all", lable.STEP)
        return
    
    # Filter plots if requested
    if filter_term:
        plot_files = [f for f in plot_files if filter_term in os.path.basename(f).lower()]
        if not plot_files:
            printIt(f"📁 No plots found matching '{filter_term}'", lable.WARN)
            return
    
    # Sort by modification time (newest first)
    plot_files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    
    # Display header
    printIt("📊 Generated Visualization Plots", lable.INFO)
    printIt("=" * 60, lable.INFO)
    
    # Group plots by simulation
    simulations = {}
    plot_types = {
        'histograms': '📈 Histograms',
        'scatter_matrix': '🔗 Scatter Matrix', 
        'correlation_matrix': '🔥 Correlation Matrix',
        'convergence': '📉 Convergence Analysis',
        'scenarios': '🎭 Scenario Comparison'
    }
    
    for plot_file in plot_files:
        filename = os.path.basename(plot_file)
        
        # Parse filename to extract simulation name and plot type
        if '_' in filename:
            parts = filename.replace('.png', '').split('_')
            if len(parts) >= 2:
                # Find the plot type
                plot_type = None
                sim_name = None
                
                for ptype in plot_types.keys():
                    if ptype in filename:
                        plot_type = ptype
                        sim_name = filename.replace(f'_{ptype}.png', '')
                        break
                
                if not plot_type:
                    # Fallback - assume last part is plot type
                    sim_name = '_'.join(parts[:-1])
                    plot_type = parts[-1]
                
                if sim_name not in simulations:
                    simulations[sim_name] = []
                
                # Get file info
                file_size = os.path.getsize(plot_file)
                file_time = datetime.fromtimestamp(os.path.getmtime(plot_file))
                
                simulations[sim_name].append({
                    'type': plot_type,
                    'file': filename,
                    'path': plot_file,
                    'size': file_size,
                    'time': file_time
                })
    
    # Display plots grouped by simulation
    total_plots = 0
    total_size = 0
    
    for sim_name, plots in simulations.items():
        printIt(f"\n🎲 {cStr(sim_name, color.CYAN)}", lable.INFO)
        
        # Sort plots by type for consistent display
        plots.sort(key=lambda x: x['type'])
        
        for plot in plots:
            plot_type_display = plot_types.get(plot['type'], f"📊 {plot['type'].title()}")
            size_mb = plot['size'] / (1024 * 1024)
            time_str = plot['time'].strftime("%Y-%m-%d %H:%M")
            
            printIt(f"   {plot_type_display}", lable.CONFIG)
            printIt(f"     File: {plot['file']}", lable.STAT)
            printIt(f"     Size: {size_mb:.1f} MB", lable.STAT)
            printIt(f"     Created: {time_str}", lable.STAT)
            
            total_plots += 1
            total_size += plot['size']
    
    # Display summary
    printIt(f"\n📈 Summary:", lable.INFO)
    printIt(f"   Total plots: {total_plots}", lable.STAT)
    printIt(f"   Total simulations: {len(simulations)}", lable.STAT)
    printIt(f"   Total size: {total_size / (1024 * 1024):.1f} MB", lable.STAT)
    printIt(f"   Plots directory: {plots_dir}", lable.CONFIG)
    
    # Show plot type breakdown
    type_counts = {}
    for plots in simulations.values():
        for plot in plots:
            plot_type = plot['type']
            type_counts[plot_type] = type_counts.get(plot_type, 0) + 1
    
    if type_counts:
        printIt(f"\n📊 Plot Types:", lable.INFO)
        for plot_type, count in sorted(type_counts.items()):
            type_display = plot_types.get(plot_type, plot_type.title())
            printIt(f"   {type_display}: {count}", lable.STAT)
    
    # Quick actions
    printIt(f"\n💡 Quick Actions:", lable.INFO)
    if len(simulations) > 0:
        first_sim = list(simulations.keys())[0]
        printIt(f"   monteCarlo plotResults {first_sim} all    # Generate all plot types", lable.STEP)
    printIt(f"   open {plots_dir}                          # Open plots folder", lable.STEP)
    
    # Show recent plots
    recent_plots = sorted(plot_files, key=lambda x: os.path.getmtime(x), reverse=True)[:3]
    if recent_plots:
        printIt(f"\n🕒 Most Recent Plots:", lable.INFO)
        for plot_file in recent_plots:
            filename = os.path.basename(plot_file)
            file_time = datetime.fromtimestamp(os.path.getmtime(plot_file))
            time_str = file_time.strftime("%H:%M")
            printIt(f"   {filename} ({time_str})", lable.CONFIG)

def filter(argParse):
    """Handle filter argument"""
    args = argParse.args
    if len(args) > 0:
        filter_term = args[0]
        printIt(f"Filter: {filter_term}", lable.CONFIG)
        
        # Provide suggestions for common filters
        suggestions = [
            "histogram", "scatter", "correlation", "convergence", "scenarios",
            "wave", "physics", "sim", "analysis"
        ]
        
        if filter_term not in suggestions:
            printIt("Common filters:", lable.INFO)
            for suggestion in suggestions[:5]:
                printIt(f"   monteCarlo listPlots {suggestion}", lable.EXAMPLE)
