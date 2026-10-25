<h2>Understanding Embeddings and Their Use Cases</h2>

<p>Today, I studied embeddings, how text is converted into numerical vectors, semantic similarity, embedding dimensions, and similarity search. I also explored how embeddings are used in semantic search, data classification, recommendation systems, and anomaly detection. Additionally, I learned about lexical search and the differences between dense and sparse retrieval.</p>

<h3>2.2 Understand Embeddings</h3>

<h3>1. What Are Embeddings?</h3>

<p>Embeddings are numerical representations of data, such as text, images, or other information. They convert data into vectors that machine learning models can process. In text applications, embeddings help represent the meaning and relationships between words, sentences, and documents.</p>

<h3>2. How Text Is Converted into Vectors</h3>

<p>An embedding model takes text as input and converts it into a list of numbers called a vector. The numbers represent learned features and relationships in the text.</p>

<p>For example, an embedding model may represent the sentences "I like dogs" and "I love puppies" with vectors that are relatively close because their meanings are similar.</p>

<p>The general process is:</p>
<ul>
<li>Provide text to an embedding model.</li>
<li>The model processes the text.</li>
<li>The model generates a numerical vector.</li>
<li>The vector can be stored, compared, or used in machine learning applications.</li>
</ul>

<h3>3. Semantic Similarity</h3>

<p>Semantic similarity measures how closely two pieces of text are related in meaning. Embeddings allow systems to compare text based on meaning rather than relying only on matching exact words.</p>

<p>For example, "How can I learn Python?" and "What is the best way to study Python programming?" use different words but have similar meanings. Their embeddings may therefore be close in vector space.</p>

<h3>4. Embedding Dimensions</h3>

<p>Embedding dimensions refer to the number of numerical values in a vector. For example, a 384-dimensional embedding contains 384 numbers, while a 768-dimensional embedding contains 768 numbers.</p>

<p>The number of dimensions depends on the embedding model. A larger dimension does not automatically mean better results; performance also depends on the model, data, and task.</p>

<h3>5. Similarity Search</h3>

<p>Similarity search finds items whose vectors are closest to a query vector. It is commonly used to retrieve relevant documents, find similar products, and search for information based on meaning.</p>

<p>Common comparison methods include:</p>
<ul>
<li><b>Cosine Similarity:</b> Measures the angle between two vectors.</li>
<li><b>Euclidean Distance:</b> Measures the straight-line distance between vectors.</li>
<li><b>Dot Product:</b> Measures the product of corresponding vector values summed together.</li>
</ul>

<p>The appropriate method depends on the embedding model and how its vectors are intended to be compared.</p>

<h3>2.3 Embedding Use Cases</h3>

<h3>1. Semantic Search</h3>

<p>Semantic search retrieves information based on meaning and context instead of relying only on exact keyword matches. It uses embeddings to find documents or passages that are relevant to a user's query, even when different words are used.</p>

<h3>2. Lexical Search</h3>

<p>Lexical search finds information by matching words or terms in a query with words in documents. It is useful when exact terms matter, such as searching for product codes, names, or specific technical keywords.</p>

<p>Unlike semantic search, traditional lexical search does not necessarily understand the meaning behind a query. A common lexical retrieval method is BM25.</p>

<h3>3. Dense and Sparse Retrieval</h3>

<ul>
<li><b>Dense Retrieval:</b> Uses dense embeddings, in which most vector values are non-zero, to retrieve information based on semantic relationships.</li>
<li><b>Sparse Retrieval:</b> Uses sparse representations, in which most values are zero and selected terms or features have non-zero weights. It is often effective for keyword-based retrieval.</li>
</ul>

<p>Dense retrieval is useful for finding conceptually related content, while sparse retrieval can be particularly useful for exact terminology. Some systems combine both approaches through hybrid search to improve retrieval quality.</p>

<h3>4. Data Classification</h3>

<p>Embeddings can represent text or other data as numerical vectors that help classification models identify categories. For example, customer feedback can be classified as positive, negative, or neutral based on its content.</p>

<p>Embeddings may be used as input features for a classifier or compared with representative examples of different classes.</p>

<h3>5. Recommendation Systems</h3>

<p>Recommendation systems can use embeddings to represent users, products, movies, or other items. By comparing these vectors, a system can identify similar items or recommend content that matches a user's interests.</p>

<p>For example, a movie recommendation system may suggest films with characteristics similar to movies a user has enjoyed previously.</p>

<h3>6. Anomaly Detection</h3>

<p>Anomaly detection identifies data points or patterns that differ significantly from expected behaviour. Embeddings can help represent data so that unusual items can be identified by comparing their vectors with normal patterns or clusters.</p>

<p>For example, an anomaly detection system may identify unusual customer messages, suspicious transactions, or unexpected patterns in system logs. Embeddings are one possible approach and are not required for every anomaly detection system.</p>

<h3>Learning Summary</h3>

<p>Through these topics, I learned how embeddings convert data into numerical vectors and how those vectors can represent semantic relationships. I also studied embedding dimensions, similarity search methods, semantic and lexical search, dense and sparse retrieval, and the use of embeddings in classification, recommendation systems, and anomaly detection.</p>

<p>These concepts provide a foundation for understanding how modern AI systems retrieve relevant information and use vector representations to compare and organise data.</p>
