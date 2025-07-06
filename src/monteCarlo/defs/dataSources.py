"""
Data Sources Registry - Discovering the Randomness of Web Information

This module defines available data sources for Monte Carlo analysis.
The philosophy: We don't know what patterns exist until we look.
Everything on the web has inherent randomness, but patterns emerge.
"""

import random
from typing import Dict, List, Any
from .logIt import printIt, lable

class DataSourceRegistry:
    """Registry of available data sources for Monte Carlo analysis"""
    
    def __init__(self):
        self.sources = {
            # Financial Markets - Classic randomness with emergent patterns
            "financial": {
                "description": "Financial markets - where randomness meets human psychology",
                "sources": {
                    "stocks": {
                        "description": "Stock prices (daily, hourly, minute data)",
                        "examples": ["AAPL", "GOOGL", "MSFT", "TSLA", "SPY"],
                        "columns": ["open", "high", "low", "close", "volume", "adj_close"],
                        "randomness": "High - affected by news, sentiment, algorithms",
                        "patterns": "Trends, seasonality, volatility clustering"
                    },
                    "crypto": {
                        "description": "Cryptocurrency prices - pure digital randomness",
                        "examples": ["BTC-USD", "ETH-USD", "ADA-USD", "DOT-USD"],
                        "columns": ["open", "high", "low", "close", "volume"],
                        "randomness": "Extreme - 24/7 global sentiment",
                        "patterns": "Pump/dump cycles, correlation with tech stocks"
                    },
                    "forex": {
                        "description": "Foreign exchange rates - economic randomness",
                        "examples": ["EURUSD=X", "GBPUSD=X", "USDJPY=X"],
                        "columns": ["open", "high", "low", "close"],
                        "randomness": "Medium - central bank policies",
                        "patterns": "Economic cycles, interest rate differentials"
                    },
                    "commodities": {
                        "description": "Commodity prices - supply/demand randomness",
                        "examples": ["GC=F", "CL=F", "SI=F", "NG=F"],
                        "columns": ["open", "high", "low", "close", "volume"],
                        "randomness": "High - weather, geopolitics, speculation",
                        "patterns": "Seasonal cycles, supply shocks"
                    }
                }
            },
            
            # Weather - Nature's randomness
            "weather": {
                "description": "Weather data - chaos theory in action",
                "sources": {
                    "current": {
                        "description": "Current weather conditions worldwide",
                        "examples": ["New York", "London", "Tokyo", "Sydney"],
                        "columns": ["temperature", "humidity", "pressure", "wind_speed", "visibility"],
                        "randomness": "High - butterfly effect, chaos systems",
                        "patterns": "Seasonal, geographic, climate zones"
                    },
                    "historical": {
                        "description": "Historical weather patterns",
                        "examples": ["temperature_trends", "precipitation", "extreme_events"],
                        "columns": ["temp_max", "temp_min", "precipitation", "wind", "humidity"],
                        "randomness": "Medium - climate patterns exist",
                        "patterns": "Seasonal cycles, climate change trends"
                    }
                }
            },
            
            # Social Media - Human behavior randomness
            "social": {
                "description": "Social media metrics - collective human randomness",
                "sources": {
                    "trends": {
                        "description": "Trending topics and hashtags",
                        "examples": ["#technology", "#finance", "#weather", "#news"],
                        "columns": ["mentions", "sentiment", "reach", "engagement"],
                        "randomness": "Extreme - viral unpredictability",
                        "patterns": "Viral cascades, sentiment waves"
                    },
                    "sentiment": {
                        "description": "Public sentiment analysis",
                        "examples": ["market_sentiment", "political_sentiment", "brand_sentiment"],
                        "columns": ["positive", "negative", "neutral", "volume"],
                        "randomness": "High - emotional responses",
                        "patterns": "Mood cycles, event-driven spikes"
                    }
                }
            },
            
            # Economic Indicators - Structured randomness
            "economic": {
                "description": "Economic indicators - policy meets randomness",
                "sources": {
                    "indicators": {
                        "description": "Key economic metrics",
                        "examples": ["GDP", "unemployment", "inflation", "interest_rates"],
                        "columns": ["value", "change", "forecast", "previous"],
                        "randomness": "Medium - policy-driven but unpredictable",
                        "patterns": "Business cycles, policy responses"
                    },
                    "employment": {
                        "description": "Employment statistics",
                        "examples": ["job_openings", "unemployment_rate", "wage_growth"],
                        "columns": ["rate", "change", "sector_breakdown"],
                        "randomness": "Medium - economic cycles",
                        "patterns": "Seasonal employment, industry trends"
                    }
                }
            },
            
            # News & Events - Information randomness
            "news": {
                "description": "News and events - information flow randomness",
                "sources": {
                    "headlines": {
                        "description": "News headline analysis",
                        "examples": ["financial_news", "tech_news", "world_news"],
                        "columns": ["sentiment", "keywords", "source", "timestamp"],
                        "randomness": "High - unpredictable events",
                        "patterns": "News cycles, topic clustering"
                    },
                    "events": {
                        "description": "Scheduled and unscheduled events",
                        "examples": ["earnings", "fed_meetings", "elections", "disasters"],
                        "columns": ["type", "impact", "surprise_factor", "market_reaction"],
                        "randomness": "Variable - some scheduled, some random",
                        "patterns": "Calendar effects, surprise impacts"
                    }
                }
            },
            
            # Internet Metrics - Digital randomness
            "internet": {
                "description": "Internet usage and digital behavior",
                "sources": {
                    "traffic": {
                        "description": "Website traffic patterns",
                        "examples": ["google_trends", "website_visits", "search_volume"],
                        "columns": ["volume", "geographic", "device_type", "time_spent"],
                        "randomness": "Medium - behavioral patterns exist",
                        "patterns": "Daily cycles, seasonal searches"
                    },
                    "domains": {
                        "description": "Domain registration and DNS data",
                        "examples": ["new_domains", "expired_domains", "dns_queries"],
                        "columns": ["registrations", "expirations", "query_volume"],
                        "randomness": "High - entrepreneurial activity",
                        "patterns": "Business cycles, tech trends"
                    }
                }
            },
            
            # Random Data Generators - Pure randomness for testing
            "synthetic": {
                "description": "Synthetic random data for testing theories",
                "sources": {
                    "pure_random": {
                        "description": "Mathematically random data",
                        "examples": ["normal", "uniform", "exponential", "poisson"],
                        "columns": ["value", "timestamp", "distribution_params"],
                        "randomness": "Perfect - mathematically defined",
                        "patterns": "Only statistical properties"
                    },
                    "correlated": {
                        "description": "Random data with defined correlations",
                        "examples": ["corr_0.5", "corr_0.8", "corr_negative"],
                        "columns": ["var1", "var2", "var3", "correlation_matrix"],
                        "randomness": "Controlled - defined relationships",
                        "patterns": "Designed correlations"
                    }
                }
            }
        }
    
    def list_categories(self):
        """List all available data categories"""
        printIt("🎲 Available Data Categories - Exploring Web Randomness", lable.INFO)
        printIt("=" * 60, lable.INFO)
        
        for category, info in self.sources.items():
            printIt(f"\n📊 {category.upper()}", lable.PASS)
            printIt(f"   {info['description']}", lable.INFO)
            printIt(f"   Sources: {len(info['sources'])} available", lable.DEBUG)
    
    def list_sources(self, category=None):
        """List sources in a category or all sources"""
        if category and category in self.sources:
            self._list_category_sources(category)
        else:
            printIt("🌐 All Available Data Sources", lable.INFO)
            printIt("=" * 60, lable.INFO)
            for cat in self.sources.keys():
                self._list_category_sources(cat)
                printIt("", lable.INFO)  # spacing
    
    def _list_category_sources(self, category):
        """List sources for a specific category"""
        cat_info = self.sources[category]
        printIt(f"\n📈 {category.upper()} - {cat_info['description']}", lable.PASS)
        
        for source_name, source_info in cat_info['sources'].items():
            printIt(f"\n  🔹 {source_name}", lable.INFO)
            printIt(f"     {source_info['description']}", lable.DEBUG)
            printIt(f"     Examples: {', '.join(source_info['examples'][:3])}", lable.DEBUG)
            printIt(f"     Columns: {', '.join(source_info['columns'][:4])}", lable.DEBUG)
            printIt(f"     Randomness: {source_info['randomness']}", lable.WARN)
            printIt(f"     Patterns: {source_info['patterns']}", lable.PASS)
    
    def get_random_suggestion(self):
        """Get a random data source suggestion - embrace the randomness!"""
        category = random.choice(list(self.sources.keys()))
        source_name = random.choice(list(self.sources[category]['sources'].keys()))
        source_info = self.sources[category]['sources'][source_name]
        
        printIt("🎯 Random Data Suggestion (Let randomness guide you!)", lable.INFO)
        printIt("=" * 50, lable.INFO)
        printIt(f"Category: {category}", lable.PASS)
        printIt(f"Source: {source_name}", lable.PASS)
        printIt(f"Description: {source_info['description']}", lable.DEBUG)
        
        # Random example
        example = random.choice(source_info['examples'])
        printIt(f"Try this: monteCarlo fetchData {category}_{source_name} {example}", lable.WARN)
        
        return category, source_name, example
    
    def get_source_info(self, category, source_name):
        """Get detailed information about a specific source"""
        if category in self.sources and source_name in self.sources[category]['sources']:
            return self.sources[category]['sources'][source_name]
        return None
    
    def search_sources(self, keyword):
        """Search for sources containing a keyword"""
        results = []
        keyword = keyword.lower()
        
        for category, cat_info in self.sources.items():
            for source_name, source_info in cat_info['sources'].items():
                # Search in description, examples, and columns
                searchable = (
                    source_info['description'].lower() + ' ' +
                    ' '.join(source_info['examples']).lower() + ' ' +
                    ' '.join(source_info['columns']).lower()
                )
                
                if keyword in searchable:
                    results.append((category, source_name, source_info))
        
        if results:
            printIt(f"🔍 Search results for '{keyword}':", lable.INFO)
            printIt("=" * 40, lable.INFO)
            for category, source_name, source_info in results:
                printIt(f"\n📊 {category}/{source_name}", lable.PASS)
                printIt(f"   {source_info['description']}", lable.DEBUG)
        else:
            printIt(f"No sources found for '{keyword}'", lable.WARN)
        
        return results

# Global instance
data_registry = DataSourceRegistry()
