# Training and Alignment Implementations

## Overview

This directory contains implementations of training methods and techniques to reduce hallucinations in LLMs.

## Training Methods

### 1. Retrieval-Augmented Generation (RAG)

```python
# code/training/rag_trainer.py

class RAGTrainer:
    """Train RAG models for reduced hallucination"""

    def __init__(self, base_model, retriever, config):
        self.model = base_model
        self.retriever = retriever
        self.config = config

    def train(self, train_data, eval_data):
        """
        Train a RAG model

        Args:
            train_data: Training corpus with documents and queries
            eval_data: Evaluation data
        """
        # Train retriever
        self.train_retriever(train_data)

        # Fine-tune generator with retrieved context
        self.train_generator(train_data)

        # Evaluate
        results = self.evaluate(eval_data)
        return results

    def train_retriever(self, train_data):
        """Train the retriever component"""
        # Create embeddings for documents
        documents = train_data["documents"]
        doc_embeddings = self.embed_documents(documents)

        # Train dual encoder
        optimizer = torch.optim.Adam(self.retriever.parameters(), lr=1e-5)

        for epoch in range(self.config.num_epochs):
            for batch in train_data["queries"]:
                # Positive and negative samples
                query = batch["query"]
                pos_doc = batch["positive_doc"]
                neg_docs = batch["negative_docs"]

                # Compute loss
                loss = self.contrastive_loss(query, pos_doc, neg_docs)

                # Update
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

    def train_generator(self, train_data):
        """Fine-tune generator with retrieved context"""
        optimizer = torch.optim.AdamW(self.model.parameters(), lr=1e-5)

        for batch in train_data:
            # Retrieve relevant documents
            query = batch["query"]
            context = self.retriever.retrieve(query, top_k=5)

            # Format input with context
            input_text = self.format_with_context(query, context)

            # Generate
            output = self.model(input_text)

            # Calculate loss
            loss = self.calculate_loss(output, batch["target"])

            # Update
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

    def format_with_context(self, query, context):
        """Format input with retrieved context"""
        context_str = "\n".join([f"- {doc}" for doc in context])
        return f"Context:\n{context_str}\n\nQuestion: {query}\nAnswer:"
```

### 2. RLHF for Truthfulness

```python
# code/training/rlhf_trainer.py

class TruthfulnessRLHFTrainer:
    """RLHF trainer focused on truthfulness"""

    def __init__(self, policy_model, reward_model, config):
        self.policy = policy_model
        self.reward_model = reward_model
        self.config = config
        self.ref_policy = copy.deepcopy(policy_model)

    def train(self, preference_data):
        """
        Train using PPO with truthfulness-focused rewards

        Args:
            preference_data: Data with preference pairs (chosen, rejected)
        """
        # Train reward model
        self.train_reward_model(preference_data)

        # Train policy with PPO
        for epoch in range(self.config.num_epochs):
            for batch in preference_data:
                # Generate samples
                prompt = batch["prompt"]
                response = self.policy.generate(prompt)

                # Calculate reward
                reward = self.reward_model.get_reward(prompt, response)

                # Calculate PPO loss
                loss = self.ppo_loss(prompt, response, reward)

                # Update policy
                loss.backward()

    def train_reward_model(self, preference_data):
        """Train reward model on preference data"""
        optimizer = torch.optim.Adam(self.reward_model.parameters())

        for batch in preference_data:
            # Get rewards for chosen and rejected
            chosen_reward = self.reward_model(
                batch["prompt"], batch["chosen_response"]
            )
            rejected_reward = self.reward_model(
                batch["prompt"], batch["rejected_response"]
            )

            # Ranking loss
            loss = -torch.log(
                torch.sigmoid(chosen_reward - rejected_reward)
            ).mean()

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

    def calculate_truthfulness_reward(self, prompt, response):
        """
        Calculate reward based on truthfulness
        """
        # Fact-checking
        factuality_score = self.fact_check(response)

        # Self-consistency
        consistency_score = self.check_consistency(prompt, response)

        # Uncertainty penalty
        uncertainty_penalty = self.calculate_uncertainty(response)

        # Combine
        reward = (
            0.5 * factuality_score +
            0.3 * consistency_score -
            0.2 * uncertainty_penalty
        )

        return reward
```

### 3. Constitutional AI Training

```python
# code/training/constitutional_ai.py

class ConstitutionalAITrainer:
    """Train models using Constitutional AI principles"""

    def __init__(self, model, constitution):
        self.model = model
        self.constitution = constitution  # List of principles

    def train(self, red_team_data):
        """
        Train using critique and revision

        Args:
            red_team_data: Examples of model failures
        """
        # Stage 1: Supervised learning from revisions
        self.train_revisions(red_team_data)

        # Stage 2: AI feedback training
        self.train_constitutional_feedback(red_team_data)

    def train_revisions(self, red_team_data):
        """Train on revised responses following constitution"""
        for example in red_team_data:
            # Generate critique
            critique = self.generate_critique(
                example["prompt"],
                example["response"],
                self.constitution
            )

            # Generate revision
            revision = self.generate_revision(
                example["prompt"],
                example["response"],
                critique
            )

            # Train on revision
            self.train_on_example(example["prompt"], revision)

    def generate_critique(self, prompt, response, constitution):
        """Generate critique based on constitutional principles"""
        critique_prompt = f"""
        Response to critique: {response}

        Constitutional principles:
        {self.format_principles(constitution)}

        Critique the response based on these principles.
        """

        return self.model.generate(critique_prompt)

    def format_principles(self, constitution):
        """Format constitutional principles"""
        return "\n".join([
            f"{i+1}. {principle}"
            for i, principle in enumerate(constitution)
        ])
```

