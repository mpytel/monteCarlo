"""
List Simulations - View All Monte Carlo Simulations

This command lists all configured and completed Monte Carlo simulations.
Philosophy: Keep track of all our explorations into randomness.
"""

from ..defs.logIt import printIt, lable, cStr, color
from ..defs.monteCarloEngine import monte_carlo_engine
from ..defs.dataFetcher import data_fetcher
from .commands import Commands
from datetime import datetime

cmdObj = Commands()
commands = cmdObj.commands

def listSims(argParse):
    """Main listSims command - list all Monte Carlo simulations"""
    global commands
    args = argParse.args
    theCmd = args.commands[0]
    theArgs = args.arguments
    
    # Get filter if provided
    status_filter = theArgs[0] if len(theArgs) > 0 else None
    
    printIt("🎲 Monte Carlo Simulations", lable.INFO)
    printIt("=" * 60, lable.INFO)
    
    simulations = monte_carlo_engine.list_simulations()
    
    if not simulations:
        printIt("No simulations found", lable.WARN)
        printIt("\n💡 Create your first simulation:", lable.INFO)
        printIt("   monteCarlo setupSim my_first_sim 10000 'value'", lable.STEP)
        printIt("   monteCarlo fetchData synthetic_normal test_data", lable.STEP)
        return
    
    # Filter simulations if requested
    if status_filter:
        filtered_sims = {name: config for name, config in simulations.items() 
                        if config.get('status', '').lower() == status_filter.lower()}
        if not filtered_sims:
            printIt(f"No simulations with status '{status_filter}' found", lable.WARN)
            return
        simulations = filtered_sims
    
    # Sort by creation date
    sorted_sims = sorted(simulations.items(), 
                        key=lambda x: x[1].get('created', ''), reverse=True)
    
    for name, config in sorted_sims:
        status = config.get('status', 'unknown')
        iterations = config.get('iterations', 0)
        columns = config.get('columns', [])
        dataset = config.get('dataset', 'None')
        created = config.get('created', 'Unknown')
        last_run = config.get('last_run', 'Never')
        
        # Format creation date
        try:
            if created != 'Unknown':
                created_dt = datetime.fromisoformat(created.replace('Z', '+00:00'))
                created_str = created_dt.strftime('%Y-%m-%d %H:%M')
            else:
                created_str = 'Unknown'
        except:
            created_str = created[:16] if len(created) > 16 else created
        
        # Color code by status
        if status == 'completed':
            status_color = color.GREEN
            status_symbol = "✅"
        elif status == 'configured':
            status_color = color.YELLOW
            status_symbol = "⚙️"
        else:
            status_color = color.RED
            status_symbol = "❓"
        
        printIt(f"\n{status_symbol} {cStr(name, color.CYAN)}", lable.INFO)
        printIt(f"   Status: {cStr(status, status_color)}", lable.CONFIG)
        printIt(f"   Iterations: {iterations:,}", lable.CONFIG)
        printIt(f"   Variables: {', '.join(columns[:3])}{' ...' if len(columns) > 3 else ''}", lable.CONFIG)
        printIt(f"   Dataset: {dataset}", lable.CONFIG)
        printIt(f"   Created: {created_str}", lable.CONFIG)
        
        if last_run != 'Never':
            try:
                if last_run != 'Never':
                    run_dt = datetime.fromisoformat(last_run.replace('Z', '+00:00'))
                    run_str = run_dt.strftime('%Y-%m-%d %H:%M')
                else:
                    run_str = 'Never'
            except:
                run_str = last_run[:16] if len(last_run) > 16 else last_run
            printIt(f"   Last Run: {run_str}", lable.CONFIG)
        
        # Show data statistics if available
        if 'data_stats' in config and config['data_stats']:
            stats_summary = []
            for col, stats in list(config['data_stats'].items())[:2]:  # Show first 2
                randomness = stats.get('randomness_score', 0)
                stats_summary.append(f"{col}(R:{randomness:.2f})")
            if stats_summary:
                printIt(f"   Randomness: {', '.join(stats_summary)}", lable.STAT)
    
    # Summary statistics
    printIt(f"\n📊 Summary:", lable.INFO)
    status_counts = {}
    total_iterations = 0
    
    for config in simulations.values():
        status = config.get('status', 'unknown')
        status_counts[status] = status_counts.get(status, 0) + 1
        total_iterations += config.get('iterations', 0)
    
    printIt(f"   Total simulations: {len(simulations)}", lable.STAT)
    for status, count in status_counts.items():
        printIt(f"   {status.title()}: {count}", lable.STAT)
    printIt(f"   Total iterations: {total_iterations:,}", lable.STAT)
    
    # Show available datasets
    saved_data = data_fetcher.list_saved_data()
    if saved_data['sources']:
        printIt(f"\n📂 Available datasets: {len(saved_data['sources'])}", lable.INFO)
        for dataset in saved_data['sources'][:3]:
            printIt(f"   {dataset}", lable.DEBUG)
        if len(saved_data['sources']) > 3:
            printIt(f"   ... and {len(saved_data['sources']) - 3} more", lable.DEBUG)
    
    # Usage suggestions
    printIt(f"\n💡 Quick actions:", lable.INFO)
    
    # Find simulations ready to run
    ready_to_run = [name for name, config in simulations.items() 
                   if config.get('status') == 'configured']
    if ready_to_run:
        printIt(f"   monteCarlo runSim {ready_to_run[0]}        # Run simulation", lable.STEP)
    
    # Find completed simulations ready to plot
    ready_to_plot = [name for name, config in simulations.items() 
                    if config.get('status') == 'completed']
    if ready_to_plot:
        printIt(f"   monteCarlo plotResults {ready_to_plot[0]} all  # Create plots", lable.STEP)
    
    printIt(f"   monteCarlo listSims completed             # Show only completed", lable.STEP)
    printIt(f"   monteCarlo listSims configured            # Show only configured", lable.STEP)


