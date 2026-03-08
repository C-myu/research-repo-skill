# Quick Start Guide

Get started with LLM applications in quantitative finance.

## Installation

### 1. Clone the Repository
```bash
cd /home/mas-chen.mingyu/project/from_github/research-repo-skill/research-repo-workspace/iteration-2/eval-2-llm-quantitative-finance/without_skill/outputs/llm-quant-finance-repo
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Additional Dependencies (Optional)
```bash
# For financial data
pip install yfinance pandas-datareader

# For NLP
pip install transformers datasets accelerate

# For deep learning (PyTorch with CUDA support)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

## Quick Examples

### Example 1: Financial Sentiment Analysis

```python
from code.models.financial_bert import FinancialBERT

# Load pre-trained model
model = FinancialBERT(model_name="ProsusAI/finbert")

# Analyze sentiment
headlines = [
    "Apple beats earnings expectations by 15%",
    "Market declines on recession fears",
    "Fed maintains interest rates steady"
]

predictions = model.predict(headlines)

for headline, pred in zip(headlines, predictions):
    print(f"Text: {headline}")
    print(f"Sentiment: {pred['label']}")
    print(f"Confidence: {pred['score']:.3f}\n")
```

### Example 2: Download Market Data

```python
import yfinance as yf

# Download stock data
ticker = "AAPL"
data = yf.download(ticker, start="2023-01-01", end="2024-12-31")

# Calculate returns
data["Return"] = data["Close"].pct_change()

# Save to file
data.to_csv("data/market/AAPL_daily.csv")
```

### Example 3: Calculate Financial Metrics

```python
from code.metrics.financial_metrics import calculate_portfolio_metrics
import pandas as pd

# Load returns data
returns = pd.read_csv("data/processed/AAPL_returns.csv", index_col=0, parse_dates=True)

# Calculate metrics
metrics = calculate_portfolio_metrics(returns["Return"])

print("Portfolio Performance:")
print(f"Total Return: {metrics['total_return']:.2%}")
print(f"Sharpe Ratio: {metrics['sharpe_ratio']:.3f}")
print(f"Max Drawdown: {metrics['max_drawdown']:.2%}")
```

### Example 4: Sentiment Analysis Pipeline

```python
from code.utils.sentiment_utils import FinancialSentimentAnalyzer
import pandas as pd

# Initialize analyzer
analyzer = FinancialSentimentAnalyzer()

# Load news data
news_df = pd.read_csv("data/sentiment/news_headlines.csv")

# Analyze sentiment
results_df = analyzer.analyze_dataframe(news_df, text_column="headline")

# Aggregate by date
from code.utils.sentiment_utils import SentimentAggregator
aggregator = SentimentAggregator()
daily_sentiment = aggregator.aggregate_by_time(
    results_df,
    time_column="date",
    freq="D",
    aggregation="mean"
)

print(daily_sentiment.head())
```

## Data Setup

### Download Sample Data

```bash
# Market data (using yfinance)
python -c "
import yfinance as yf
import pandas as pd

# Download S&P 500 data
sp500 = yf.download('^GSPC', start='2020-01-01', end='2024-12-31')
sp500.to_csv('data/market/sp500.csv')

# Download individual stocks
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
for ticker in tickers:
    data = yf.download(ticker, start='2020-01-01', end='2024-12-31')
    data.to_csv(f'data/market/{ticker}.csv')
"
```

### Prepare Sentiment Data

```bash
# This would typically come from APIs or news sources
# For now, create sample structure
python -c "
import pandas as pd

# Sample news data
news_data = {
    'date': pd.date_range('2024-01-01', periods=100),
    'headline': [
        'Market rallies on positive economic data' if i % 2 == 0
        else 'Stocks decline amid rate hike concerns'
        for i in range(100)
    ],
    'source': ['Bloomberg'] * 100
}

df = pd.DataFrame(news_data)
df.to_csv('data/sentiment/sample_news.csv', index=False)
"
```

## Running Experiments

### Train a Sentiment Model

```bash
python code/experiments/sentiment_analysis/train.py \
    --config code/configs/training_config.yaml \
    --data data/processed/sentiment_train.parquet
```

### Evaluate Model Performance

