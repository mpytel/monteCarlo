import json
import pickle
import os
import numpy as np
import pandas as pd
from ..defs.logIt import printIt, lable

# Data storage directory
DATA_DIR = os.path.expanduser("~/.monteCarlo_data")

def ensure_data_dir():
    """Ensure data directory exists"""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def save_dataset(name, data, metadata=None):
    """Save dataset to persistent storage"""
    ensure_data_dir()
    
    # Save data as pickle for complex objects
    data_file = os.path.join(DATA_DIR, f"{name}_data.pkl")
    with open(data_file, 'wb') as f:
        pickle.dump(data, f)
    
    # Save metadata as JSON
    if metadata:
        meta_file = os.path.join(DATA_DIR, f"{name}_meta.json")
        with open(meta_file, 'w') as f:
            json.dump(metadata, f, indent=2)

def load_dataset(name):
    """Load dataset from persistent storage"""
    ensure_data_dir()
    
    data_file = os.path.join(DATA_DIR, f"{name}_data.pkl")
    meta_file = os.path.join(DATA_DIR, f"{name}_meta.json")
    
    if not os.path.exists(data_file):
        return None, None
    
    # Load data
    with open(data_file, 'rb') as f:
        data = pickle.load(f)
    
    # Load metadata if exists
    metadata = None
    if os.path.exists(meta_file):
        with open(meta_file, 'r') as f:
            metadata = json.load(f)
    
    return data, metadata

def list_datasets():
    """List all available datasets"""
    ensure_data_dir()
    
    datasets = []
    for file in os.listdir(DATA_DIR):
        if file.endswith('_data.pkl'):
            dataset_name = file[:-9]  # Remove '_data.pkl'
            datasets.append(dataset_name)
    
    return datasets

def save_correlations(correlations):
    """Save correlation data"""
    ensure_data_dir()
    
    corr_file = os.path.join(DATA_DIR, "correlations.json")
    
    # Convert numpy arrays to lists for JSON serialization
    serializable_corr = {}
    for key, value in correlations.items():
        serializable_corr[key] = {
            'dataset': value['dataset'],
            'column1': value['column1'],
            'column2': value['column2'],
            'method': value['method'],
            'correlation': float(value['correlation']),
            'p_value': float(value['p_value']),
            'significance': value['significance'],
            'sample_size': int(value['sample_size'])
        }
    
    with open(corr_file, 'w') as f:
        json.dump(serializable_corr, f, indent=2)

def load_correlations():
    """Load correlation data"""
    ensure_data_dir()
    
    corr_file = os.path.join(DATA_DIR, "correlations.json")
    
    if not os.path.exists(corr_file):
        return {}
    
    with open(corr_file, 'r') as f:
        return json.load(f)

def save_simulations(simulations):
    """Save simulation results"""
    ensure_data_dir()
    
    sim_file = os.path.join(DATA_DIR, "simulations.pkl")
    
    with open(sim_file, 'wb') as f:
        pickle.dump(simulations, f)

def load_simulations():
    """Load simulation results"""
    ensure_data_dir()
    
    sim_file = os.path.join(DATA_DIR, "simulations.pkl")
    
    if not os.path.exists(sim_file):
        return {}
    
    with open(sim_file, 'rb') as f:
        return pickle.load(f)

def clear_all_data():
    """Clear all stored data"""
    ensure_data_dir()
    
    for file in os.listdir(DATA_DIR):
        file_path = os.path.join(DATA_DIR, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
    
    printIt("All stored data cleared", lable.INFO)
