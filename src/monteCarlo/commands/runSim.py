"""
Run Simulation - Execute Monte Carlo Analysis

This command runs configured Monte Carlo simulations to explore randomness.
Philosophy: Execute thousands of scenarios to understand uncertainty patterns.
"""

from ..defs.logIt import printIt, lable, cStr, color
from ..defs.monteCarloEngine import monte_carlo_engine
from .commands import Commands
import time

cmdObj = Commands()
commands = cmdObj.commands

def runSim(argParse):
    """Main runSim command - execute Monte Carlo simulation"""
    global commands
    args = argParse.args
    theCmd = args.commands[0]
    theArgs = args.arguments
    
    if len(theArgs) < 1:
        printIt("🚀 Usage: monteCarlo runSim <simulation_name>", lable.WARN)
        
        # Show available simulations
        simulations = monte_carlo_engine.list_simulations()
        if simulations:
            printIt("\n📊 Available simulations:", lable.INFO)
            for name, config in simulations.items():
                status = config.get('status', 'unknown')
                iterations = config.get('iterations', 0)
                columns = config.get('columns', [])
                
                status_color = color.GREEN if status == 'completed' else color.YELLOW
                printIt(f"   {cStr(name, color.CYAN)} - {cStr(status, status_color)}", lable.INFO)
                printIt(f"     Iterations: {iterations:,}, Columns: {', '.join(columns[:3])}", lable.DEBUG)
        else:
            printIt("\n💡 No simulations found. Create one first:", lable.INFO)
            printIt("   monteCarlo setupSim my_sim 10000 'column1,column2'", lable.DEBUG)
        return
    
    sim_name = theArgs[0]
    
    printIt(f"🎲 Executing Monte Carlo simulation '{sim_name}'...", lable.INFO)
    
    # Record start time
    start_time = time.time()
    
    # Run the simulation
    success = monte_carlo_engine.run_simulation(sim_name)
    
    # Record end time
    end_time = time.time()
    execution_time = end_time - start_time
    
    if success:
        printIt(f"\n🎉 Simulation '{sim_name}' completed successfully!", lable.PASS)
        printIt(f"⏱️  Execution time: {execution_time:.2f} seconds", lable.INFO)
        
        printIt(f"\n💡 Next steps:", lable.INFO)
        printIt(f"   monteCarlo plotResults {sim_name} histogram    # Visualize distributions", lable.DEBUG)
        printIt(f"   monteCarlo sensitivity {sim_name}             # Analyze sensitivity", lable.DEBUG)
        printIt(f"   monteCarlo listSims                           # View all simulations", lable.DEBUG)
        
        # Show quick summary
        simulations = monte_carlo_engine.list_simulations()
        if sim_name in simulations:
            config = simulations[sim_name]
            printIt(f"\n📈 Quick Summary:", lable.INFO)
            printIt(f"   Iterations: {config['iterations']:,}", lable.DEBUG)
            printIt(f"   Variables: {', '.join(config['columns'])}", lable.DEBUG)
            if config.get('dataset'):
                printIt(f"   Dataset: {config['dataset']}", lable.DEBUG)
    else:
        printIt(f"❌ Failed to run simulation '{sim_name}'", lable.ERROR)
        printIt("Check that the simulation exists and is properly configured", lable.WARN)

def name(argParse):
    """Handle simulation name argument"""
    args = argParse.args
    theArgs = args.arguments
    
    if len(theArgs) > 0:
        sim_name = theArgs[0]
        printIt(f"Running simulation: {sim_name}", lable.DEBUG)
        
        # Check if simulation exists
        simulations = monte_carlo_engine.list_simulations()
        if sim_name not in simulations:
            printIt(f"Warning: Simulation '{sim_name}' not found", lable.WARN)
            
            # Suggest similar names
            similar_names = [name for name in simulations.keys() if sim_name.lower() in name.lower()]
            if similar_names:
                printIt(f"Did you mean: {', '.join(similar_names)}", lable.INFO)
        else:
            config = simulations[sim_name]
            status = config.get('status', 'unknown')
            if status != 'configured':
                printIt(f"Note: Simulation status is '{status}'", lable.INFO)
