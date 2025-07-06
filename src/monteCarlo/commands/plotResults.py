"""
Plot Results - Visualizing Randomness Patterns

This command creates visualizations for Monte Carlo simulation results.
Philosophy: Patterns in randomness become visible when we plot them.
"""

from ..defs.logIt import printIt, lable, cStr, color
from ..defs.visualizer import visualizer
from ..defs.monteCarloEngine import monte_carlo_engine
from .commands import Commands

cmdObj = Commands()
commands = cmdObj.commands

def plotResults(argParse):
    """Main plotResults command - create visualizations for simulation results"""
    global commands
    args = argParse.args
    theCmd = args.commands[0]
    theArgs = args.arguments
    
    if len(theArgs) < 1:
        printIt("📊 Usage: monteCarlo plotResults <sim_name> [plot_type]", lable.WARN)
        printIt("\nAvailable plot types:", lable.INFO)
        printIt("  histogram    - Distribution plots for each variable", lable.DEBUG)
        printIt("  scatter      - Scatter matrix showing relationships", lable.DEBUG)
        printIt("  convergence  - Monte Carlo convergence analysis", lable.DEBUG)
        printIt("  correlation  - Correlation matrix heatmap", lable.DEBUG)
        printIt("  scenarios    - Scenario analysis comparison", lable.DEBUG)
        printIt("  all          - Generate all plot types", lable.DEBUG)
        
        # Show available simulations
        simulations = monte_carlo_engine.list_simulations()
        if simulations:
            printIt(f"\n🎯 Available simulations:", lable.INFO)
            for name, config in simulations.items():
                status = config.get('status', 'unknown')
                if status == 'completed':
                    printIt(f"   {cStr(name, color.GREEN)} - ready for plotting", lable.DEBUG)
                else:
                    printIt(f"   {cStr(name, color.YELLOW)} - {status}", lable.DEBUG)
        
        return
    
    sim_name = theArgs[0]
    plot_type = theArgs[1] if len(theArgs) > 1 else 'histogram'
    
    printIt(f"🎨 Creating {plot_type} plots for simulation '{sim_name}'", lable.INFO)
    
    # Check if simulation exists and is completed
    simulations = monte_carlo_engine.list_simulations()
    if sim_name not in simulations:
        printIt(f"Simulation '{sim_name}' not found", lable.ERROR)
        
        # Suggest similar names
        similar_names = [name for name in simulations.keys() if sim_name.lower() in name.lower()]
        if similar_names:
            printIt(f"Did you mean: {', '.join(similar_names)}", lable.INFO)
        return
    
    sim_config = simulations[sim_name]
    if sim_config.get('status') != 'completed':
        printIt(f"Simulation '{sim_name}' has not been completed yet", lable.WARN)
        printIt(f"Current status: {sim_config.get('status', 'unknown')}", lable.INFO)
        printIt(f"Run: monteCarlo runSim {sim_name}", lable.DEBUG)
        return
    
    # Create the plots
    success = visualizer.plot_results(sim_name, plot_type)
    
    if success:
        printIt(f"✅ {plot_type.title()} plots created successfully!", lable.PASS)
        
        # Show where plots are saved
        plots = visualizer.list_plots()
        sim_plots = [p for p in plots if p.startswith(sim_name)]
        
        if sim_plots:
            printIt(f"\n📁 Generated plots:", lable.INFO)
            for plot in sim_plots:
                printIt(f"   {plot}", lable.DEBUG)
        
        printIt(f"\n💡 Next steps:", lable.INFO)
        if plot_type != 'all':
            printIt(f"   monteCarlo plotResults {sim_name} all     # Generate all plot types", lable.DEBUG)
        printIt(f"   monteCarlo listPlots                      # View all available plots", lable.DEBUG)
        printIt(f"   open {visualizer.plots_dir}               # Open plots folder", lable.DEBUG)
        
    else:
        printIt(f"❌ Failed to create {plot_type} plots", lable.ERROR)

def sim_name(argParse):
    """Handle simulation name argument"""
    args = argParse.args
    theArgs = args.arguments
    
    if len(theArgs) > 0:
        name = theArgs[0]
        printIt(f"Plotting results for: {name}", lable.DEBUG)
        
        # Validate simulation exists
        simulations = monte_carlo_engine.list_simulations()
        if name not in simulations:
            printIt(f"Warning: Simulation '{name}' not found", lable.WARN)
            
            # Show available simulations
            if simulations:
                printIt("Available simulations:", lable.INFO)
                for sim_name in list(simulations.keys())[:5]:
                    printIt(f"  {sim_name}", lable.DEBUG)

def plot_type(argParse):
    """Handle plot type argument"""
    args = argParse.args
    theArgs = args.arguments
    
    if len(theArgs) > 1:
        ptype = theArgs[1]
        printIt(f"Plot type: {ptype}", lable.DEBUG)
        
        # Validate plot type
        valid_types = ['histogram', 'scatter', 'convergence', 'correlation', 'scenarios', 'all']
        if ptype not in valid_types:
            printIt(f"Warning: Unknown plot type '{ptype}'", lable.WARN)
            printIt(f"Valid types: {', '.join(valid_types)}", lable.INFO)
