"""
Real News Data Fetcher with Sentiment Analysis
Fetches actual news headlines and analyzes sentiment and impact
"""

import os
import requests
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import numpy as np
from dotenv import load_dotenv

from .logIt import printIt, lable

# Load environment variables
load_dotenv()

class NewsDataFetcher:
    def __init__(self):
        self.news_api_key = os.getenv('NEWS_API_KEY')
        self.alpha_vantage_key = os.getenv('ALPHA_VANTAGE_API_KEY')
        self.finnhub_key = os.getenv('FINNHUB_API_KEY')
        
        # Initialize sentiment analyzers
        self.vader_analyzer = SentimentIntensityAnalyzer()
        
        # News sources configuration
        self.financial_sources = [
            'bloomberg', 'reuters', 'financial-times', 'wall-street-journal',
            'cnbc', 'marketwatch', 'yahoo-finance', 'business-insider'
        ]
        
        self.general_sources = [
            'bbc-news', 'cnn', 'abc-news', 'associated-press', 
            'reuters', 'the-guardian-uk', 'usa-today'
        ]
        
    def fetch_news_headlines(self, identifier: str, days: int = 7, **kwargs) -> pd.DataFrame:
        """Fetch real news headlines with sentiment analysis"""
        
        if not self.news_api_key:
            printIt("⚠️  NEWS_API_KEY not found. Using synthetic data fallback.", lable.WARN)
            return self._generate_synthetic_news(identifier, days)
        
        try:
            if identifier == "financial_news":
                return self._fetch_financial_news(days, **kwargs)
            elif identifier == "general_news":
                return self._fetch_general_news(days, **kwargs)
            elif identifier == "tech_news":
                return self._fetch_tech_news(days, **kwargs)
            else:
                return self._fetch_custom_news(identifier, days, **kwargs)
                
        except Exception as e:
            printIt(f"Error fetching real news data: {str(e)}", lable.ERROR)
            printIt("Falling back to synthetic news data", lable.WARN)
            return self._generate_synthetic_news(identifier, days)
    
    def _fetch_financial_news(self, days: int, **kwargs) -> pd.DataFrame:
        """Fetch financial news from multiple sources"""
        printIt("📰 Fetching real financial news headlines...", lable.DEBUG)
        
        # Calculate date range
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        all_articles = []
        
        # NewsAPI endpoint
        url = "https://newsapi.org/v2/everything"
        
        # Financial keywords
        keywords = kwargs.get('keywords', 'stock market OR finance OR economy OR trading OR investment')
        
        params = {
            'apiKey': self.news_api_key,
            'q': keywords,
            'sources': ','.join(self.financial_sources[:5]),  # Limit to avoid API limits
            'from': start_date.strftime('%Y-%m-%d'),
            'to': end_date.strftime('%Y-%m-%d'),
            'language': 'en',
            'sortBy': 'publishedAt',
            'pageSize': 100
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
            
            for article in articles:
                if article['title'] and article['description']:
                    all_articles.append({
                        'headline': article['title'],
                        'description': article['description'],
                        'source': article['source']['name'],
                        'published_at': article['publishedAt'],
                        'url': article['url']
                    })
        
        if not all_articles:
            printIt("No articles found, generating synthetic data", lable.WARN)
            return self._generate_synthetic_news("financial_news", days)
        
        # Convert to DataFrame and analyze sentiment
        df = pd.DataFrame(all_articles)
        df = self._analyze_sentiment_and_impact(df)
        
        printIt(f"✅ Fetched {len(df)} real financial news articles", lable.PASS)
        return df
    
    def _fetch_general_news(self, days: int, **kwargs) -> pd.DataFrame:
        """Fetch general news headlines"""
        printIt("📰 Fetching real general news headlines...", lable.DEBUG)
        
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        url = "https://newsapi.org/v2/top-headlines"
        
        params = {
            'apiKey': self.news_api_key,
            'sources': ','.join(self.general_sources[:5]),
            'language': 'en',
            'pageSize': 100
        }
        
        all_articles = []
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
            
            for article in articles:
                if article['title'] and article['description']:
                    all_articles.append({
                        'headline': article['title'],
                        'description': article['description'],
                        'source': article['source']['name'],
                        'published_at': article['publishedAt'],
                        'url': article['url']
                    })
        
        if not all_articles:
            return self._generate_synthetic_news("general_news", days)
        
        df = pd.DataFrame(all_articles)
        df = self._analyze_sentiment_and_impact(df)
        
        printIt(f"✅ Fetched {len(df)} real general news articles", lable.PASS)
        return df
    
    def _fetch_tech_news(self, days: int, **kwargs) -> pd.DataFrame:
        """Fetch technology news"""
        printIt("📰 Fetching real technology news headlines...", lable.DEBUG)
        
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        url = "https://newsapi.org/v2/everything"
        
        params = {
            'apiKey': self.news_api_key,
            'q': 'technology OR AI OR artificial intelligence OR tech OR startup',
            'sources': 'techcrunch,the-verge,wired,ars-technica',
            'from': start_date.strftime('%Y-%m-%d'),
            'to': end_date.strftime('%Y-%m-%d'),
            'language': 'en',
            'sortBy': 'publishedAt',
            'pageSize': 100
        }
        
        all_articles = []
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])
            
            for article in articles:
                if article['title'] and article['description']:
                    all_articles.append({
                        'headline': article['title'],
                        'description': article['description'],
                        'source': article['source']['name'],
                        'published_at': article['publishedAt'],
                        'url': article['url']
                    })
        
        if not all_articles:
            return self._generate_synthetic_news("tech_news", days)
        
        df = pd.DataFrame(all_articles)
        df = self._analyze_sentiment_and_impact(df)
        
        printIt(f"✅ Fetched {len(df)} real technology news articles", lable.PASS)
        return df
    
    def _analyze_sentiment_and_impact(self, df: pd.DataFrame) -> pd.DataFrame:
        """Analyze sentiment and calculate impact scores for news articles"""
        printIt("🔍 Analyzing sentiment and impact...", lable.DEBUG)
        
        sentiments = []
        impacts = []
        surprise_factors = []
        
        for _, row in df.iterrows():
            # Combine headline and description for analysis
            text = f"{row['headline']} {row['description']}"
            
            # TextBlob sentiment analysis
            blob = TextBlob(text)
            textblob_sentiment = blob.sentiment.polarity
            
            # VADER sentiment analysis
            vader_scores = self.vader_analyzer.polarity_scores(text)
            vader_compound = vader_scores['compound']
            
            # Combined sentiment score (average of both methods)
            combined_sentiment = (textblob_sentiment + vader_compound) / 2
            
            # Calculate impact score based on various factors
            impact_score = self._calculate_impact_score(text, row)
            
            # Calculate surprise factor
            surprise_factor = self._calculate_surprise_factor(text)
            
            sentiments.append(combined_sentiment)
            impacts.append(impact_score)
            surprise_factors.append(surprise_factor)
        
        # Add analysis results to dataframe
        df['sentiment'] = sentiments
        df['impact'] = impacts
        df['surprise_factor'] = surprise_factors
        
        # Add additional metrics
        df['abs_sentiment'] = np.abs(df['sentiment'])
        df['sentiment_category'] = df['sentiment'].apply(self._categorize_sentiment)
        df['impact_category'] = pd.cut(df['impact'], bins=3, labels=['Low', 'Medium', 'High'])
        
        # Add datetime parsing
        df['datetime'] = pd.to_datetime(df['published_at'])
        df['hour'] = df['datetime'].dt.hour
        df['day_of_week'] = df['datetime'].dt.dayofweek
        
        return df
    
    def _calculate_impact_score(self, text: str, row: Dict) -> float:
        """Calculate impact score based on content analysis"""
        impact_keywords = {
            'high': ['crisis', 'crash', 'surge', 'plunge', 'breakthrough', 'record', 'historic'],
            'medium': ['rise', 'fall', 'increase', 'decrease', 'growth', 'decline'],
            'low': ['stable', 'steady', 'maintain', 'continue']
        }
        
        text_lower = text.lower()
        
        # Base impact score
        impact = 0.5
        
        # Keyword-based impact
        for keyword in impact_keywords['high']:
            if keyword in text_lower:
                impact += 0.3
        
        for keyword in impact_keywords['medium']:
            if keyword in text_lower:
                impact += 0.1
        
        # Source credibility factor
        credible_sources = ['reuters', 'bloomberg', 'financial times', 'wall street journal']
        if any(source in row['source'].lower() for source in credible_sources):
            impact += 0.2
        
        # Length factor (longer articles might be more impactful)
        if len(text) > 200:
            impact += 0.1
        
        return min(impact, 1.0)  # Cap at 1.0
    
    def _calculate_surprise_factor(self, text: str) -> float:
        """Calculate surprise factor based on unexpected events"""
        surprise_keywords = [
            'unexpected', 'surprise', 'shock', 'sudden', 'unprecedented', 
            'breaking', 'urgent', 'alert', 'emergency'
        ]
        
        text_lower = text.lower()
        surprise_score = 0.1  # Base surprise
        
        for keyword in surprise_keywords:
            if keyword in text_lower:
                surprise_score += 0.2
        
        return min(surprise_score, 1.0)
    
    def _categorize_sentiment(self, sentiment: float) -> str:
        """Categorize sentiment into positive, negative, neutral"""
        if sentiment > 0.1:
            return 'Positive'
        elif sentiment < -0.1:
            return 'Negative'
        else:
            return 'Neutral'
    
    def _generate_synthetic_news(self, identifier: str, days: int) -> pd.DataFrame:
        """Fallback synthetic news generation"""
        printIt(f"🎲 Generating synthetic news data for {identifier}", lable.DEBUG)
        
        # Generate random news events (not uniform - news comes in bursts)
        num_events = np.random.poisson(days * 5)  # Average 5 events per day
        event_times = pd.to_datetime(np.random.uniform(
            (datetime.now() - timedelta(days=days)).timestamp(),
            datetime.now().timestamp(),
            num_events
        ), unit='s')
        
        # Sample headlines based on identifier
        if "financial" in identifier:
            headlines = [
                "Stock Market Shows Volatility Amid Economic Uncertainty",
                "Federal Reserve Considers Interest Rate Changes",
                "Tech Stocks Rally on Earnings Reports",
                "Oil Prices Fluctuate on Global Supply Concerns",
                "Cryptocurrency Market Experiences Major Movements"
            ]
        elif "tech" in identifier:
            headlines = [
                "AI Breakthrough Announced by Major Tech Company",
                "New Smartphone Technology Revolutionizes Industry",
                "Cybersecurity Concerns Rise with Data Breach",
                "Cloud Computing Market Continues Rapid Growth",
                "Social Media Platform Updates Privacy Policies"
            ]
        else:
            headlines = [
                "Global Economic Summit Addresses Trade Relations",
                "Climate Change Initiative Gains International Support",
                "Healthcare Innovation Shows Promise in Clinical Trials",
                "Transportation Infrastructure Investment Announced",
                "Education Reform Proposal Sparks Debate"
            ]
        
        # Generate synthetic data
        synthetic_headlines = np.random.choice(headlines, num_events, replace=True)
        sentiment = np.random.normal(0, 0.4, num_events)
        impact = np.random.exponential(0.5, num_events)
        surprise_factor = np.random.beta(2, 5, num_events)
        
        data = pd.DataFrame({
            'datetime': event_times,
            'headline': synthetic_headlines,
            'sentiment': sentiment,
            'impact': impact,
            'surprise_factor': surprise_factor,
            'source': 'Synthetic',
            'identifier': identifier,
            'source_type': 'news_headlines',
            'fetch_time': datetime.now()
        })
        
        data = data.sort_values('datetime').reset_index(drop=True)
        return data
