"""
Sentiment analysis utilities for financial text.

This module provides functions for sentiment analysis, aggregation,
and visualization of financial sentiment data.
"""

from typing import Dict, List, Optional, Tuple
import numpy as np
import pandas as pd
from transformers import pipeline
from textblob import TextBlob
import torch


class FinancialSentimentAnalyzer:
    """
    Sentiment analyzer specifically designed for financial text.

    Supports multiple sentiment models and aggregation strategies.
    """

    def __init__(
        self,
        model_name: str = "ProsusAI/finbert",
        use_gpu: bool = True,
    ):
        """
        Initialize sentiment analyzer.

        Args:
            model_name: Hugging Face model for sentiment analysis
            use_gpu: Whether to use GPU acceleration
        """
        self.device = "cuda" if (use_gpu and torch.cuda.is_available()) else "cpu"
        self.model_name = model_name

        # Load sentiment pipeline
        self.sentiment_pipeline = pipeline(
            "sentiment-analysis",
            model=model_name,
            device=0 if self.device == "cuda" else -1,
        )

        # Sentiment label mapping for FinBERT
        # FinBERT uses: Positive, Negative, Neutral
        self.label_mapping = {
            "LABEL_0": "negative",
            "LABEL_1": "neutral",
            "LABEL_2": "positive",
        }

    def analyze_text(
        self,
        text: str,
        return_scores: bool = True,
    ) -> Dict[str, any]:
        """
        Analyze sentiment of a single text.

        Args:
            text: Input text
            return_scores: Whether to return individual label scores

        Returns:
            Dictionary with sentiment label and scores
        """
        # Truncate text if too long
        max_length = 512
        if len(text) > max_length * 4:  # Approximate token limit
            text = text[:max_length * 4]

        # Get prediction
        result = self.sentiment_pipeline(text)[0]

        # Map label
        sentiment_label = self.label_mapping.get(
            result["label"],
            result["label"].lower(),
        )

        output = {
            "sentiment": sentiment_label,
            "score": result["score"],
        }

        if return_scores:
            # Get all label scores (requires running model with output_all_scores=True)
            output["scores"] = self._get_all_scores(text)

        return output

    def _get_all_scores(self, text: str) -> Dict[str, float]:
        """
        Get sentiment scores for all labels.

        Args:
            text: Input text

        Returns:
            Dictionary with scores for all labels
        """
        # This is a simplified version
        # In practice, you'd need to access the model directly
        result = self.sentiment_pipeline(text, return_all_scores=True)[0]
        scores = {
            self.label_mapping.get(r["label"], r["label"].lower()): r["score"]
            for r in result
        }
        return scores

    def analyze_batch(
        self,
        texts: List[str],
        batch_size: int = 32,
    ) -> List[Dict[str, any]]:
        """
        Analyze sentiment for multiple texts.

        Args:
            texts: List of input texts
            batch_size: Batch size for processing

        Returns:
            List of sentiment dictionaries
        """
        results = []

        for i in range(0, len(texts), batch_size):
            batch = texts[i : i + batch_size]
            batch_results = self.sentiment_pipeline(batch)
            results.extend(batch_results)

        # Format results
        formatted_results = []
        for result in results:
            sentiment_label = self.label_mapping.get(
                result["label"],
                result["label"].lower(),
            )
            formatted_results.append({
                "sentiment": sentiment_label,
                "score": result["score"],
            })

        return formatted_results

    def analyze_dataframe(
        self,
        df: pd.DataFrame,
        text_column: str = "text",
        batch_size: int = 32,
    ) -> pd.DataFrame:
        """
        Analyze sentiment for all texts in a DataFrame.

        Args:
            df: Input DataFrame
            text_column: Column containing text to analyze
            batch_size: Batch size for processing

        Returns:
            DataFrame with added sentiment columns
        """
        # Analyze sentiment
        results = self.analyze_batch(
            df[text_column].tolist(),
            batch_size=batch_size,
        )

        # Add to DataFrame
        df = df.copy()
        df["sentiment"] = [r["sentiment"] for r in results]
        df["sentiment_score"] = [r["score"] for r in results]

        # Convert sentiment to numeric
        sentiment_numeric = {
            "positive": 1,
            "neutral": 0,
            "negative": -1,
        }
        df["sentiment_numeric"] = df["sentiment"].map(sentiment_numeric)

        return df


