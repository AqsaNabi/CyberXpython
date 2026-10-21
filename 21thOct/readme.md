## Topics Learned

### 1. Oversampling and Undersampling
- Learned about oversampling and undersampling techniques used to handle imbalanced datasets.
- Studied different types of oversampling and undersampling methods.
- **SMOTE (Synthetic Minority Over-sampling Technique):** Generates synthetic samples for the minority class to help balance a dataset.

### 2. Data Augmentation
- Learned how data augmentation increases training data diversity through transformations such as rotation, flipping, cropping, and resizing.

### 3. Transformers in Deep Learning

Studied the Transformer architecture in detail, including its components, attention mechanisms, mathematical formulas, and step-by-step working.

**RNN vs. LSTM vs. Transformer**
- **RNN:** Processes sequential data one step at a time.
- **LSTM:** Uses memory cells and gates to retain information over longer sequences.
- **Transformer:** Uses attention mechanisms to capture relationships between tokens and supports parallel processing during training.

**Transformer Architecture**
- Input sequence and tokenization
- Token embeddings and positional encoding
- Encoder and self-attention
- Feedforward neural network
- Decoder and masked self-attention
- Encoder-decoder attention (cross-attention)
- Output sequence generation
- Step-by-step workflow of an encoder-decoder Transformer for language translation

**Query, Key, and Value (Q, K, V)**
- **Query (Q):** Represents what a token is looking for.
- **Key (K):** Helps determine the relevance of other tokens.
- **Value (V):** Contains the information used to calculate the attention output.

**Scaled Dot-Product Attention**

Studied the attention formula and the role of each component.

\[
\operatorname{Attention}(Q,K,V)=
\operatorname{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
\]

- \(Q\): Query matrix
- \(K^T\): Transposed key matrix
- \(V\): Value matrix
- \(d_k\): Dimension of the key vectors
- **Softmax:** Converts scaled similarity scores into attention weights.

**Multi-Head Attention**
- Learned how multiple attention heads capture different relationships between tokens and combine their outputs into richer representations.

### 4. Introduction to AI Concepts

Covered the following topics at an introductory level:

- **AI vs. AGI:** Difference between Artificial Intelligence and Artificial General Intelligence.
- **Large Language Models (LLMs):** Basic working of LLMs and how they generate text.
- **LLMs vs. RNNs:** Why Transformer-based architectures are widely used in modern language models.
- **Embeddings:** Representing text or other data as numerical vectors.
- **Inference:** Using a trained model to generate predictions or outputs.
- **AI Agents:** AI systems that can make decisions, pursue goals, and use tools to perform tasks.