"""
Financial metrics and evaluation functions.

This module provides functions for calculating financial performance metrics,
risk measures, and portfolio evaluation metrics.
"""

from typing import Dict, List, Optional, Tuple
import numpy as np
import pandas as pd
from scipy import stats


def calculate_returns(
    prices: pd.Series,
    method: str = "simple",
) -> pd.Series:
    """
    Calculate returns from price series.

    Args:
        prices: Series of prices
        method: 'simple' or 'log' returns

    Returns:
        Series of returns
    """
    if method == "simple":
        return prices.pct_change().fillna(0)
    elif method == "log":
        return np.log(prices / prices.shift(1)).fillna(0)
    else:
        raise ValueError(f"Unknown return method: {method}")


def calculate_volatility(
    returns: pd.Series,
    window: Optional[int] = None,
    annualize: bool = True,
    trading_days: int = 252,
) -> float:
    """
    Calculate volatility (standard deviation of returns).

    Args:
        returns: Series of returns
        window: Rolling window size (None for full period)
        annualize: Whether to annualize the volatility
        trading_days: Number of trading days per year

    Returns:
        Volatility value
    """
    if window:
        vol = returns.rolling(window=window).std().iloc[-1]
    else:
        vol = returns.std()

    if annualize:
        vol = vol * np.sqrt(trading_days)

    return vol


def calculate_sharpe_ratio(
    returns: pd.Series,
    risk_free_rate: float = 0.0,
    annualize: bool = True,
    trading_days: int = 252,
) -> float:
    """
    Calculate Sharpe ratio.

    Args:
        returns: Series of returns
        risk_free_rate: Annual risk-free rate
        annualize: Whether to annualize the ratio
        trading_days: Number of trading days per year

    Returns:
        Sharpe ratio
    """
    # Convert annual risk-free rate to daily
    daily_rf = risk_free_rate / trading_days

    # Calculate excess returns
    excess_returns = returns - daily_rf

    # Calculate Sharpe ratio
    if annualize:
        sharpe = excess_returns.mean() / excess_returns.std() * np.sqrt(trading_days)
    else:
        sharpe = excess_returns.mean() / excess_returns.std()

    return sharpe


def calculate_sortino_ratio(
    returns: pd.Series,
    risk_free_rate: float = 0.0,
    annualize: bool = True,
    trading_days: int = 252,
) -> float:
    """
    Calculate Sortino ratio (downside risk-adjusted return).

    Args:
        returns: Series of returns
        risk_free_rate: Annual risk-free rate
        annualize: Whether to annualize the ratio
        trading_days: Number of trading days per year

    Returns:
        Sortino ratio
    """
    daily_rf = risk_free_rate / trading_days
    excess_returns = returns - daily_rf

    # Calculate downside deviation (only negative returns)
    downside_returns = excess_returns[excess_returns < 0]
    downside_deviation = downside_returns.std()

    if downside_deviation == 0:
        return np.inf

    if annualize:
        sortino = excess_returns.mean() / downside_deviation * np.sqrt(trading_days)
    else:
        sortino = excess_returns.mean() / downside_deviation

    return sortino


def calculate_max_drawdown(
    prices: pd.Series,
) -> Tuple[float, pd.Timestamp, pd.Timestamp]:
    """
    Calculate maximum drawdown.

    Args:
        prices: Series of prices

    Returns:
        Tuple of (max_drawdown, peak_date, trough_date)
    """
    # Calculate cumulative returns
    cumulative = (1 + calculate_returns(prices)).cumprod()

    # Calculate running maximum
    running_max = cumulative.expanding().max()

    # Calculate drawdown
    drawdown = (cumulative - running_max) / running_max

    # Find maximum drawdown
    max_dd = drawdown.min()
    trough_date = drawdown.idxmin()

    # Find peak date (maximum before trough)
    peak_date = running_max[:trough_date].idxmax()

    return max_dd, peak_date, trough_date


