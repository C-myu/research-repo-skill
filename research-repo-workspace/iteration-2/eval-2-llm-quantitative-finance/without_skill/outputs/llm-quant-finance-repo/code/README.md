# Code Directory - LLM Quantitative Finance

This directory contains implementations, experiments, and analysis pipelines for LLM applications in quantitative finance.

## Directory Structure

### 1. Experiments (`/experiments`)
Reproducible experimental pipelines for research projects.

#### Financial Prediction Experiments
- **`price_prediction/`**: Stock price forecasting models
  - Data preprocessing for time series
  - Model training and evaluation
  - Hyperparameter tuning
  - Result visualization

- **`earnings_prediction/`**: Earnings per share (EPS) forecasting
  - Feature engineering from financial statements
  - Sequential model architectures
  - Ensemble methods
  - Backtesting framework

- **`market_regime_detection/`**: Identifying market states
  - Clustering and classification
  - Hidden Markov Models
  - Transformer-based regime detection

#### Sentiment Analysis Experiments
- **`news_sentiment/`**: Financial news sentiment classification
  - Fine-tuning BERT/FinBERT
  - Multi-label classification
  - Domain adaptation

- **`social_sentiment/`**: Social media sentiment analysis
  - Twitter/Reddit data processing
  - Sarcasm and irony detection
  - Influencer weight modeling

- **`multimodal_sentiment/`**: Fusing multiple sentiment sources
  - Late fusion strategies
  - Attention-based fusion
  - Cross-source validation

#### Risk Management Experiments
- **`var_prediction/`**: Value at Risk forecasting
  - Conditional VaR models
  - Monte Carlo simulation with LLM features
  - Extreme value theory

- **`credit_scoring/`**: Credit risk assessment
  - Alternative data integration
  - Explainable AI for credit decisions
  - Fairness and bias mitigation

- **`portfolio_optimization/`**: LLM-enhanced portfolio construction
  - Natural language constraint extraction
  - Black-Litterman with LLM views
  - Dynamic rebalancing

### 2. Analysis (`/analysis`)
Exploratory data analysis and visualization scripts.

#### Market Analysis
- **`trend_analysis.py`**: Market trend detection and visualization
- **`correlation_analysis.py`**: Asset correlation matrices and networks
- **`volatility_analysis.py`**: Volatility clustering and regime changes
- **`sector_analysis.py`**: Sector and industry performance

#### Sentiment Analysis
- **`sentiment_distribution.py`**: Sentiment score distributions over time
- **`sentiment_vs_returns.py`**: Correlation between sentiment and returns
- **`topic_modeling.py`**: LDA/BERTopic for financial themes
- **`event_analysis.py`**: Sentiment around major events

#### Model Analysis
- **`feature_importance.py`**: SHAP values and feature attribution
- **`error_analysis.py`**: Model error patterns and diagnostics
- **`attention_visualization.py`**: Transformer attention weights
- **`embedding_analysis.py`**: Document embedding visualizations (UMAP/t-SNE)

#### Backtesting Analysis
- **`backtest_engine.py`**: Backtesting framework for trading strategies
- **`performance_metrics.py`**: Sharpe, Sortino, drawdown calculations
- **`transaction_costs.py`**: Cost-adjusted performance evaluation
- **`regime_analysis.py`**: Performance across market regimes

### 3. Models (`/models`)
Model architectures and training implementations.

#### Transformer Models
- **`financial_bert.py`**: Fine-tuned BERT for finance
  - Pre-training on financial corpus
  - Task-specific fine-tuning
  - Multi-task learning

- **`time_series_transformer.py`**: Transformer for financial time series
  - Temporal fusion architecture
  - Attention mechanisms for sequences
  - Positional encoding for time series

- **`multimodal_transformer.py`**: Cross-modal attention for text + prices
  - Text and price sequence encoding
  - Fusion layers
  - Joint training

#### Specialized Models
- **`sentiment_model.py`**: Sentiment classification heads
  - FinBERT fine-tuning
  - Custom sentiment architectures
  - Domain-adaptive pretraining

- **`risk_model.py`**: Risk assessment models
  - VaR prediction networks
  - Credit scoring models
  - Anomaly detection

- **`generative_model.py`**: Text generation for finance
  - GPT-based report generation
  - Summarization models
  - Question answering

