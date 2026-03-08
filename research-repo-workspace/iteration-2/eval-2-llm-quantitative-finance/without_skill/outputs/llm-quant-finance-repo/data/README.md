# Data Directory - LLM Quantitative Finance

This directory contains datasets, data sources, and preprocessing pipelines for financial data used in LLM applications.

## Data Categories

### 1. Market Data (`/market`)
Historical and real-time market data for quantitative analysis.

#### Price and Volume Data
- **OHLCV Data**: Open, High, Low, Close, Volume for various instruments
  - Sources: Yahoo Finance, Alpha Vantage, Polygon.io, Bloomberg
  - Coverage: Stocks, ETFs, indices, futures, forex, crypto
  - Frequency: Tick, minute, hourly, daily, weekly, monthly
  - File format: Parquet, CSV, HDF5

- **Corporate Actions**: Splits, dividends, mergers, IPOs
  - Sources: Bloomberg, Refinitiv, ISS
  - Fields: Action type, date, ratio, description

#### Market Microstructure
- **Order Book Data**: Level 1 (quotes) and Level 2 (depth)
  - Sources: NASDAQ ITCH, NYSE TAQ, Lobster
  - Fields: Bid/ask prices, sizes, timestamp

- **Trades Data**: Individual transaction records
  - Fields: Price, size, direction, timestamp, venue

#### Reference Data
- **Security Master**: Instrument identifiers and metadata
  - Tickers, CUSIP, ISIN, SEDOL
  - Exchange, sector, industry classifications
  - Contract specifications for derivatives

### 2. Sentiment Data (`/sentiment`)
Textual and alternative data for sentiment analysis.

#### News Data
- **Financial News**: Headlines and articles
  - Sources: Bloomberg, Reuters, WSJ, CNBC
  - Fields: Timestamp, title, body, topics, sentiment scores
  - Format: JSON, CSV, Parquet

- **Press Releases**: Company announcements
  - Sources: PR Newswire, Business Wire
  - Fields: Timestamp, company, title, body, ticker mentions

#### Social Media Data
- **Twitter/X**: Financial tweets and sentiment
  - Sources: Twitter API, StockTwits
  - Fields: Timestamp, user, text, likes, retweets, ticker cashtags
  - Sentiment: Bullish/bearish labels, VADER, FinBERT scores

- **Reddit**: Financial forum discussions
  - Subreddits: r/wallstreetbets, r/investing, r/stocks
  - Fields: Timestamp, user, text, upvotes, comments

#### Analyst Communications
- **Earnings Call Transcripts**: Q&A sessions
  - Sources: Seeking Alpha, Bloomberg, FactSet
  - Fields: Date, company, participants, transcript, sentiment

- **Analyst Reports**: Research publications
  - Sources: Bloomberg, FactSet, TipRanks
  - Fields: Date, analyst, firm, ticker, rating, price target, summary

#### Central Bank Communications
- **FOMC Statements**: Federal Reserve policy decisions
  - Sources: Federal Reserve website
  - Fields: Date, statement text, voting outcomes, rate decisions

- **Fed Minutes**: Detailed meeting transcripts
  - Fields: Date, participants, discussion topics, policy outlook

### 3. Fundamental Data (`/fundamental`)
Company financials and accounting data.

#### Financial Statements
- **Income Statement**: Revenue, expenses, net income
  - Sources: SEC EDGAR, Compustat, Bloomberg
  - Frequency: Quarterly (10-Q), Annual (10-K)
  - Fields: Revenue, COGS, operating income, net income, EPS

- **Balance Sheet**: Assets, liabilities, equity
  - Fields: Total assets, current assets, total debt, shareholders' equity

- **Cash Flow Statement**: Operating, investing, financing activities
  - Fields: Operating CF, capital expenditures, free cash flow, dividends

#### Financial Ratios
- **Profitability**: ROE, ROA, profit margins, earnings growth
- **Valuation**: P/E, P/B, EV/EBITDA, PEG ratios
- **Leverage**: Debt-to-equity, interest coverage, current ratio
- **Efficiency**: Asset turnover, inventory turnover, receivable days

#### Estimates and Guidance
- **Analyst Estimates**: Forward-looking projections
  - Sources: IBES, Bloomberg, FactSet
  - Fields: EPS estimates, revenue estimates, price targets

- **Company Guidance**: Management forecasts
  - Sources: Earnings calls, press releases
  - Fields: Expected revenue, EPS, CAPEX guidance

### 4. Alternative Data (`/alternative`)
Non-traditional data sources for competitive insights.

#### Web Data
- **Web Traffic**: Website and app usage metrics
  - Sources: SimilarWeb, Apptopia, Sensor Tower
  - Metrics: Visits, unique visitors, time on site, bounce rate

- **Search Trends**: Google Trends data
  - Metrics: Search volume for tickers, companies, products

#### Satellite and Geospatial
- **Economic Activity**: Satellite imagery analysis
  - Sources: Orbital Insight, RS Metrics
  - Metrics: Crop yields, oil storage, retail parking lot occupancy

- **Construction and Development**: Building permits, construction activity
  - Sources: Municipal records, satellite data

#### Transactional Data
- **Credit Card**: Consumer spending patterns
  - Sources: Adyen, Stripe, First Data
  - Metrics: Transaction volume, merchant category codes

- **Supply Chain**: Trade and shipping data
  - Sources: Panjiva, Import Genius
  - Metrics: Import/export volumes, shipping container counts

### 5. Processed Data (`/processed`)
Cleaned, feature-engineered, and modeled datasets ready for analysis.

