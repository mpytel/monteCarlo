"""
Setup Simulation - Configure Monte Carlo Analysis

This command sets up Monte Carlo simulations to analyze randomness patterns.
Philosophy: Configure the parameters to explore uncertainty in web data.
"""

from ..defs.logIt import printIt, lable, cStr, color
from ..defs.monteCarloEngine import monte_carlo_engine
from ..defs.dataFetcher import data_fetcher
from .commands import Commands

cmdObj = Commands()
commands = cmdObj.commands

def setupSim(argParse):
    """Main setupSim command - configure Monte Carlo simulation"""
    global commands
    args = argParse.args
    theCmd = args.commands[0]
    theArgs = args.arguments
    
    if len(theArgs) < 3:
        printIt("🎲 Usage: monteCarlo setupSim <name> <iterations> <columns> [dataset]", lable.WARN)
        printIt("\nExamples:", lable.INFO)
        printIt("  monteCarlo setupSim stock_analysis 10000 'Close,Volume'", lable.EXAMPLE)
        printIt("  monteCarlo setupSim weather_sim 5000 'temperature,humidity' weather_data", lable.EXAMPLE)
        printIt("  monteCarlo setupSim random_test 1000 'value' synthetic_normal", lable.EXAMPLE)
        return
    
    sim_name = theArgs[0]
    
    # Parse iterations
    try:
        iterations = int(theArgs[1])
        if iterations < 100:
            printIt("Warning: Very few iterations may not provide reliable results", lable.WARN)
        elif iterations > 1000000:
            printIt("Warning: Very high iterations may take a long time", lable.WARN)
    except ValueError:
        printIt(f"Invalid iterations: {theArgs[1]}. Must be a number.", lable.ERROR)
        return
    
    # Parse columns
    columns_str = theArgs[2]
    columns = [col.strip() for col in columns_str.split(',')]
    
    # Optional dataset
    dataset = theArgs[3] if len(theArgs) > 3 else None
    
    printIt(f"🎯 Setting up simulation '{sim_name}'", lable.INFO)
    printIt(f"   Iterations: {iterations:,}", lable.CONFIG)
    printIt(f"   Columns: {', '.join(columns)}", lable.CONFIG)
    if dataset:
        printIt(f"   Dataset: {dataset}", lable.CONFIG)
    
    # Setup the simulation
    success = monte_carlo_engine.setup_simulation(
        name=sim_name,
        iterations=iterations,
        columns=columns,
        dataset=dataset
    )
    
    if success:
        printIt(f"\n✅ Simulation '{sim_name}' configured successfully!", lable.PASS)
        printIt(f"\n💡 Next steps:", lable.INFO)
        printIt(f"   monteCarlo runSim {sim_name}     # Execute the simulation", lable.STEP)
        printIt(f"   monteCarlo listSims              # View all simulations", lable.STEP)
        
        # Show available datasets if none specified
        if not dataset:
            saved_data = data_fetcher.list_saved_data()
            if saved_data['sources'] or saved_data['processed']:
                printIt(f"\n📂 Available datasets:", lable.INFO)
                for ds in saved_data['sources'][:5]:
                    printIt(f"   {ds}", lable.DEBUG)
                if len(saved_data['sources']) > 5:
                    printIt(f"   ... and {len(saved_data['sources']) - 5} more", lable.DEBUG)
    else:
        printIt(f"❌ Failed to setup simulation '{sim_name}'", lable.ERROR)

def name(argParse):
    """Handle simulation name argument"""
    args = argParse.args
    theArgs = args.arguments
    
    if len(theArgs) > 0:
        sim_name = theArgs[0]
        printIt(f"Simulation name: {sim_name}", lable.DEBUG)
        
        # Check if name already exists
        existing_sims = monte_carlo_engine.list_simulations()
        if sim_name in existing_sims:
            printIt(f"Warning: Simulation '{sim_name}' already exists", lable.WARN)

def iterations(argParse):
    """Handle iterations argument"""
    args = argParse.args
    theArgs = args.arguments
    
    if len(theArgs) > 1:
        try:
            iter_count = int(theArgs[1])
            printIt(f"Iterations: {iter_count:,}", lable.DEBUG)
            
            # Provide guidance on iteration count
            if iter_count < 1000:
                printIt("Tip: Consider 1000+ iterations for stable results", lable.INFO)
            elif iter_count > 100000:
                printIt("Tip: High iteration counts may take significant time", lable.INFO)
                
        except ValueError:
            printIt(f"Invalid iterations: {theArgs[1]}", lable.ERROR)

def columns(argParse):
    """Handle columns argument"""
    args = argParse.args
    theArgs = args.arguments
    
    if len(theArgs) > 2:
        columns_str = theArgs[2]
        columns = [col.strip() for col in columns_str.split(',')]
        printIt(f"Columns: {', '.join(columns)}", lable.DEBUG)
        
        if len(columns) > 10:
            printIt("Warning: Many columns may slow down simulation", lable.WARN)

def dataset(argParse):
    """Handle dataset argument"""
    args = argParse.args
    theArgs = args.arguments
    
    if len(theArgs) > 3:
        dataset_name = theArgs[3]
        printIt(f"Dataset: {dataset_name}", lable.DEBUG)
        
        # Check if dataset exists
        data = data_fetcher.load_data(dataset_name)
        if data is None:
            printIt(f"Warning: Dataset '{dataset_name}' not found", lable.WARN)
            
            # Show available datasets
            saved_data = data_fetcher.list_saved_data()
            if saved_data['sources']:
                printIt("Available datasets:", lable.INFO)
                for ds in saved_data['sources'][:5]:
                    printIt(f"  {ds}", lable.DEBUG)