#### Model Utilities
- **`training.py`**: Training loops and callbacks
- **`evaluation.py`**: Evaluation metrics and logging
- **`checkpointing.py`**: Model saving and loading
- **`hyperparameter_tuning.py`**: Optuna/Ray Tune integration

### 4. Metrics (`/metrics`)
Evaluation metrics and scoring functions.

#### Prediction Metrics
- **`regression_metrics.py`**:
  - MSE, RMSE, MAE, MAPE
  - R-squared, adjusted R-squared
  - Directional accuracy
  - Information Coefficient (IC)

- **`classification_metrics.py`**:
  - Accuracy, precision, recall, F1
  - ROC-AUC, PR-AUC
  - Confusion matrix
  - Precision@K, recall@K

#### Financial Metrics
- **`return_metrics.py`**:
  - Cumulative returns
  - Annualized returns
  - Alpha, beta
  - Tracking error

- **`risk_metrics.py`**:
  - Volatility (annualized)
  - Sharpe ratio, Sortino ratio
  - Maximum drawdown
  - VaR, CVaR
  - Calmar ratio

- **`portfolio_metrics.py`**:
  - Portfolio turnover
  - Concentration metrics
  - Factor exposures
  - Attribution analysis

#### NLP Metrics
- **`text_metrics.py`**:
  - BLEU, ROUGE for summarization
  - Perplexity for language models
  - Semantic similarity
  - Entity recognition F1

#### Backtesting Metrics
- **`backtest_metrics.py`**:
  - Win rate, profit factor
  - Average win/loss
  - Hit rate
  - Risk-reward ratio

### 5. Utils (`/utils`)
Utility functions and helper modules.

#### Data Utilities
- **`data_loader.py`**: Data loading and caching
- **`preprocessing.py`**: Cleaning and transformation pipelines
- **`feature_engineering.py`**: Feature creation and selection
- **`augmentation.py`**: Data augmentation techniques

#### NLP Utilities
- **`tokenization.py`**: Tokenizer wrappers and utilities
- **`text_cleaning.py`**: Text normalization and cleaning
- **`entity_extraction.py`**: Financial NER and relation extraction
- **`sentiment_utils.py`**: Sentiment scoring and aggregation

#### Model Utilities
- **`model_utils.py`**: Model building and configuration
- **`training_utils.py`**: Training helpers (LR scheduling, early stopping)
- **`inference.py`**: Model inference and batch prediction
- **`ensemble.py`**: Ensemble methods and model combination

#### Visualization Utilities
- **`plotting.py`**: Financial plotting functions
- **`interactive_plots.py`**: Plotly dashboards
- **`time_series_plots.py`**: Time series visualizations
- **`sentiment_plots.py`**: Sentiment visualization

#### System Utilities
- **`logging.py`**: Logging configuration
- **`config.py`**: Configuration management
- **`path_utils.py`**: Path handling and file I/O
- **`parallel.py`**: Parallel processing utilities

### 6. Configs (`/configs`)
Configuration files for experiments and models.

#### Experiment Configs
- **`training_config.yaml`**: Training hyperparameters
  - Learning rate, batch size, epochs
  - Optimizer settings
  - Regularization parameters

- **`model_config.yaml`**: Model architecture settings
  - Layer sizes, attention heads
  - Dropout rates
  - Activation functions

- **`data_config.yaml`**: Data source and preprocessing settings
  - Data paths and sources
  - Train/validation/test splits
  - Feature columns

#### Environment Configs
- **`paths.yaml`**: Directory paths for data, models, outputs
- **`api_keys.yaml`**: API keys and credentials (encrypted)
- **`logging.yaml`**: Logging levels and outputs

### 7. Tracking (`/tracking`)
Experiment tracking and reproducibility.

#### MLflow Tracking
- **`mlflow_setup.py`**: MLflow initialization
- **`experiments/`**: MLflow experiment definitions
- **`runs/`**: Saved run metadata and artifacts

#### Experiment Logs
- **`training_logs/`**: Training history and metrics
- **`error_logs/`**: Error tracking and debugging
- **`hyperparameter_search/`**: Tuning results and analysis

#### Reproducibility
- **`requirements.txt`**: Python package dependencies
- **`environment.yml`**: Conda environment specification
- **`Dockerfile`**: Docker container configuration
- **`seed.py`**: Random seed setting for reproducibility

## Key Technologies and Libraries

### Deep Learning
- **PyTorch**: Primary deep learning framework
- **Hugging Face Transformers**: Pre-trained LLMs
- **TensorFlow/Keras**: Alternative deep learning framework

