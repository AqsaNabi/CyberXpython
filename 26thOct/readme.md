<h2>Learning Retrieval-Augmented Generation (RAG)</h2>

<p>Today, I studied Retrieval-Augmented Generation (RAG), its use cases, the difference between RAG and fine-tuning, and the main steps involved in implementing a RAG pipeline.</p>

<h3>1. What Is RAG?</h3>

<p>RAG stands for Retrieval-Augmented Generation. It is a technique that combines information retrieval with a Large Language Model (LLM) to generate answers using relevant external information.</p>

<h3>2. RAG Use Cases</h3>

<p>I learned how RAG can be used in different applications, including:</p>

<ul>
<li>Question-answering systems over documents.</li>
<li>Chatbots that use company or private knowledge bases.</li>
<li>Searching and retrieving relevant information from large collections of documents.</li>
<li>Customer support systems and knowledge assistants.</li>
<li>Applications that require access to updated or specialised information.</li>
</ul>

<h3>3. RAG vs. Fine-tuning</h3>

<p>I studied the difference between RAG and fine-tuning, including their purposes and how they are implemented.</p>

<ul>
<li><b>RAG:</b> Retrieves relevant external information and provides it to the LLM as context when generating a response.</li>
<li><b>Fine-tuning:</b> Trains a pre-trained model further on selected examples to adapt its behaviour or improve performance for a specific task.</li>
</ul>

<h3>4. Implementing RAG</h3>

<p>I learned the main stages involved in building a RAG pipeline:</p>

<ul>
<li>Document loading.</li>
<li>Document chunking.</li>
<li>Generating embeddings.</li>
<li>Storing vectors in a vector database.</li>
<li>Retrieving relevant chunks for a user query.</li>
<li>Constructing an augmented prompt.</li>
<li>Generating the final answer using an LLM.</li>
</ul>

<h3>5. Chunking and Types of Chunking</h3>

<p>I learned about chunking, which involves dividing large documents into smaller sections so they can be processed, embedded, and retrieved more effectively.</p>

<p>The chunking methods I studied included:</p>

<ul>
<li><b>Fixed-size chunking:</b> Splits text into chunks based on a specified size.</li>
<li><b>Sentence-based chunking:</b> Divides text according to sentence boundaries.</li>
<li><b>Paragraph-based chunking:</b> Uses paragraphs as individual chunks.</li>
<li><b>Recursive character chunking:</b> Splits text using a hierarchy of separators to preserve structure where possible.</li>
<li><b>Semantic chunking:</b> Groups text according to changes in meaning or semantic similarity.</li>
<li><b>Document-structure-based chunking:</b> Uses headings, sections, or other structural elements to divide documents.</li>
</ul>

<h3>6. Embeddings</h3>

<p>I learned what embeddings are and how they represent text as numerical vectors that capture useful semantic relationships. These vectors allow an AI system to compare text and find information with similar meanings.</p>

<h3>7. Vector Database and Retrieval Process</h3>

<p>I studied how vector databases store embeddings and associated information, and how they retrieve relevant document chunks using similarity search.</p>

<ul>
<li>Document chunks are converted into vectors using an embedding model.</li>
<li>The vectors and associated content are stored in a vector database or search index.</li>
<li>A user's query is converted into a vector.</li>
<li>The system retrieves the most relevant chunks by comparing the query with stored vectors.</li>
<li>The retrieved information is passed to the LLM as context.</li>
</ul>

<h3>8. Generation</h3>

<p>I learned how the generation stage uses the user's query and retrieved context to construct an augmented prompt. The LLM then generates a response based on the supplied information and its learned capabilities.</p>

<h3>Learning Summary</h3>

<p>Through these topics, I learned the fundamental components of a RAG pipeline, including document processing, chunking, embeddings, vector storage, retrieval, and response generation. I also explored RAG use cases and its differences from fine-tuning.</p>