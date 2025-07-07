"""
Fetch Data - Collecting Random Information from the Web

This command fetches data from various sources for Monte Carlo analysis.
Philosophy: The web contains infinite randomness - let's capture and analyze it.
"""

from ..defs.logIt import printIt, lable, cStr, color
from ..defs.dataFetcher import data_fetcher
from ..defs.dataSources import data_registry
from .commands import Commands
import pandas as pd
import numpy as np

cmdObj = Commands()
commands = cmdObj.commands

def fetchData(argParse):
    """Main fetchData command - fetch data from various web sources"""
    global commands
    args = argParse.args
    theCmd = args.commands[0]
    theArgs = args.arguments
    
    if len(theArgs) < 2:
        printIt("🌐 Usage: monteCarlo fetchData <source_type> <identifier> [options]", lable.WARN)
        printIt("\nExamples:", lable.INFO)
        printIt("  monteCarlo fetchData financial_stocks AAPL", lable.EXAMPLE)
        printIt("  monteCarlo fetchData synthetic_normal random_walk", lable.EXAMPLE)
        printIt("  monteCarlo fetchData weather_current 'New York'", lable.EXAMPLE)
        printIt("\nUse 'monteCarlo listSources' to see available sources", lable.INFO)
        return
    
    source_type = theArgs[0]
    identifier = theArgs[1]
    
    # Parse additional options
    options = {}
    if len(theArgs) > 2:
        for i in range(2, len(theArgs)):
            if '=' in theArgs[i]:
                key, value = theArgs[i].split('=', 1)
                options[key] = value
            else:
                # Default options based on position
                if i == 2:
                    options['period'] = theArgs[i]
                elif i == 3:
                    options['interval'] = theArgs[i]
    
    printIt(f"🎲 Fetching {source_type} data for {identifier}...", lable.INFO)
    
    # Fetch the data
    data = data_fetcher.fetch_data(source_type, identifier, **options)
    
    if data is None:
        printIt("❌ Failed to fetch data", lable.ERROR)
        return
    
    # Generate filename
    filename = f"{source_type}_{identifier}_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}"
    filename = filename.replace(' ', '_').replace('/', '_')
    
    # Save the data
    filepath = data_fetcher.save_data(data, filename)
    
    # Analyze randomness
    printIt(f"\n🔍 Randomness Analysis for {identifier}:", lable.INFO)
    printIt("=" * 50, lable.INFO)
    
    # Find numeric columns for analysis
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    
    for col in numeric_cols[:5]:  # Analyze first 5 numeric columns
        if col not in ['fetch_time']:  # Skip metadata columns
            analysis = data_fetcher.analyze_randomness(data, col)
            if analysis:
                printIt(f"\n📊 {col.upper()}:", lable.PASS)
                printIt(f"   Mean: {analysis['mean']:.4f}", lable.STAT)
                printIt(f"   Std Dev: {analysis['std']:.4f}", lable.STAT)
                printIt(f"   Randomness Score: {analysis['randomness_score']:.4f}", lable.STAT)
                
                # Interpret randomness
                if analysis['randomness_score'] > 2.0:
                    printIt(f"   Assessment: {cStr('High randomness - chaotic behavior', color.RED)}", lable.INFO)
                elif analysis['randomness_score'] > 1.0:
                    printIt(f"   Assessment: {cStr('Moderate randomness - some patterns', color.YELLOW)}", lable.INFO)
                else:
                    printIt(f"   Assessment: {cStr('Low randomness - strong patterns', color.GREEN)}", lable.INFO)
    
    # Display summary
    printIt(f"\n✅ Data Summary:", lable.PASS)
    printIt(f"   Records: {len(data)}", lable.INFO)
    printIt(f"   Columns: {len(data.columns)}", lable.INFO)
    printIt(f"   Saved as: {filename}", lable.INFO)
    printIt(f"   File: {filepath}", lable.DEBUG)
    
    # Suggest next steps
    printIt(f"\n💡 Next Steps:", lable.INFO)
    printIt(f"   monteCarlo analyzeCorr {filename}", lable.STEP)
    printIt(f"   monteCarlo setupSim my_sim 1000 {','.join(numeric_cols[:3])}", lable.STEP)

def source_type(argParse):
    """Handle source_type argument"""
    args = argParse.args
    theArgs = args.arguments
    
    if len(theArgs) > 0:
        source = theArgs[0]
        printIt(f"Source type: {source}", lable.DEBUG)
        
        # Validate source type
        valid_sources = []
        for category, cat_info in data_registry.sources.items():
            for source_name in cat_info['sources'].keys():
                valid_sources.append(f"{category}_{source_name}")
        
        if source not in valid_sources:
            printIt(f"Unknown source type: {source}", lable.WARN)
            printIt("Available sources:", lable.INFO)
            for src in valid_sources[:10]:  # Show first 10
                printIt(f"  {src}", lable.DEBUG)

def identifier(argParse):
    """Handle identifier argument"""
    args = argParse.args
    theArgs = args.arguments
    
    if len(theArgs) > 1:
        ident = theArgs[1]
        printIt(f"Identifier: {ident}", lable.DEBUG)

def period(argParse):
    """Handle period argument for time-series data"""
    args = argParse.args
    theArgs = args.arguments
    
    if len(theArgs) > 2:
        period = theArgs[2]
        printIt(f"Period: {period}", lable.DEBUG)
        
        # Validate period format
        valid_periods = ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
        if period not in valid_periods:
            printIt(f"Note: {period} may not be valid. Common periods: {', '.join(valid_periods)}", lable.WARN)