### 4. Instruction Tuning for Factuality

```python
# code/training/instruction_tuning.py

class FactualityInstructionTuner:
    """Instruction tuning focused on factual accuracy"""

    def __init__(self, model, config):
        self.model = model
        self.config = config

    def prepare_training_data(self, raw_data):
        """
        Prepare instruction tuning data with emphasis on factuality

        Args:
            raw_data: Raw factual QA pairs
        """
        training_examples = []

        for example in raw_data:
            # Create multiple instruction formats
            templates = [
                "Answer the following question accurately: {question}",
                "Provide a factual answer to: {question}",
                "What is the correct answer to: {question}",
            ]

            for template in templates:
                prompt = template.format(question=example["question"])

                training_examples.append({
                    "prompt": prompt,
                    "completion": example["answer"],
                    "metadata": {
                        "source": example["source"],
                        "confidence": example.get("confidence", 1.0)
                    }
                })

        return training_examples

    def train(self, training_data):
        """Train with factuality-focused loss"""
        optimizer = torch.optim.AdamW(
            self.model.parameters(),
            lr=self.config.learning_rate
        )

        for epoch in range(self.config.num_epochs):
            for batch in training_data:
                # Forward pass
                loss = self.calculate_factuality_loss(batch)

                # Backward pass
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

    def calculate_factuality_loss(self, batch):
        """Calculate loss with factuality weighting"""
        # Standard language modeling loss
        lm_loss = self.model.calculate_loss(batch["prompt"], batch["completion"])

        # Factuality weighting
        confidence = batch["metadata"]["confidence"]

        # Weight by confidence (high confidence = higher weight)
        weighted_loss = lm_loss * confidence

        return weighted_loss
```

## Training Configuration

### Example Config
```yaml
# configs/training/rag.yaml

model:
  base_model: "llama-2-7b"
  max_length: 512

retriever:
  type: "dense"
  embedding_model: "sentence-transformers/all-MiniLM-L6-v2"
  index_type: "faiss"
  top_k: 5

training:
  num_epochs: 3
  batch_size: 8
  learning_rate: 1.0e-5
  gradient_accumulation_steps: 4
  warmup_steps: 100

optimizer:
  type: "AdamW"
  weight_decay: 0.01

evaluation:
  eval_steps: 500
  benchmarks:
    - "truthfulqa"
    - "factscore"
```

## Training Scripts

### Main Training Script
```bash
# scripts/train.sh

#!/bin/bash

python train.py \
  --config configs/training/rag.yaml \
  --data_dir data/training \
  --output_dir outputs/rag_model \
  --num_train_epochs 3 \
  --per_device_train_batch_size 8 \
  --gradient_accumulation_steps 4 \
  --learning_rate 1e-5 \
  --warmup_steps 100 \
  --logging_steps 10 \
  --eval_steps 500 \
  --save_steps 500
```

### Evaluation Script
```bash
# scripts/evaluate.sh

#!/bin/bash

python evaluate.py \
  --model_dir outputs/rag_model \
  --benchmarks truthfulqa factscore \
  --output_dir outputs/evaluation \
  --batch_size 16
```

## Data Preparation

### RAG Training Data
```python
# scripts/prepare_rag_data.py

def prepare_rag_data(corpus, queries):
    """
    Prepare training data for RAG

    Args:
        corpus: Collection of documents
        queries: Query-document pairs
    """
    # Chunk documents
    chunks = chunk_documents(corpus, chunk_size=512)

    # Create training pairs
    training_data = []
    for query in queries:
        relevant_docs = find_relevant_docs(query, chunks)
        training_data.append({
            "query": query,
            "documents": relevant_docs
        })

    return training_data
```

### RLHF Preference Data
```python
# scripts/prepare_rlhf_data.py

def create_preference_pairs(qa_data):
    """
    Create preference pairs for RLHF

    Args:
        qa_data: QA pairs with correctness labels
    """
    preference_pairs = []

    for item in qa_data:
        # Correct answer as "chosen"
        chosen = item["correct_answer"]

        # Incorrect answer as "rejected"
        rejected = item["incorrect_answer"]

        preference_pairs.append({
            "prompt": item["question"],
            "chosen": chosen,
            "rejected": rejected
        })

    return preference_pairs
```

## Monitoring

### TensorBoard Setup
```python
# code/training/logger.py

from torch.utils.tensorboard import SummaryWriter

class TrainingLogger:
    """Log training metrics"""

    def __init__(self, log_dir):
        self.writer = SummaryWriter(log_dir)

    def log_metrics(self, metrics, step):
        """Log metrics to TensorBoard"""
        for key, value in metrics.items():
            self.writer.add_scalar(key, value, step)

    def log_embeddings(self, embeddings, labels, step):
        """Log embeddings for visualization"""
        self.writer.add_embedding(embeddings, metadata=labels, global_step=step)
```

## Related Files
- `/papers/alignment/` - Papers on training methods
- `/data/baselines/` - Baseline models
- `/experiments/` - Training experiments and results