### Data Processing
- **Pandas**: Data manipulation
- **NumPy**: Numerical computing
- **Dask**: Out-of-core computation
- **Polars**: Fast DataFrame library

### Financial Data
- **yfinance**: Yahoo Finance API
- **pandas-datareader**: Multi-source data reader
- **Alpha Vantage**: Financial data API
- **QuantLib**: Quantitative finance library

### NLP
- **NLTK/SpaCy**: Text processing
- **TextBlob**: Sentiment analysis
- **FinBERT**: Financial sentiment model
- **LangChain**: LLM application framework

### Visualization
- **Matplotlib**: Basic plotting
- **Seaborn**: Statistical visualization
- **Plotly**: Interactive plots
- **Bokeh**: Dashboards

### Experiment Tracking
- **MLflow**: Experiment tracking and model registry
- **Weights & Biases**: Advanced experiment tracking
- **TensorBoard**: Training visualization

### Backtesting
- **Backtrader**: Backtesting framework
- **Zipline**: Quantopian's backtesting engine
- **VectorBT**: Vectorized backtesting

## Code Style and Best Practices

### Python Style Guide
- Follow PEP 8 style guidelines
- Use type hints for function signatures
- Write docstrings for all public functions
- Keep functions focused and modular

### Code Organization
```python
# Example module structure
"""
Module description.

This module provides functionality for...
"""

from typing import Dict, List, Optional
import pandas as pd
import numpy as np

def example_function(param1: str, param2: int) -> Dict[str, float]:
    """
    Brief function description.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Dictionary with results

    Raises:
        ValueError: If inputs are invalid
    """
    # Implementation
    pass

if __name__ == "__main__":
    # Example usage
    result = example_function("test", 42)
    print(result)
```

### Testing
- **Unit Tests**: pytest for individual functions
- **Integration Tests**: End-to-end pipeline tests
- **Coverage**: Aim for >80% code coverage
- **Continuous Integration**: GitHub Actions or similar

### Documentation
- **Code Comments**: Explain non-obvious logic
- **README**: Each subdirectory should have a README
- **API Docs**: Sphinx or MkDocs for API documentation
- **Examples**: Jupyter notebooks demonstrating usage

### Version Control
- **Git**: Version control for all code
- **Branching**: Feature branches for development
- **Commits**: Descriptive commit messages
- **Tags**: Version tags for releases

## Running Experiments

### Basic Experiment
```bash
cd experiments/price_prediction
python train.py --config ../configs/training_config.yaml
```

### Hyperparameter Tuning
```bash
python tune.py --experiment price_prediction --n_trials 100
```

### Backtesting
```bash
cd ../backtesting
python backtest.py --strategy sentiment_momentum --start 2020-01-01
```

### Evaluation
```bash
python evaluate.py --checkpoint models/best_model.pt --data test
```

## Performance Optimization

### GPU Acceleration
- Use CUDA-enabled PyTorch for training
- Batch processing for inference
- Mixed precision training (FP16)

### Parallel Processing
- Multiprocessing for data loading
- Parallel hyperparameter search
- Distributed training across GPUs

### Memory Optimization
- Data streaming for large datasets
- Gradient checkpointing for large models
- Model pruning and quantization

## Deployment Considerations

### Model Serving
- **FastAPI**: REST API for model inference
- **TorchServe**: PyTorch model serving
- **Docker**: Containerized deployment
- **Kubernetes**: Orchestration for scaling

### Monitoring
- **Prometheus**: Metrics collection
- **Grafana**: Visualization dashboards
- **Logging**: Structured logging with ELK stack

### A/B Testing
- Experiment comparison framework
- Statistical significance testing
- Performance tracking

## Contributing

When adding new code:

1. **Follow conventions**: Match existing code style
2. **Add tests**: Unit tests for new functionality
3. **Update docs**: README and docstrings
4. **Code review**: Get review before merging
5. **Version control**: Use feature branches

## Troubleshooting

### Common Issues
- **CUDA out of memory**: Reduce batch size or use gradient checkpointing
- **Data loading slow**: Use caching and parallel loading
- **Model not converging**: Check learning rate, data normalization
- **Reproducibility issues**: Set random seeds, fix software versions

### Debugging Tips
- Use `pdb` or `ipdb` for debugging
- Enable verbose logging
- Validate data before training
- Start with small datasets for testing
