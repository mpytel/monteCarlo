import numpy as np
import pandas as pd
from scipy import stats
from ..defs.logIt import printIt, lable, cStr, color
from .commands import Commands
from .dataStore import load_dataset, list_datasets, save_correlations, load_correlations

cmdObj = Commands()
commands = cmdObj.commands

def setCorrelation(argParse):
    """
    Define statistical relationships between data columns for Monte Carlo simulation.
    Analyzes correlation patterns that emerge from seemingly random web data.
    """
    args = argParse.args
    theArgs = args.arguments
    cmd_options = argParse.cmd_options
    
    if len(theArgs) < 3:
        printIt("Usage: monteCarlo setCorrelation <dataset> <column1> <column2> [method]", lable.WARN)
        printIt("Available datasets:", lable.INFO)
        datasets = list_datasets()
        for name in datasets:
            printIt(f"  - {cStr(name, color.CYAN)}", lable.INFO)
        return
    
    dataset_name = theArgs[0]
    column1 = theArgs[1]
    column2 = theArgs[2]
    method = theArgs[3] if len(theArgs) > 3 else 'pearson'
    
    # Load dataset
    data, metadata = load_dataset(dataset_name)
    if data is None:
        printIt(f"Dataset '{dataset_name}' not found", lable.ERROR)
        return
    
    # Validate columns exist
    if hasattr(data, 'columns'):
        available_cols = list(data.columns)
        if column1 not in available_cols or column2 not in available_cols:
            printIt(f"Columns not found. Available: {available_cols}", lable.ERROR)
            return
    
    printIt(f"Analyzing correlation between {cStr(column1, color.CYAN)} and {cStr(column2, color.YELLOW)}", lable.INFO)
    
    try:
        # Extract column data
        col1_data = data[column1].dropna()
        col2_data = data[column2].dropna()
        
        # Align data (common indices)
        common_idx = col1_data.index.intersection(col2_data.index)
        col1_aligned = col1_data.loc[common_idx]
        col2_aligned = col2_data.loc[common_idx]
        
        if len(col1_aligned) < 3:
            printIt("Insufficient data points for correlation analysis", lable.ERROR)
            return
        
        # Calculate correlation based on method
        correlation_result = _calculate_correlation(col1_aligned, col2_aligned, method)
        
        # Store correlation information
        correlations = load_correlations()
        corr_key = f"{dataset_name}_{column1}_{column2}"
        correlations[corr_key] = {
            'dataset': dataset_name,
            'column1': column1,
            'column2': column2,
            'method': method,
            'correlation': correlation_result['correlation'],
            'p_value': correlation_result['p_value'],
            'significance': correlation_result['significance'],
            'sample_size': len(col1_aligned)
        }
        
        # Save correlations
        save_correlations(correlations)
        
        # Display results
        _display_correlation_results(correlation_result, column1, column2, method)
        
        # Analyze randomness vs pattern
        _analyze_correlation_randomness(correlation_result, col1_aligned, col2_aligned)
        
        # Generate correlation matrix for dataset if multiple correlations exist
        _update_correlation_matrix(dataset_name)
        
        printIt(f"Correlation analysis saved as: {cStr(corr_key, color.GREEN)}", lable.PASS)
        
    except Exception as e:
        printIt(f"Error calculating correlation: {str(e)}", lable.ERROR)

def _calculate_correlation(data1, data2, method):
    """Calculate correlation using specified method"""
    result = {}
    
    if method.lower() == 'pearson':
        corr, p_val = stats.pearsonr(data1, data2)
        result['method_full'] = 'Pearson Product-Moment'
    elif method.lower() == 'spearman':
        corr, p_val = stats.spearmanr(data1, data2)
        result['method_full'] = 'Spearman Rank'
    elif method.lower() == 'kendall':
        corr, p_val = stats.kendalltau(data1, data2)
        result['method_full'] = 'Kendall Tau'
    else:
        printIt(f"Unknown method '{method}', using Pearson", lable.WARN)
        corr, p_val = stats.pearsonr(data1, data2)
        result['method_full'] = 'Pearson Product-Moment (default)'
    
    result['correlation'] = float(corr)
    result['p_value'] = float(p_val)
    result['significance'] = 'significant' if p_val < 0.05 else 'not significant'
    
    return result

