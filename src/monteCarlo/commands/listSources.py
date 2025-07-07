"""
List Available Data Sources - Discover the Randomness of Web Information

This command helps users explore what data is available for Monte Carlo analysis.
Philosophy: We don't assume anyone knows what's out there - let's discover together!
"""

from ..defs.logIt import printIt, lable, cStr, color
from ..defs.dataSources import data_registry
from .commands import Commands

cmdObj = Commands()
commands = cmdObj.commands

def listSources(argParse):
    """Main listSources command - discover available data sources"""
    global commands
    args = argParse.args
    theCmd = args.commands[0]
    theArgNames = list(commands[theCmd].keys())
    theArgs = args.arguments
    argIndex = 0
    nonCmdArg = True
    
    # If no arguments, show all categories
    if len(theArgs) == 0:
        data_registry.list_categories()
        printIt("\n💡 Usage Examples:", lable.INFO)
        printIt("  monteCarlo listSources financial    # Show financial data sources", lable.EXAMPLE)
        printIt("  monteCarlo listSources all          # Show all sources", lable.EXAMPLE)
        printIt("  monteCarlo listSources random       # Get random suggestion", lable.EXAMPLE)
        printIt("  monteCarlo listSources search crypto # Search for crypto-related sources", lable.EXAMPLE)
        return
    
    # Process arguments
    while argIndex < len(theArgs):
        anArg = theArgs[argIndex]
        
        # Handle special commands
        if anArg == "all":
            data_registry.list_sources()
        elif anArg == "random":
            data_registry.get_random_suggestion()
        elif anArg == "search":
            if argIndex + 1 < len(theArgs):
                keyword = theArgs[argIndex + 1]
                data_registry.search_sources(keyword)
                argIndex += 1  # Skip the keyword
            else:
                printIt("Search requires a keyword", lable.WARN)
        elif anArg in commands[theCmd]:
            # This is a defined command argument
            nonCmdArg = False
            exec(f"{anArg}(argParse)")
        elif anArg in data_registry.sources:
            # This is a valid category
            data_registry.list_sources(anArg)
        else:
            # Try as a search term
            printIt(f"🔍 Searching for '{anArg}'...", lable.INFO)
            results = data_registry.search_sources(anArg)
            if not results:
                printIt(f"Category '{anArg}' not found. Available categories:", lable.WARN)
                data_registry.list_categories()
        
        argIndex += 1

def category(argParse):
    """Handle category-specific requests"""
    args = argParse.args
    theArgs = args.arguments
    
    if len(theArgs) > 1:
        category_name = theArgs[1]  # The category argument
        if category_name in data_registry.sources:
            data_registry.list_sources(category_name)
        else:
            printIt(f"Category '{category_name}' not found", lable.WARN)
            data_registry.list_categories()
    else:
        printIt("Category argument requires a category name", lable.WARN)
        data_registry.list_categories()