def calculate_calmar_ratio(
    returns: pd.Series,
    annualize: bool = True,
    trading_days: int = 252,
) -> float:
    """
    Calculate Calmar ratio (annual return / maximum drawdown).

    Args:
        returns: Series of returns
        annualize: Whether to annualize the return
        trading_days: Number of trading days per year

    Returns:
        Calmar ratio
    """
    # Calculate cumulative return
    cumulative_return = (1 + returns).prod() - 1

    if annualize:
        years = len(returns) / trading_days
        annual_return = (1 + cumulative_return) ** (1 / years) - 1
    else:
        annual_return = cumulative_return

    # Calculate max drawdown
    prices = (1 + returns).cumprod()
    max_dd, _, _ = calculate_max_drawdown(prices)

    if max_dd == 0:
        return np.inf

    return annual_return / abs(max_dd)


def calculate_var(
    returns: pd.Series,
    confidence_level: float = 0.95,
    method: str = "historical",
) -> float:
    """
    Calculate Value at Risk (VaR).

    Args:
        returns: Series of returns
        confidence_level: Confidence level (e.g., 0.95 for 95% VaR)
        method: 'historical', 'parametric', or 'cornish_fisher'

    Returns:
        VaR value (negative number)
    """
    alpha = 1 - confidence_level

    if method == "historical":
        var = np.percentile(returns, alpha * 100)

    elif method == "parametric":
        # Assume normal distribution
        mu = returns.mean()
        sigma = returns.std()
        var = mu + sigma * stats.norm.ppf(alpha)

    elif method == "cornish_fisher":
        # Cornish-Fisher expansion (adjusts for skewness and kurtosis)
        mu = returns.mean()
        sigma = returns.std()
        skew = stats.skew(returns)
        kurt = stats.kurtosis(returns)

        # Z-score for confidence level
        z = stats.norm.ppf(alpha)

        # Cornish-Fisher adjustment
        t = z + (z**2 - 1) * skew / 6 + (z**3 - 3 * z) * kurt / 24 - (2 * z**3 - 5 * z) * skew**2 / 36

        var = mu + sigma * t

    else:
        raise ValueError(f"Unknown VaR method: {method}")

    return var


def calculate_cvar(
    returns: pd.Series,
    confidence_level: float = 0.95,
) -> float:
    """
    Calculate Conditional Value at Risk (CVaR) / Expected Shortfall.

    Args:
        returns: Series of returns
        confidence_level: Confidence level

    Returns:
        CVaR value (negative number)
    """
    var = calculate_var(returns, confidence_level, method="historical")
    cvar = returns[returns <= var].mean()
    return cvar


def calculate_information_ratio(
    returns: pd.Series,
    benchmark_returns: pd.Series,
) -> float:
    """
    Calculate Information Ratio (active return / tracking error).

    Args:
        returns: Strategy returns
        benchmark_returns: Benchmark returns

    Returns:
        Information ratio
    """
    # Align series
    aligned_returns, aligned_benchmark = returns.align(benchmark_returns, join="inner")

    # Calculate active returns
    active_returns = aligned_returns - aligned_benchmark

    # Calculate tracking error (std of active returns)
    tracking_error = active_returns.std()

    if tracking_error == 0:
        return 0.0

    # Calculate information ratio
    ir = active_returns.mean() / tracking_error

    return ir


def calculate_alpha_beta(
    returns: pd.Series,
    benchmark_returns: pd.Series,
    risk_free_rate: float = 0.0,
    trading_days: int = 252,
) -> Tuple[float, float]:
    """
    Calculate alpha and beta relative to benchmark.

    Args:
        returns: Strategy returns
        benchmark_returns: Benchmark returns
        risk_free_rate: Annual risk-free rate
        trading_days: Number of trading days per year

    Returns:
        Tuple of (alpha, beta)
    """
    # Align series
    aligned_returns, aligned_benchmark = returns.align(benchmark_returns, join="inner")

    # Calculate excess returns
    daily_rf = risk_free_rate / trading_days
    excess_returns = aligned_returns - daily_rf
    excess_benchmark = aligned_benchmark - daily_rf

    # Run regression
    cov_matrix = np.cov(excess_returns, excess_benchmark)
    beta = cov_matrix[0, 1] / cov_matrix[1, 1]

    # Alpha (annualized)
    alpha = (excess_returns.mean() - beta * excess_benchmark.mean()) * trading_days

    return alpha, beta