class SentimentAggregator:
    """
    Aggregate sentiment scores over time and across sources.
    """

    def __init__(
        self,
        sentiment_column: str = "sentiment_numeric",
        score_column: str = "sentiment_score",
    ):
        """
        Initialize sentiment aggregator.

        Args:
            sentiment_column: Column with sentiment labels
            score_column: Column with sentiment confidence scores
        """
        self.sentiment_column = sentiment_column
        self.score_column = score_column

    def aggregate_by_time(
        self,
        df: pd.DataFrame,
        time_column: str = "timestamp",
        freq: str = "D",
        aggregation: str = "mean",
    ) -> pd.DataFrame:
        """
        Aggregate sentiment over time periods.

        Args:
            df: Input DataFrame with timestamp and sentiment
            time_column: Column with timestamps
            freq: Aggregation frequency (D=daily, W=weekly, M=monthly)
            aggregation: Aggregation method (mean, sum, ewm)

        Returns:
            Aggregated DataFrame
        """
        # Ensure timestamp is datetime
        df = df.copy()
        df[time_column] = pd.to_datetime(df[time_column])
        df = df.set_index(time_column)

        # Aggregate
        if aggregation == "mean":
            agg_sentiment = df[self.sentiment_column].resample(freq).mean()
            agg_score = df[self.score_column].resample(freq).mean()
        elif aggregation == "sum":
            agg_sentiment = df[self.sentiment_column].resample(freq).sum()
            agg_score = df[self.score_column].resample(freq).mean()
        elif aggregation == "ewm":
            # Exponential weighted moving average
            span = 5 if freq == "D" else 20 if freq == "W" else 60
            agg_sentiment = df[self.sentiment_column].ewm(span=span).mean()
            agg_score = df[self.score_column].ewm(span=span).mean()
        else:
            raise ValueError(f"Unknown aggregation: {aggregation}")

        result = pd.DataFrame({
            "sentiment_aggregated": agg_sentiment,
            "score_aggregated": agg_score,
        })

        return result

    def aggregate_by_source(
        self,
        df: pd.DataFrame,
        source_column: str = "source",
        time_column: str = "timestamp",
        freq: str = "D",
    ) -> pd.DataFrame:
        """
        Aggregate sentiment by source over time.

        Args:
            df: Input DataFrame
            source_column: Column with source identifiers
            time_column: Column with timestamps
            freq: Aggregation frequency

        Returns:
            Aggregated DataFrame with multi-level index (time, source)
        """
        df = df.copy()
        df[time_column] = pd.to_datetime(df[time_column])
        df = df.set_index(time_column)

        # Group by source and time
        grouped = df.groupby([pd.Grouper(freq=freq), source_column])

        result = grouped.agg({
            self.sentiment_column: "mean",
            self.score_column: "mean",
            "text": "count",  # Count of documents
        })

        result.columns = ["sentiment_mean", "score_mean", "doc_count"]

        return result

    def compute_sentiment_momentum(
        self,
        df: pd.DataFrame,
        sentiment_column: str = "sentiment_aggregated",
        window: int = 5,
    ) -> pd.DataFrame:
        """
        Compute sentiment momentum (rate of change).

        Args:
            df: Input DataFrame with aggregated sentiment
            sentiment_column: Column with sentiment values
            window: Rolling window for momentum calculation

        Returns:
            DataFrame with added momentum column
        """
        df = df.copy()

        # Calculate momentum as difference from window ago
        df["sentiment_momentum"] = df[sentiment_column].diff(window)

        # Normalize by rolling standard deviation
        rolling_std = df[sentiment_column].rolling(window=window).std()
        df["sentiment_momentum_norm"] = df["sentiment_momentum"] / rolling_std

        return df


