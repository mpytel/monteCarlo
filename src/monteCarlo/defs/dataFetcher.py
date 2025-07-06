"""
Data Fetcher - Collecting Random Information from the Web

This module handles fetching data from various web sources for Monte Carlo analysis.
Philosophy: The web is full of random information - let's capture it and find patterns.
"""

import requests
import pandas as pd
import numpy as np
import yfinance as yf
import json
import os
import time
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from .logIt import printIt, lable
from .dataSources import data_registry

class DataFetcher:
    """Fetches data from various web sources"""
    
    def __init__(self, data_dir="/Users/primwind/proj/test/monteCarlo/data"):
        self.data_dir = data_dir
        self.sources_dir = os.path.join(data_dir, "sources")
        self.processed_dir = os.path.join(data_dir, "processed")
        
        # Ensure directories exist
        os.makedirs(self.sources_dir, exist_ok=True)
        os.makedirs(self.processed_dir, exist_ok=True)
    
    def fetch_data(self, source_type: str, identifier: str, **kwargs) -> Optional[pd.DataFrame]:
        """Main data fetching method"""
        printIt(f"🌐 Fetching {source_type} data for {identifier}...", lable.INFO)
        
        try:
            if source_type.startswith("financial"):
                return self._fetch_financial_data(source_type, identifier, **kwargs)
            elif source_type.startswith("weather"):
                return self._fetch_weather_data(identifier, **kwargs)
            elif source_type.startswith("synthetic"):
                return self._generate_synthetic_data(source_type, identifier, **kwargs)
            elif source_type.startswith("economic"):
                return self._fetch_economic_data(identifier, **kwargs)
            elif source_type.startswith("social"):
                return self._fetch_social_data(source_type, identifier, **kwargs)
            elif source_type.startswith("news"):
                return self._fetch_news_data(source_type, identifier, **kwargs)
            elif source_type.startswith("internet"):
                return self._fetch_internet_data(source_type, identifier, **kwargs)
            else:
                printIt(f"Source type '{source_type}' not yet implemented", lable.WARN)
                return None
                
        except Exception as e:
            printIt(f"Error fetching data: {str(e)}", lable.ERROR)
            return None
    
    def _fetch_financial_data(self, source_type: str, symbol: str, **kwargs) -> pd.DataFrame:
        """Fetch financial data using yfinance"""
        period = kwargs.get('period', '1y')
        interval = kwargs.get('interval', '1d')
        
        printIt(f"📈 Fetching financial data for {symbol} ({period}, {interval})", lable.DEBUG)
        
        # Use yfinance for financial data
        ticker = yf.Ticker(symbol)
        
        if "stocks" in source_type or "crypto" in source_type or "forex" in source_type:
            data = ticker.history(period=period, interval=interval)
        elif "commodities" in source_type:
            data = ticker.history(period=period, interval=interval)
        else:
            data = ticker.history(period=period, interval=interval)
        
        if data.empty:
            printIt(f"No data found for {symbol}", lable.WARN)
            return None
        
        # Add metadata
        data['symbol'] = symbol
        data['source_type'] = source_type
        data['fetch_time'] = datetime.now()
        
        # Calculate additional randomness metrics
        data['returns'] = data['Close'].pct_change()
        data['volatility'] = data['returns'].rolling(window=20).std()
        data['randomness_score'] = np.abs(data['returns']) / data['volatility']
        
        printIt(f"✅ Fetched {len(data)} records for {symbol}", lable.PASS)
        return data
    
    def _fetch_weather_data(self, location: str, **kwargs) -> pd.DataFrame:
        """Fetch weather data (placeholder - would use weather API)"""
        printIt(f"🌤️ Generating sample weather data for {location}", lable.DEBUG)
        
        # For now, generate synthetic weather data
        # In production, would use OpenWeatherMap, WeatherAPI, etc.
        days = kwargs.get('days', 365)
        
        dates = pd.date_range(start=datetime.now() - timedelta(days=days), 
                             end=datetime.now(), freq='D')
        
        # Generate realistic weather patterns with randomness
        base_temp = 20  # Base temperature
        seasonal_pattern = 10 * np.sin(2 * np.pi * np.arange(len(dates)) / 365)
        random_variation = np.random.normal(0, 5, len(dates))
        
        data = pd.DataFrame({
            'date': dates,
            'temperature': base_temp + seasonal_pattern + random_variation,
            'humidity': np.random.uniform(30, 90, len(dates)),
            'pressure': np.random.normal(1013, 20, len(dates)),
            'wind_speed': np.random.exponential(10, len(dates)),
            'location': location,
            'source_type': 'weather_synthetic',
            'fetch_time': datetime.now()
        })
        
        # Add randomness metrics
        data['temp_volatility'] = data['temperature'].rolling(window=7).std()
        data['weather_randomness'] = (
            np.abs(data['temperature'].diff()) + 
            np.abs(data['humidity'].diff()) / 10
        )
        
        printIt(f"✅ Generated {len(data)} weather records for {location}", lable.PASS)
        return data
    
    def _generate_synthetic_data(self, source_type: str, distribution: str, **kwargs) -> pd.DataFrame:
        """Generate synthetic random data for testing"""
        n_samples = kwargs.get('samples', 1000)
        
        # Convert samples to int if it's a string
        if isinstance(n_samples, str):
            try:
                n_samples = int(n_samples)
            except ValueError:
                n_samples = 1000
        
        printIt(f"🎲 Generating {n_samples} synthetic {distribution} samples", lable.DEBUG)
        
        dates = pd.date_range(start=datetime.now() - timedelta(days=n_samples), 
                             end=datetime.now(), freq='D')[:n_samples]
        
        if distribution == 'normal':
            values = np.random.normal(0, 1, n_samples)
        elif distribution == 'uniform':
            values = np.random.uniform(-1, 1, n_samples)
        elif distribution == 'exponential':
            values = np.random.exponential(1, n_samples)
        elif distribution == 'poisson':
            values = np.random.poisson(5, n_samples)
        else:
            values = np.random.normal(0, 1, n_samples)  # Default to normal
        
        data = pd.DataFrame({
            'date': dates,
            'value': values,
            'distribution': distribution,
            'source_type': source_type,
            'fetch_time': datetime.now()
        })
        
        # Add pure randomness metrics
        data['abs_change'] = np.abs(data['value'].diff())
        data['randomness_score'] = data['abs_change'] / data['value'].std()
        
        printIt(f"✅ Generated {n_samples} {distribution} samples", lable.PASS)
        return data
    
    def _fetch_economic_data(self, indicator: str, **kwargs) -> pd.DataFrame:
        """Fetch economic data (placeholder - would use FRED API, etc.)"""
        printIt(f"📊 Generating sample economic data for {indicator}", lable.DEBUG)
        
        # Generate synthetic economic data
        # In production, would use FRED API, World Bank API, etc.
        months = kwargs.get('months', 120)  # 10 years of monthly data
        
        dates = pd.date_range(start=datetime.now() - timedelta(days=months*30), 
                             end=datetime.now(), freq='M')[:months]
        
        # Generate realistic economic patterns
        if indicator.lower() in ['gdp', 'growth']:
            # GDP-like growth with cycles
            trend = 0.02  # 2% annual growth
            cycle = 0.01 * np.sin(2 * np.pi * np.arange(len(dates)) / 48)  # 4-year cycle
            shock = np.random.normal(0, 0.005, len(dates))  # Random shocks
            values = trend + cycle + shock
        elif indicator.lower() in ['unemployment', 'jobless']:
            # Unemployment rate
            base_rate = 0.05  # 5% base
            cycle = 0.02 * np.sin(2 * np.pi * np.arange(len(dates)) / 48)
            shock = np.random.normal(0, 0.01, len(dates))
            values = base_rate + cycle + np.abs(shock)
        else:
            # Generic economic indicator
            values = np.random.normal(0, 0.1, len(dates))
        
        data = pd.DataFrame({
            'date': dates,
            'value': values,
            'indicator': indicator,
            'source_type': 'economic_synthetic',
            'fetch_time': datetime.now()
        })
        
        # Add economic randomness metrics
        data['volatility'] = data['value'].rolling(window=12).std()
        data['trend'] = data['value'].rolling(window=24).mean()
        data['deviation_from_trend'] = data['value'] - data['trend']
        
    def _fetch_social_data(self, source_type: str, identifier: str, **kwargs) -> pd.DataFrame:
        """Fetch social media data (synthetic for now)"""
        printIt(f"📱 Generating sample social media data for {identifier}", lable.DEBUG)
        
        # For now, generate synthetic social media data
        # In production, would use Twitter API, Reddit API, etc.
        days = kwargs.get('days', 30)  # 30 days of social data
        
        dates = pd.date_range(start=datetime.now() - timedelta(days=days), 
                             end=datetime.now(), freq='h')[:days*24]  # Hourly data
        
        if "sentiment" in source_type:
            # Generate sentiment analysis data
            if identifier == "brand_sentiment":
                # Brand sentiment with realistic patterns
                base_sentiment = 0.1  # Slightly positive baseline
                trend = np.linspace(0, 0.2, len(dates))  # Improving trend
                daily_cycle = 0.1 * np.sin(2 * np.pi * np.arange(len(dates)) / 24)  # Daily cycle
                random_events = np.random.normal(0, 0.3, len(dates))  # Random sentiment events
                
                sentiment_score = base_sentiment + trend + daily_cycle + random_events
                sentiment_score = np.clip(sentiment_score, -1, 1)  # Keep in valid range
                
                # Generate related metrics
                volume = np.random.poisson(50, len(dates)) + np.abs(sentiment_score * 100)
                positive = np.maximum(0, sentiment_score) * volume
                negative = np.maximum(0, -sentiment_score) * volume
                neutral = volume - positive - negative
                
            elif identifier == "market_sentiment":
                # Market sentiment - more volatile
                base_sentiment = 0.0  # Neutral baseline
                volatility = np.random.normal(0, 0.4, len(dates))
                market_events = np.random.choice([-0.8, -0.3, 0, 0.3, 0.8], len(dates), 
                                               p=[0.05, 0.15, 0.6, 0.15, 0.05])  # Rare extreme events
                
                sentiment_score = base_sentiment + volatility + market_events * 0.1
                sentiment_score = np.clip(sentiment_score, -1, 1)
                
                volume = np.random.poisson(100, len(dates)) + np.abs(sentiment_score * 200)
                positive = np.maximum(0, sentiment_score) * volume
                negative = np.maximum(0, -sentiment_score) * volume
                neutral = volume - positive - negative
                
            else:
                # Generic sentiment
                sentiment_score = np.random.normal(0, 0.3, len(dates))
                sentiment_score = np.clip(sentiment_score, -1, 1)
                
                volume = np.random.poisson(30, len(dates))
                positive = np.maximum(0, sentiment_score) * volume
                negative = np.maximum(0, -sentiment_score) * volume
                neutral = volume - positive - negative
            
            data = pd.DataFrame({
                'datetime': dates,
                'sentiment_score': sentiment_score,
                'volume': volume.astype(int),
                'positive': positive.astype(int),
                'negative': negative.astype(int),
                'neutral': neutral.astype(int),
                'identifier': identifier,
                'source_type': source_type,
                'fetch_time': datetime.now()
            })
            
        elif "trends" in source_type:
            # Generate trending topics data
            trend_strength = np.random.exponential(1, len(dates))  # Exponential distribution for viral trends
            mentions = np.random.poisson(trend_strength * 10, len(dates))
            engagement = mentions * np.random.uniform(0.1, 0.3, len(dates))  # 10-30% engagement rate
            reach = mentions * np.random.uniform(5, 50, len(dates))  # Reach multiplier
            
            data = pd.DataFrame({
                'datetime': dates,
                'trend_strength': trend_strength,
                'mentions': mentions.astype(int),
                'engagement': engagement.astype(int),
                'reach': reach.astype(int),
                'identifier': identifier,
                'source_type': source_type,
                'fetch_time': datetime.now()
            })
        
        else:
            # Generic social data
            activity = np.random.poisson(25, len(dates))
            engagement = activity * np.random.uniform(0.05, 0.25, len(dates))
            
            data = pd.DataFrame({
                'datetime': dates,
                'activity': activity,
                'engagement': engagement.astype(int),
                'identifier': identifier,
                'source_type': source_type,
                'fetch_time': datetime.now()
            })
        
        # Add randomness metrics for social data
        numeric_cols = data.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            if col != 'fetch_time':
                col_data = data[col]
                data[f'{col}_volatility'] = col_data.rolling(window=24, min_periods=1).std()
                data[f'{col}_trend'] = col_data.rolling(window=48, min_periods=1).mean()
        
        printIt(f"✅ Generated {len(data)} social media records for {identifier}", lable.PASS)
        return data
    
    def _fetch_news_data(self, source_type: str, identifier: str, **kwargs) -> pd.DataFrame:
        """Fetch news data (synthetic for now)"""
        printIt(f"📰 Generating sample news data for {identifier}", lable.DEBUG)
        
        # Generate news event data
        days = kwargs.get('days', 7)  # 7 days of news
        
        # Generate random news events (not uniform - news comes in bursts)
        num_events = np.random.poisson(days * 5)  # Average 5 events per day
        event_times = pd.to_datetime(np.random.uniform(
            (datetime.now() - timedelta(days=days)).timestamp(),
            datetime.now().timestamp(),
            num_events
        ), unit='s')
        
        if "headlines" in source_type:
            # News headline sentiment and impact
            sentiment = np.random.normal(0, 0.4, num_events)  # News sentiment
            impact = np.random.exponential(1, num_events)  # Impact follows power law
            surprise_factor = np.random.beta(2, 5, num_events)  # Most news is not surprising
            
            data = pd.DataFrame({
                'datetime': event_times,
                'sentiment': sentiment,
                'impact': impact,
                'surprise_factor': surprise_factor,
                'identifier': identifier,
                'source_type': source_type,
                'fetch_time': datetime.now()
            })
            
        elif "events" in source_type:
            # Scheduled vs unscheduled events
            is_scheduled = np.random.choice([True, False], num_events, p=[0.3, 0.7])
            market_reaction = np.random.normal(0, 0.2, num_events)
            importance = np.random.uniform(0, 1, num_events)
            
            data = pd.DataFrame({
                'datetime': event_times,
                'is_scheduled': is_scheduled,
                'market_reaction': market_reaction,
                'importance': importance,
                'identifier': identifier,
                'source_type': source_type,
                'fetch_time': datetime.now()
            })
        
        else:
            # Generic news data
            relevance = np.random.uniform(0, 1, num_events)
            virality = np.random.exponential(0.5, num_events)
            
            data = pd.DataFrame({
                'datetime': event_times,
                'relevance': relevance,
                'virality': virality,
                'identifier': identifier,
                'source_type': source_type,
                'fetch_time': datetime.now()
            })
        
        data = data.sort_values('datetime').reset_index(drop=True)
        
        printIt(f"✅ Generated {len(data)} news records for {identifier}", lable.PASS)
        return data
    
    def _fetch_internet_data(self, source_type: str, identifier: str, **kwargs) -> pd.DataFrame:
        """Fetch internet usage data (synthetic for now)"""
        printIt(f"🌐 Generating sample internet data for {identifier}", lable.DEBUG)
        
        # Generate internet usage patterns
        days = kwargs.get('days', 30)
        hours = pd.date_range(start=datetime.now() - timedelta(days=days), 
                             end=datetime.now(), freq='h')
        
        if "traffic" in source_type:
            # Website traffic patterns with daily and weekly cycles
            hour_of_day = hours.hour
            day_of_week = hours.dayofweek
            
            # Daily pattern (higher during business hours)
            daily_pattern = 1 + 0.5 * np.sin(2 * np.pi * (hour_of_day - 6) / 24)
            
            # Weekly pattern (lower on weekends)
            weekly_pattern = np.where(day_of_week < 5, 1.2, 0.8)
            
            # Base traffic with patterns and randomness
            base_traffic = 1000
            traffic = base_traffic * daily_pattern * weekly_pattern * np.random.lognormal(0, 0.3, len(hours))
            
            # Related metrics
            unique_visitors = traffic * np.random.uniform(0.6, 0.8, len(hours))
            page_views = traffic * np.random.uniform(1.5, 3.0, len(hours))
            bounce_rate = np.random.uniform(0.3, 0.7, len(hours))
            
            data = pd.DataFrame({
                'datetime': hours,
                'traffic': traffic.astype(int),
                'unique_visitors': unique_visitors.astype(int),
                'page_views': page_views.astype(int),
                'bounce_rate': bounce_rate,
                'identifier': identifier,
                'source_type': source_type,
                'fetch_time': datetime.now()
            })
            
        elif "domains" in source_type:
            # Domain registration/expiration data (daily aggregates)
            days_range = pd.date_range(start=datetime.now() - timedelta(days=days), 
                                      end=datetime.now(), freq='D')
            
            # Domain activity follows business cycles
            registrations = np.random.poisson(50, len(days_range))  # New domains per day
            expirations = np.random.poisson(30, len(days_range))   # Expired domains per day
            dns_queries = np.random.lognormal(10, 1, len(days_range))  # DNS query volume
            
            data = pd.DataFrame({
                'date': days_range,
                'registrations': registrations,
                'expirations': expirations,
                'dns_queries': dns_queries.astype(int),
                'net_domains': registrations - expirations,
                'identifier': identifier,
                'source_type': source_type,
                'fetch_time': datetime.now()
            })
        
        else:
            # Generic internet metrics
            activity = np.random.lognormal(5, 1, len(hours))
            bandwidth = activity * np.random.uniform(0.5, 2.0, len(hours))
            
            data = pd.DataFrame({
                'datetime': hours,
                'activity': activity.astype(int),
                'bandwidth': bandwidth,
                'identifier': identifier,
                'source_type': source_type,
                'fetch_time': datetime.now()
            })
        
        printIt(f"✅ Generated {len(data)} internet records for {identifier}", lable.PASS)
        return data
    
    def save_data(self, data: pd.DataFrame, filename: str, processed: bool = False) -> str:
        """Save data to appropriate directory"""
        if processed:
            filepath = os.path.join(self.processed_dir, f"{filename}.csv")
        else:
            filepath = os.path.join(self.sources_dir, f"{filename}.csv")
        
        data.to_csv(filepath, index=False)
        printIt(f"💾 Data saved to {filepath}", lable.PASS)
        return filepath
    
    def load_data(self, filename: str, processed: bool = False) -> Optional[pd.DataFrame]:
        """Load previously saved data"""
        if processed:
            filepath = os.path.join(self.processed_dir, f"{filename}.csv")
        else:
            filepath = os.path.join(self.sources_dir, f"{filename}.csv")
        
        if os.path.exists(filepath):
            data = pd.read_csv(filepath)
            printIt(f"📂 Loaded data from {filepath}", lable.INFO)
            return data
        else:
            printIt(f"File not found: {filepath}", lable.WARN)
            return None
    
    def list_saved_data(self) -> Dict[str, List[str]]:
        """List all saved datasets"""
        sources = []
        processed = []
        
        if os.path.exists(self.sources_dir):
            sources = [f.replace('.csv', '') for f in os.listdir(self.sources_dir) if f.endswith('.csv')]
        
        if os.path.exists(self.processed_dir):
            processed = [f.replace('.csv', '') for f in os.listdir(self.processed_dir) if f.endswith('.csv')]
        
        return {'sources': sources, 'processed': processed}
    
    def analyze_randomness(self, data: pd.DataFrame, value_column: str = 'value') -> Dict[str, float]:
        """Analyze the randomness characteristics of a dataset"""
        if value_column not in data.columns:
            # Try to find a suitable column
            numeric_cols = data.select_dtypes(include=[np.number]).columns
            if len(numeric_cols) > 0:
                value_column = numeric_cols[0]
            else:
                printIt(f"No numeric columns found for randomness analysis", lable.WARN)
                return {}
        
        values = data[value_column].dropna()
        
        if len(values) < 2:
            printIt("Insufficient data for randomness analysis", lable.WARN)
            return {}
        
        # Calculate various randomness metrics
        analysis = {
            'mean': float(values.mean()),
            'std': float(values.std()),
            'skewness': float(values.skew()),
            'kurtosis': float(values.kurtosis()),
            'min': float(values.min()),
            'max': float(values.max()),
            'range': float(values.max() - values.min()),
            'coefficient_of_variation': float(values.std() / abs(values.mean())) if values.mean() != 0 else float('inf'),
            'autocorrelation_lag1': float(values.autocorr(lag=1)) if len(values) > 1 else 0.0,
            'randomness_score': float(np.abs(values.diff()).mean() / values.std()) if values.std() != 0 else 0.0
        }
        
        return analysis

# Global instance
data_fetcher = DataFetcher()