def _display_correlation_results(result, col1, col2, method):
    """Display correlation analysis results with color coding"""
    printIt(f"\n{cStr('Correlation Analysis Results', color.YELLOW)}", lable.INFO)
    printIt(f"Method: {result['method_full']}", lable.INFO)
    corr_value = f'{result["correlation"]:.4f}'
    printIt(f"Correlation coefficient: {cStr(corr_value, color.CYAN)}", lable.INFO)
    printIt(f"P-value: {result['p_value']:.6f}", lable.INFO)
    printIt(f"Statistical significance: {cStr(result['significance'], color.GREEN if result['significance'] == 'significant' else color.YELLOW)}", lable.INFO)
    
    # Interpret correlation strength
    abs_corr = abs(result['correlation'])
    if abs_corr >= 0.8:
        strength = cStr("Very Strong", color.RED)
    elif abs_corr >= 0.6:
        strength = cStr("Strong", color.YELLOW)
    elif abs_corr >= 0.4:
        strength = cStr("Moderate", color.CYAN)
    elif abs_corr >= 0.2:
        strength = cStr("Weak", color.WHITE)
    else:
        strength = cStr("Very Weak/Random", color.GREEN)
    
    direction = "Positive" if result['correlation'] > 0 else "Negative"
    printIt(f"Relationship: {strength} {direction} correlation", lable.INFO)

def _analyze_correlation_randomness(result, data1, data2):
    """Analyze the randomness vs pattern in correlation"""
    printIt(f"\n{cStr('Randomness vs Pattern Analysis', color.MAGENTA)}", lable.INFO)
    
    # Calculate additional randomness metrics
    abs_corr = abs(result['correlation'])
    
    # Mutual information (measure of dependency)
    mutual_info = _calculate_mutual_information(data1, data2)
    
    # Randomness score (inverse of correlation strength)
    randomness_score = 1 - abs_corr
    
    # Pattern emergence probability
    pattern_prob = 1 - result['p_value'] if result['p_value'] < 1 else 0
    
    printIt(f"Mutual Information: {mutual_info:.4f}", lable.INFO)
    printIt(f"Randomness Score: {randomness_score:.4f} (1.0 = completely random)", lable.INFO)
    printIt(f"Pattern Emergence Probability: {pattern_prob:.4f}", lable.INFO)
    
    # Philosophical interpretation
    if abs_corr < 0.1 and result['p_value'] > 0.5:
        printIt(f"Assessment: {cStr('Data appears truly random - no discernible pattern', color.GREEN)}", lable.INFO)
    elif abs_corr > 0.5 and result['p_value'] < 0.01:
        printIt(f"Assessment: {cStr('Strong pattern emerged from apparent randomness', color.RED)}", lable.INFO)
    else:
        printIt(f"Assessment: {cStr('Weak patterns in seemingly random data', color.YELLOW)}", lable.INFO)

def _calculate_mutual_information(data1, data2):
    """Calculate mutual information between two variables"""
    try:
        # Discretize data into bins
        bins = min(20, len(data1) // 10 + 1)
        
        # Create joint histogram
        hist_2d, _, _ = np.histogram2d(data1, data2, bins=bins)
        hist_2d = hist_2d + 1e-10  # Avoid log(0)
        
        # Marginal histograms
        hist_1 = np.sum(hist_2d, axis=1)
        hist_2 = np.sum(hist_2d, axis=0)
        
        # Convert to probabilities
        p_xy = hist_2d / np.sum(hist_2d)
        p_x = hist_1 / np.sum(hist_1)
        p_y = hist_2 / np.sum(hist_2)
        
        # Calculate mutual information
        mi = 0
        for i in range(len(p_x)):
            for j in range(len(p_y)):
                if p_xy[i, j] > 0:
                    mi += p_xy[i, j] * np.log2(p_xy[i, j] / (p_x[i] * p_y[j]))
        
        return float(mi)
    except:
        return 0.0

def _update_correlation_matrix(dataset_name):
    """Update correlation matrix for the dataset"""
    correlations = load_correlations()
    dataset_correlations = {k: v for k, v in correlations.items() if v['dataset'] == dataset_name}
    
    if len(dataset_correlations) > 1:
        printIt(f"\n{cStr('Correlation Matrix Summary for ' + dataset_name, color.YELLOW)}", lable.INFO)
        
        # Get all unique columns involved in correlations
        columns = set()
        for corr_data in dataset_correlations.values():
            columns.add(corr_data['column1'])
            columns.add(corr_data['column2'])
        
        columns = sorted(list(columns))
        
        # Display correlation pairs
        for corr_key, corr_data in dataset_correlations.items():
            col1, col2 = corr_data['column1'], corr_data['column2']
            corr_val = corr_data['correlation']
            significance = corr_data['significance']
            
            color_code = color.RED if abs(corr_val) > 0.6 else color.YELLOW if abs(corr_val) > 0.3 else color.GREEN
            printIt(f"  {col1} ↔ {col2}: {cStr(f'{corr_val:.3f}', color_code)} ({significance})", lable.INFO)

def dataset(argParse):
    """Handle dataset argument"""
    printIt("Dataset parameter processed", lable.DEBUG)

def column1(argParse):
    """Handle column1 argument"""
    printIt("Column1 parameter processed", lable.DEBUG)

def column2(argParse):
    """Handle column2 argument"""
    printIt("Column2 parameter processed", lable.DEBUG)

def method(argParse):
    """Handle method argument"""
    printIt("Method parameter processed", lable.DEBUG)