class SentimentFeatureEngineer:
    """
    Engineer features from sentiment data for ML models.
    """

    @staticmethod
    def create_lag_features(
        df: pd.DataFrame,
        column: str,
        lags: List[int] = [1, 2, 3, 5, 10],
    ) -> pd.DataFrame:
        """
        Create lagged sentiment features.

        Args:
            df: Input DataFrame
            column: Column to create lags for
            lags: List of lag periods

        Returns:
            DataFrame with added lag features
        """
        df = df.copy()
        for lag in lags:
            df[f"{column}_lag_{lag}"] = df[column].shift(lag)
        return df

    @staticmethod
    def create_rolling_features(
        df: pd.DataFrame,
        column: str,
        windows: List[int] = [5, 10, 20],
    ) -> pd.DataFrame:
        """
        Create rolling window sentiment features.

        Args:
            df: Input DataFrame
            column: Column to compute rolling stats for
            windows: List of window sizes

        Returns:
            DataFrame with added rolling features
        """
        df = df.copy()
        for window in windows:
            df[f"{column}_rolling_mean_{window}"] = (
                df[column].rolling(window=window).mean()
            )
            df[f"{column}_rolling_std_{window}"] = (
                df[column].rolling(window=window).std()
            )
            df[f"{column}_rolling_min_{window}"] = (
                df[column].rolling(window=window).min()
            )
            df[f"{column}_rolling_max_{window}"] = (
                df[column].rolling(window=window).max()
            )
        return df

    @staticmethod
    def create_sentiment_regime_features(
        df: pd.DataFrame,
        column: str,
        threshold: float = 0.5,
    ) -> pd.DataFrame:
        """
        Create regime-based features (bullish, bearish, neutral).

        Args:
            df: Input DataFrame
            column: Sentiment column
            threshold: Threshold for regime classification

        Returns:
            DataFrame with added regime features
        """
        df = df.copy()

        # Classify regimes
        df["regime"] = "neutral"
        df.loc[df[column] > threshold, "regime"] = "bullish"
        df.loc[df[column] < -threshold, "regime"] = "bearish"

        # One-hot encode
        df["regime_bullish"] = (df["regime"] == "bullish").astype(int)
        df["regime_bearish"] = (df["regime"] == "bearish").astype(int)
        df["regime_neutral"] = (df["regime"] == "neutral").astype(int)

        return df


def compute_sentiment_return_correlation(
    sentiment_df: pd.DataFrame,
    price_df: pd.DataFrame,
    sentiment_column: str = "sentiment_numeric",
    return_column: str = "return",
    lags: List[int] = [0, 1, 2, 5],
) -> pd.DataFrame:
    """
    Compute correlation between sentiment and returns at various lags.

    Args:
        sentiment_df: DataFrame with sentiment data
        price_df: DataFrame with price data
        sentiment_column: Column with sentiment values
        return_column: Column with return values
        lags: List of lag periods to test

    Returns:
        DataFrame with correlation coefficients
    """
    # Merge on date
    merged = pd.merge(
        sentiment_df,
        price_df,
        left_index=True,
        right_index=True,
        how="inner",
    )

    correlations = {}
    for lag in lags:
        if lag == 0:
            corr = merged[sentiment_column].corr(merged[return_column])
        else:
            corr = merged[sentiment_column].corr(merged[return_column].shift(-lag))
        correlations[f"lag_{lag}"] = corr

    return pd.DataFrame.from_dict(correlations, orient="index", columns=["correlation"])


if __name__ == "__main__":
    # Example usage
    analyzer = FinancialSentimentAnalyzer()

    # Sample texts
    texts = [
        "Apple reports strong earnings",
        "Market declines on recession fears",
        "Fed maintains interest rates",
    ]

    # Analyze sentiment
    for text in texts:
        result = analyzer.analyze_text(text)
        print(f"\nText: {text}")
        print(f"Sentiment: {result['sentiment']}")
        print(f"Score: {result['score']:.3f}")