def calculate_portfolio_metrics(
    returns: pd.Series,
    benchmark_returns: Optional[pd.Series] = None,
    risk_free_rate: float = 0.0,
) -> Dict[str, float]:
    """
    Calculate comprehensive portfolio metrics.

    Args:
        returns: Strategy returns
        benchmark_returns: Benchmark returns (optional)
        risk_free_rate: Annual risk-free rate

    Returns:
        Dictionary of metrics
    """
    metrics = {}

    # Basic return metrics
    metrics["total_return"] = (1 + returns).prod() - 1
    metrics["annual_return"] = (1 + returns).mean() * 252
    metrics["volatility"] = calculate_volatility(returns)

    # Risk-adjusted returns
    metrics["sharpe_ratio"] = calculate_sharpe_ratio(returns, risk_free_rate)
    metrics["sortino_ratio"] = calculate_sortino_ratio(returns, risk_free_rate)
    metrics["calmar_ratio"] = calculate_calmar_ratio(returns)

    # Drawdown
    max_dd, peak_date, trough_date = calculate_max_drawdown(
        (1 + returns).cumprod(),
    )
    metrics["max_drawdown"] = max_dd

    # VaR and CVaR
    metrics["var_95"] = calculate_var(returns, 0.95)
    metrics["cvar_95"] = calculate_cvar(returns, 0.95)

    # Win rate
    metrics["win_rate"] = (returns > 0).mean()

    # Benchmark metrics
    if benchmark_returns is not None:
        aligned_returns, aligned_benchmark = returns.align(
            benchmark_returns,
            join="inner",
        )

        metrics["alpha"], metrics["beta"] = calculate_alpha_beta(
            aligned_returns,
            aligned_benchmark,
            risk_free_rate,
        )
        metrics["information_ratio"] = calculate_information_ratio(
            aligned_returns,
            aligned_benchmark,
        )

        metrics["benchmark_return"] = (1 + aligned_benchmark).prod() - 1
        metrics["excess_return"] = metrics["total_return"] - metrics["benchmark_return"]

    return metrics


def backtest_performance_summary(
    actual_returns: pd.Series,
    predicted_returns: pd.Series,
) -> Dict[str, float]:
    """
    Evaluate prediction performance for financial returns.

    Args:
        actual_returns: Actual returns
        predicted_returns: Predicted returns (or directions)

    Returns:
        Dictionary of evaluation metrics
    """
    # Align series
    actual, predicted = actual_returns.align(predicted_returns, join="inner")

    metrics = {}

    # Regression metrics
    metrics["mse"] = np.mean((actual - predicted) ** 2)
    metrics["mae"] = np.mean(np.abs(actual - predicted))
    metrics["rmse"] = np.sqrt(metrics["mse"])

    # Directional accuracy
    actual_direction = np.sign(actual)
    predicted_direction = np.sign(predicted)
    metrics["directional_accuracy"] = (actual_direction == predicted_direction).mean()

    # Correlation
    metrics["correlation"] = actual.corr(predicted)

    # Information coefficient (rank correlation)
    metrics["information_coefficient"] = actual.corr(predicted, method="spearman")

    return metrics


if __name__ == "__main__":
    # Example usage
    import yfinance as yf

    # Download price data
    ticker = "AAPL"
    data = yf.download(ticker, start="2023-01-01", end="2024-12-31")
    prices = data["Close"]

    # Calculate returns
    returns = calculate_returns(prices)

    # Calculate metrics
    metrics = calculate_portfolio_metrics(returns)

    print("Portfolio Metrics:")
    for key, value in metrics.items():
        if isinstance(value, float):
            print(f"{key}: {value:.4f}")
        else:
            print(f"{key}: {value}")