```bash
python code/experiments/sentiment_analysis/evaluate.py \
    --checkpoint checkpoints/best_model.pt \
    --test_data data/processed/sentiment_test.parquet
```

### Hyperparameter Tuning

```bash
python code/experiments/sentiment_analysis/tune.py \
    --n_trials 100 \
    --experiment sentiment_analysis
```

## Common Workflows

### 1. Research New Paper
```bash
# Add paper to repository
cd papers
# Create new markdown file with paper details
# Update README.md with new entry

# Implement key method
cd ../code/models
# Create new model implementation

# Run experiments
cd ../experiments
# Create experiment directory and run experiments
```

### 2. Analyze New Dataset
```bash
# Add data to appropriate directory
# data/market/, data/sentiment/, etc.

# Create preprocessing script
# code/utils/preprocess_new_data.py

# Update data catalog
# Update data/README.md with new data source
```

### 3. Track Experiments
```bash
# Start MLflow UI
mlflow ui

# Run experiment with tracking
python code/experiments/example_experiment.py \
    --tracking mlflow \
    --experiment_name my_experiment

# View results at http://localhost:5000
```

## Project Structure Reference

```
llm-quant-finance-repo/
├── README.md                    # Main project documentation
├── QUICKSTART.md               # This file
├── requirements.txt            # Python dependencies
├── LICENSE                     # MIT License
│
├── papers/                     # Research papers and literature
│   └── README.md               # Paper catalog and organization
│
├── data/                       # Data directory
│   ├── market/                 # Price and volume data
│   ├── sentiment/              # Sentiment data sources
│   ├── fundamental/            # Financial statements
│   ├── alternative/            # Alternative data
│   ├── processed/              # Processed and feature data
│   └── README.md               # Data documentation
│
├── code/                       # Implementation code
│   ├── experiments/            # Experiment scripts
│   ├── models/                 # Model implementations
│   ├── analysis/               # Analysis scripts
│   ├── metrics/                # Evaluation metrics
│   ├── utils/                  # Utility functions
│   ├── configs/                # Configuration files
│   ├── tracking/               # Experiment tracking
│   └── README.md               # Code documentation
│
├── notes/                      # Research notes
│   ├── research_ideas.md       # Research questions and hypotheses
│   └── README.md               # Notes organization
│
└── .claude/                    # Claude-specific configs
    └── config.json             # Project configuration
```

## Next Steps

1. **Explore the Repository**: Read through the main README.md
2. **Set Up Data**: Download financial data from your preferred sources
3. **Run Baseline Models**: Implement and train simple baselines
4. **Review Literature**: Check papers/README.md for key papers
5. **Develop Research Questions**: Review notes/research_ideas.md
6. **Start Experiments**: Begin with sentiment analysis or price prediction

## Getting Help

### Resources
- **Main Documentation**: See README.md
- **Data Guide**: data/README.md
- **Code Guide**: code/README.md
- **Research Notes**: notes/README.md

### Common Issues

**Issue**: CUDA out of memory
```python
# Reduce batch size in config
# Or use gradient checkpointing
# Or switch to CPU
```

**Issue**: Data loading errors
```python
# Check data paths in config
# Verify data files exist
# Check file formats
```

**Issue**: Model not converging
```python
# Try different learning rate
# Check data normalization
# Increase training epochs
# Verify labels are correct
```

## Configuration

Edit `code/configs/training_config.yaml` to customize:
- Model architecture
- Training hyperparameters
- Data paths
- Logging settings
- Hardware configuration

## Best Practices

1. **Version Control**: Use git for code, DVC for data
2. **Experiment Tracking**: Log all experiments with MLflow
3. **Documentation**: Document code, experiments, and results
4. **Reproducibility**: Set random seeds, save configurations
5. **Testing**: Write tests for critical code

## Disclaimer

This repository is for research and educational purposes only. Nothing herein constitutes financial advice or investment recommendations. Always conduct your own research and consult with qualified financial advisors before making investment decisions.

## Contributing

We welcome contributions! Please:
1. Follow the existing code style
2. Add tests for new features
3. Update documentation
4. Use descriptive commit messages

---

**Ready to start?** Begin with the sentiment analysis example above!
