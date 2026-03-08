"""
Financial BERT: Fine-tuned BERT model for financial text analysis.

This module provides a fine-tuned BERT model specifically designed for
financial sentiment analysis and document understanding.
"""

from typing import Dict, List, Optional, Tuple
import torch
import torch.nn as nn
from transformers import (
    AutoModelForSequenceClassification,
    AutoTokenizer,
    Trainer,
    TrainingArguments,
)
from datasets import Dataset


class FinancialBERT(nn.Module):
    """
    Financial BERT model for sentiment analysis and classification tasks.

    This model wraps a pre-trained BERT model and specializes it for
    financial text classification tasks such as sentiment analysis,
    topic classification, and financial document understanding.

    Attributes:
        model: The underlying BERT model
        tokenizer: Tokenizer for text preprocessing
        num_labels: Number of classification labels
    """

    def __init__(
        self,
        model_name: str = "ProsusAI/finbert",
        num_labels: int = 3,
        max_length: int = 512,
    ):
        """
        Initialize Financial BERT model.

        Args:
            model_name: Hugging Face model identifier
            num_labels: Number of classification labels
            max_length: Maximum sequence length
        """
        super().__init__()
        self.model_name = model_name
        self.num_labels = num_labels
        self.max_length = max_length

        # Load pre-trained model and tokenizer
        self.model = AutoModelForSequenceClassification.from_pretrained(
            model_name,
            num_labels=num_labels,
        )
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def forward(
        self,
        input_ids: torch.Tensor,
        attention_mask: torch.Tensor,
        labels: Optional[torch.Tensor] = None,
    ) -> Dict[str, torch.Tensor]:
        """
        Forward pass through the model.

        Args:
            input_ids: Tokenized input sequences
            attention_mask: Attention mask for padding
            labels: Ground truth labels (optional)

        Returns:
            Dictionary containing loss and logits
        """
        outputs = self.model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            labels=labels,
        )
        return {
            "loss": outputs.loss,
            "logits": outputs.logits,
        }

    def predict(self, texts: List[str]) -> List[Dict[str, float]]:
        """
        Make predictions on a list of texts.

        Args:
            texts: List of input texts

        Returns:
            List of prediction dictionaries with labels and scores
        """
        self.eval()
        predictions = []

        with torch.no_grad():
            for text in texts:
                # Tokenize
                inputs = self.tokenizer(
                    text,
                    max_length=self.max_length,
                    truncation=True,
                    padding="max_length",
                    return_tensors="pt",
                )

                # Forward pass
                outputs = self.model(**inputs)
                probs = torch.nn.functional.softmax(outputs.logits, dim=-1)

                # Get prediction
                pred_label = torch.argmax(probs, dim=-1).item()
                pred_score = probs[0, pred_label].item()

                predictions.append({
                    "label": pred_label,
                    "score": pred_score,
                    "probabilities": probs[0].tolist(),
                })

        return predictions

    def fine_tune(
        self,
        train_dataset: Dataset,
        val_dataset: Optional[Dataset] = None,
        output_dir: str = "./results",
        num_epochs: int = 3,
        learning_rate: float = 2e-5,
        batch_size: int = 16,
    ) -> Trainer:
        """
        Fine-tune the model on a custom dataset.

        Args:
            train_dataset: Training dataset
            val_dataset: Validation dataset (optional)
            output_dir: Directory to save results
            num_epochs: Number of training epochs
            learning_rate: Learning rate
            batch_size: Training batch size

        Returns:
            Trained Trainer object
        """
        # Tokenize datasets
        def tokenize_function(examples):
            return self.tokenizer(
                examples["text"],
                max_length=self.max_length,
                truncation=True,
                padding="max_length",
            )

        tokenized_train = train_dataset.map(tokenize_function, batched=True)
        if val_dataset:
            tokenized_val = val_dataset.map(tokenize_function, batched=True)

        # Training arguments
        training_args = TrainingArguments(
            output_dir=output_dir,
            num_train_epochs=num_epochs,
            per_device_train_batch_size=batch_size,
            per_device_eval_batch_size=batch_size,
            learning_rate=learning_rate,
            evaluation_strategy="epoch" if val_dataset else "no",
            save_strategy="epoch",
            logging_dir=f"{output_dir}/logs",
            logging_steps=100,
            load_best_model_at_end=True if val_dataset else False,
            metric_for_best_model="eval_loss" if val_dataset else None,
        )

        # Initialize trainer
        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=tokenized_train,
            eval_dataset=tokenized_val if val_dataset else None,
        )

        # Train
        trainer.train()

        return trainer

    def extract_features(
        self,
        texts: List[str],
        layer: int = -1,
    ) -> torch.Tensor:
        """
        Extract contextual embeddings from the model.

        Args:
            texts: List of input texts
            layer: Which layer to extract features from (-1 for last layer)

        Returns:
            Tensor of shape (batch_size, seq_length, hidden_size)
        """
        self.eval()
        features = []

        with torch.no_grad():
            for text in texts:
                inputs = self.tokenizer(
                    text,
                    max_length=self.max_length,
                    truncation=True,
                    padding="max_length",
                    return_tensors="pt",
                )

                # Get hidden states
                outputs = self.model(**inputs, output_hidden_states=True)
                hidden_states = outputs.hidden_states[layer]

                # Use [CLS] token representation
                cls_embedding = hidden_states[:, 0, :]
                features.append(cls_embedding)

        return torch.cat(features, dim=0)


class MultiLabelFinancialBERT(FinancialBERT):
    """
    Multi-label Financial BERT for tasks like topic classification.

    Extends FinancialBERT to handle multiple labels per instance.
    """

    def __init__(
        self,
        model_name: str = "ProsusAI/finbert",
        num_labels: int = 10,
        max_length: int = 512,
        threshold: float = 0.5,
    ):
        """
        Initialize multi-label Financial BERT.

        Args:
            model_name: Hugging Face model identifier
            num_labels: Number of possible labels
            max_length: Maximum sequence length
            threshold: Classification threshold
        """
        super().__init__(model_name, num_labels, max_length)
        self.threshold = threshold

        # Replace classification head with multi-label head
        self.model.classifier = nn.Sequential(
            nn.Linear(self.model.config.hidden_size, 256),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(256, num_labels),
        )

    def predict(self, texts: List[str]) -> List[Dict[str, any]]:
        """
        Make multi-label predictions.

        Args:
            texts: List of input texts

        Returns:
            List of prediction dictionaries with active labels
        """
        self.eval()
        predictions = []

        with torch.no_grad():
            for text in texts:
                inputs = self.tokenizer(
                    text,
                    max_length=self.max_length,
                    truncation=True,
                    padding="max_length",
                    return_tensors="pt",
                )

                outputs = self.model(**inputs)
                probs = torch.sigmoid(outputs.logits)

                # Get active labels
                active_labels = (probs > self.threshold).squeeze().tolist()

                predictions.append({
                    "labels": active_labels,
                    "probabilities": probs.squeeze().tolist(),
                })

        return predictions


if __name__ == "__main__":
    # Example usage
    model = FinancialBERT()

    # Sample financial headlines
    headlines = [
        "Apple reports record quarterly earnings, stock surges",
        "Fed signals potential rate hike amid inflation concerns",
        "Tech sector faces headwinds from regulatory scrutiny",
    ]

    # Make predictions
    predictions = model.predict(headlines)

    for headline, pred in zip(headlines, predictions):
        print(f"\nHeadline: {headline}")
        print(f"Predicted Label: {pred['label']}")
        print(f"Confidence: {pred['score']:.3f}")