#### Feature Engineering
- **Technical Indicators**: Moving averages, RSI, MACD, Bollinger Bands
- **Momentum Features**: Returns over various periods, acceleration
- **Volatility Features**: Historical volatility, GARCH models
- **Volume Features**: Volume moving averages, on-balance volume

#### NLP Features
- **Sentiment Scores**: Time-series sentiment from various sources
- **Topic Models**: LDA, BERTopic for document themes
- **Embeddings**: Document and word embeddings (BERT, RoBERTa, FinBERT)
- **Named Entities**: Extracted companies, people, locations, events

#### Labels and Targets
- **Return Labels**: Future returns for classification/regression
- **Risk Labels**: Drawdown, volatility, VaR-based labels
- **Event Labels**: Earnings surprises, merger announcements, rating changes

## Data Acquisition

### APIs and Data Providers

#### Free Sources
- **Yahoo Finance** (`yfinance`): End-of-day prices, fundamentals
- **Alpha Vantage**: Technical indicators, fundamentals, forex
- **FRED**: Economic indicators and macro data
- **SEC EDGAR**: Company filings (10-K, 10-Q, 8-K)
- **Federal Reserve**: Monetary policy data

#### Paid Sources
- **Bloomberg Terminal**: Comprehensive financial data
- **Refinitiv (formerly Thomson Reuters)**: News, fundamentals, estimates
- **FactSet**: Estimates, ownership, fundamentals
- **Polygon.io**: Real-time and historical market data
- **Quandl**: Alternative data and curated datasets

### Web Scraping
- **News Sites**: Bloomberg, Reuters, WSJ (respect robots.txt)
- **Social Media**: Twitter API, Reddit API (with authentication)
- **SEC Filings**: Automated downloading from EDGAR

## Data Preprocessing

### Cleaning Steps
1. **Missing Value Handling**: Forward-fill, interpolation, imputation
2. **Outlier Detection**: Winsorization, z-score filtering
3. **Time Alignment**: Timezone normalization, resampling
4. **Corporate Actions**: Adjusting for splits, dividends, mergers
5. **Survivorship Bias**: Including delisted stocks

### Feature Engineering
1. **Price Features**: Returns, log returns, volatility
2. **Volume Features**: Volume changes, turnover, volume-weighted metrics
3. **Technical Indicators**: RSI, MACD, Bollinger Bands, ATR
4. **Calendar Features**: Day of week, month, quarter effects
5. **Cross-Sectional Features**: Sector, market cap, value/growth factors

### NLP Preprocessing
1. **Tokenization**: WordPiece, BPE for transformer models
2. **Cleaning**: Remove HTML, special characters, URLs
3. **Normalization**: Lowercase, lemmatization
4. **Financial Entity Recognition**: Ticker symbols, company names, financial terms
5. **Sentiment Extraction**: FinBERT, VADER, custom models

## Data Storage

### File Formats
- **Raw Data**: CSV, JSON (human-readable)
- **Processed Data**: Parquet, Feather (efficient columnar storage)
- **Time Series**: HDF5, Zarr (compressed, chunked)
- **Large Files**: Pickle (Python objects), msgpack

### Database Options
- **Time Series DB**: InfluxDB, TimescaleDB (PostgreSQL extension)
- **Document Store**: MongoDB (news, social media)
- **Search Engine**: Elasticsearch (text search and analytics)
- **Data Warehouse**: Snowflake, BigQuery (analytics)

### Version Control
- Use DVC (Data Version Control) for large datasets
- Track data lineage and preprocessing steps
- Store metadata and data dictionaries
- Implement data validation checks

## Data Quality

### Validation Checks
- **Range Checks**: Prices, volumes within expected ranges
- **Cross-Validation**: Compare multiple sources
- **Temporal Consistency**: No future data leakage
- **Completeness**: Minimum data requirements
- **Freshness**: Regular updates, staleness monitoring

### Documentation
- **Data Dictionary**: Field descriptions, units, sources
- **Lineage**: Transformation history
- **Quality Metrics**: Completeness, accuracy, timeliness scores
- **Known Issues**: Document gaps and limitations

## Data Ethics and Compliance

### Legal Considerations
- **Terms of Service**: Respect data provider terms
- **Copyright**: Fair use for research, proper attribution
- **Privacy**: Anonymize personal data from social media
- **Insider Trading**: Use only public information

### Best Practices
- **Data Minimization**: Collect only necessary data
- **Consent**: User consent for social media data
- **Attribution**: Credit data sources in publications
- **Reproducibility**: Document data sources and preprocessing

## Usage Examples

### Loading Price Data
```python
import pandas as pd
import yfinance as yf

# Download stock data
ticker = "AAPL"
data = yf.download(ticker, start="2020-01-01", end="2024-12-31")
data.to_parquet(f"processed/market/{ticker}_daily.parquet")
```

### Processing Sentiment Data
```python
from transformers import pipeline

# Load FinBERT for sentiment analysis
sentiment_pipeline = pipeline("sentiment-analysis",
                              model="ProsusAI/finbert")

# Analyze news headlines
headlines = ["Apple beats earnings expectations",
             "Fed signals rate hike possibility"]
results = sentiment_pipeline(headlines)
```

## Data Updates

### Refresh Schedule
- **Market Data**: Daily (EOD) or real-time
- **Fundamental Data**: Quarterly (earnings season)
- **Sentiment Data**: Continuous (news feeds, social media)
- **Alternative Data**: Varies by source (daily to monthly)

### Automation
- Use cron jobs or Airflow for scheduled updates
- Implement data pipeline monitoring
- Set up alerts for data quality issues
- Maintain backup and recovery procedures
