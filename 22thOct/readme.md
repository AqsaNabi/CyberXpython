<h2>Learning AI, LLMs, Vector Databases, AI Agents, RAG, and Prompt Engineering</h2>

<p>Today, I studied several concepts related to Artificial Intelligence, Large Language Models (LLMs), vector databases, AI agents, Retrieval-Augmented Generation (RAG), and prompt engineering. I also learned about pre-trained models, context windows, knowledge cutoff dates, and how to select the right model for different use cases.</p>

<h3>1. Vector Databases</h3>

<p>I learned what vector databases are, how they work, and why they are useful in AI applications.</p>

<p>A vector database stores and retrieves numerical vectors called embeddings. These vectors represent information such as text, images, or other data. Vector databases can find information that is semantically similar to a query, even when the wording is different.</p>

<p><b>How a vector database works:</b></p>
<ul>
<li>Data is collected, such as documents or text.</li>
<li>An embedding model converts the data into numerical vectors.</li>
<li>The vectors and associated information are stored in the database.</li>
<li>A query is converted into a vector.</li>
<li>The database searches for similar vectors and retrieves relevant information.</li>
</ul>

<p><b>Examples of vector databases:</b> Pinecone, Weaviate, Milvus, Chroma, and PostgreSQL with the pgvector extension.</p>

<p><b>Traditional relational databases vs. vector databases:</b></p>
<ul>
<li><b>Relational databases:</b> Store structured information in tables containing rows and columns. They are commonly used for exact matches, transactions, and structured queries.</li>
<li><b>Vector databases:</b> Store embeddings and support similarity searches based on relationships between vectors.</li>
</ul>

<p>Relational databases are useful for structured records, while vector databases are especially useful for semantic search, recommendation systems, and retrieval-based AI applications. Some databases can support both types of operations.</p>

<h3>2. AI Agents</h3>

<p>I learned what AI agents are and how they differ from ordinary chatbots.</p>

<p>An AI agent is a system that uses an AI model to interpret a goal, decide what to do, and take actions using available tools or other resources.</p>

<p><b>Ordinary chatbots vs. AI agents:</b></p>
<ul>
<li><b>Ordinary chatbots:</b> Mainly respond to user messages and answer questions.</li>
<li><b>AI agents:</b> Can plan steps, use tools, observe results, and perform multiple actions to work toward a goal.</li>
</ul>

<p><b>How an LLM-based agent works:</b></p>
<ul>
<li>The user provides a goal or request.</li>
<li>The agent interprets the request.</li>
<li>The agent selects a suitable tool or action when needed.</li>
<li>The tool performs the action and returns a result.</li>
<li>The agent observes the result and decides whether another step is needed.</li>
<li>The agent provides a response to the user.</li>
</ul>

<p><b>Main components of an AI agent:</b></p>
<ul>
<li><b>Instructions:</b> Define the agent's role, goals, and expected behaviour.</li>
<li><b>Tools:</b> Allow the agent to interact with external systems, APIs, databases, or other services.</li>
<li><b>State:</b> Holds relevant information about the current task and progress.</li>
<li><b>Planning and Control:</b> Help the agent determine and manage the steps required to complete a task.</li>
<li><b>Guardrails and Permissions:</b> Set boundaries on what the agent can do and which actions or resources it is allowed to access.</li>
</ul>

<p><b>Types of AI agents I studied:</b></p>
<ul>
<li><b>Tool-using agents:</b> Use tools such as search engines, calculators, APIs, or databases to complete tasks.</li>
<li><b>Planning agents:</b> Break complex goals into smaller steps and organise actions before or during execution.</li>
<li><b>Multi-agent systems:</b> Use multiple agents that can collaborate or divide work among themselves.</li>
<li><b>Reactive agents:</b> Respond to current inputs or environmental changes using predefined rules or learned policies, without necessarily building a long-term plan.</li>
</ul>

<h3>3. Retrieval-Augmented Generation (RAG)</h3>

<p>I learned what Retrieval-Augmented Generation is, how it works, why it is used, and how it differs from fine-tuning.</p>

<p>RAG is a technique that combines information retrieval with text generation. It retrieves relevant information from an external knowledge source and provides that information to an LLM as context for generating an answer.</p>

<p><b>Why RAG is used:</b></p>
<ul>
<li>To provide relevant information from external documents.</li>
<li>To answer questions using private or organisation-specific information.</li>
<li>To make use of updated information without retraining the entire model.</li>
<li>To help ground answers in retrieved sources and reduce some types of hallucination.</li>
</ul>

<p><b>Part A: Preparing and Indexing Documents</b></p>
<ul>
<li>Documents are collected from relevant sources.</li>
<li>The documents are divided into smaller sections called chunks.</li>
<li>An embedding model converts the chunks into numerical vectors.</li>
<li>The vectors and associated text are stored in a vector database or another search index.</li>
</ul>

<p><b>Part B: Answering a User's Question</b></p>
<ul>
<li>The user submits a question.</li>
<li>The system searches for and retrieves relevant chunks.</li>
<li>The retrieved information is added to the prompt as context.</li>
<li>The LLM uses the question and retrieved context to generate an answer.</li>
</ul>

<p><b>RAG vs. fine-tuning:</b></p>
<ul>
<li><b>RAG:</b> Retrieves relevant information and supplies it to the model when answering a question. The model's parameters do not need to be changed.</li>
<li><b>Fine-tuning:</b> Further trains a model on selected examples to adapt its behaviour, style, or performance for a particular task.</li>
</ul>

<p>RAG is particularly useful when an application needs access to changing or specialised information. Fine-tuning is useful when the model needs to learn a more consistent task-specific behaviour. They can also be used together.</p>

<h3>4. How LLMs Generate Responses</h3>

<p>I studied the basic process through which a Large Language Model processes an input and generates a response.</p>

<ul>
<li><b>User Prompt:</b> The user provides a question or instruction.</li>
<li><b>Tokenization:</b> The input text is divided into tokens, which may be words, word fragments, or other text units.</li>
<li><b>Embedding:</b> Tokens are converted into numerical vector representations.</li>
<li><b>Positional Information:</b> Information about token order is incorporated so the model can process sequence relationships.</li>
<li><b>Transformer:</b> Transformer layers process token representations using mechanisms such as attention and feed-forward networks.</li>
<li><b>Probability Calculation:</b> The model calculates scores and probabilities for possible next tokens.</li>
<li><b>Token Selection:</b> A next token is selected using the model's decoding strategy.</li>
<li><b>Text Generation:</b> The process repeats until the model generates an ending token or reaches a stopping limit.</li>
</ul>

<p>This process allows LLMs to generate responses one token at a time based on the input and the tokens generated so far.</p>

<h3>5. Pre-trained Models</h3>

<p>I learned what pre-trained models are, why they are used, and how the pre-training process works.</p>

<p>A pre-trained model is a model that has already been trained on a large dataset before being adapted or used for a particular application.</p>

<p><b>How pre-training works:</b></p>
<ul>
<li>A large training dataset is collected.</li>
<li>An initial model architecture is selected and its parameters are initialised.</li>
<li>The model is trained on the dataset using a learning objective.</li>
<li>The model's parameters are updated during training.</li>
<li>The resulting pre-trained model can be used directly or adapted for other tasks.</li>
</ul>

<p><b>Common ways to use pre-trained models:</b></p>
<ul>
<li><b>Use directly:</b> Use the model for tasks it already supports, such as text generation or summarisation.</li>
<li><b>Use with RAG:</b> Supply retrieved information to the model as additional context.</li>
<li><b>Fine-tune:</b> Train the model further on task-specific examples to adapt its behaviour.</li>
</ul>

<p><b>Pre-trained models vs. fine-tuned models:</b></p>
<ul>
<li><b>Pre-trained model:</b> Has learned general patterns during its initial training.</li>
<li><b>Fine-tuned model:</b> Has undergone additional training to improve its performance or behaviour for a particular task or domain.</li>
</ul>

<p><b>Benefits of pre-trained models:</b></p>
<ul>
<li>Reduce the need to train a model from scratch.</li>
<li>Lower development effort and potentially reduce training costs.</li>
<li>Speed up AI application development.</li>
<li>Support transfer learning, where previously learned representations help with another task.</li>
<li>Provide broad capabilities across different types of tasks.</li>
</ul>

<p><b>Limitations of pre-trained models:</b></p>
<ul>
<li><b>Hallucination:</b> May generate incorrect or unsupported information.</li>
<li><b>Outdated Knowledge:</b> May not know about events after its training data or knowledge cutoff.</li>
<li><b>Bias:</b> May reproduce biases found in its training data.</li>
<li><b>Limited Context:</b> Can process only a limited amount of information within its context window.</li>
<li><b>Cost and Latency:</b> Inference can require computing resources and take time.</li>
<li><b>Privacy and Security:</b> Sensitive information must be protected when using models and connected services.</li>
</ul>

<h3>6. Context Windows</h3>

<p>I learned about context windows and how they determine how much information a model can process for a particular request.</p>

<p>The context may include system instructions, the user's current message, relevant conversation history, retrieved documents, and tool results. Depending on the model and system, generated output also uses the available context capacity.</p>

<p>Context windows are measured in tokens rather than simply in words or characters. A larger context window can accommodate more information, but the quality of the response still depends on how relevant and useful that information is.</p>

<h3>7. Knowledge Cutoff Dates</h3>

<p>I learned that a knowledge cutoff date indicates the approximate limit of the information available from a model's training. It does not necessarily mean that the model knows every fact published before that date.</p>

<p>Information about newer events may need to be supplied through web search, external tools, updated documents, or RAG. The ability to access current information depends on the tools and data sources connected to the system.</p>

<h3>8. Selecting the Right Model for Different Use Cases</h3>

<p>I learned that model selection should begin by identifying the type of task, such as text generation, coding, summarisation, question answering, classification, or complex reasoning.</p>

<p>After identifying the task, I studied the following factors for choosing an appropriate model:</p>

<ul>
<li><b>Capabilities:</b> Whether the model can perform the required task.</li>
<li><b>Cost:</b> The expense of using, training, or deploying the model.</li>
<li><b>Latency:</b> How quickly the model responds.</li>
<li><b>Context Window:</b> How much information the model can process in one request.</li>
<li><b>Output Quality:</b> The accuracy, relevance, and usefulness of the generated response.</li>
<li><b>Deployment:</b> Whether the model can run in the required cloud, local, or private environment.</li>
<li><b>Reliability:</b> How consistently the model performs under expected conditions.</li>
<li><b>Tool Support:</b> Whether the model supports required tools, APIs, or structured outputs.</li>
<li><b>Licensing:</b> Whether the model's usage terms meet the application's requirements.</li>
</ul>

<p>The best model is not always the largest or most expensive one. The choice depends on the task, performance requirements, available resources, and deployment constraints.</p>

<h3>9. Prompt Engineering</h3>

<p>I learned about prompt engineering, which involves designing and improving instructions given to an LLM to obtain more useful, relevant, and consistent responses.</p>

<p><b>Important elements of a prompt:</b></p>
<ul>
<li><b>Instruction:</b> Clearly states what the model should do.</li>
<li><b>Context:</b> Provides background information needed for the task.</li>
<li><b>Input Data:</b> Supplies the text, question, or information to process.</li>
<li><b>Constraints:</b> Defines limits, rules, or requirements.</li>
<li><b>Output Format:</b> Specifies how the answer should be presented.</li>
</ul>

<p><b>Common prompting approaches:</b></p>
<ul>
<li><b>Zero-shot prompting:</b> Gives the model a task without providing examples.</li>
<li><b>Few-shot prompting:</b> Provides a few examples to demonstrate the expected output.</li>
<li><b>Role-based prompting:</b> Gives the model a role or perspective to guide its response.</li>
<li><b>Structured prompting:</b> Organises instructions, context, and output requirements into clear sections.</li>
</ul>

<p>Clear prompts help reduce ambiguity and guide the model toward the desired result. However, prompt engineering alone cannot guarantee factual accuracy.</p>

<h3>10. Learning Summary</h3>

<p>Through these topics, I developed an understanding of how vector databases support similarity search, how AI agents use tools to work toward goals, and how RAG connects external information with LLM-generated answers. I also studied the response-generation process of LLMs, pre-trained models and their limitations, context windows, knowledge cutoff dates, model selection, and prompt engineering.</p>

<p>These concepts form a foundation for understanding and building modern AI applications that combine language models, retrieval systems, external tools, and structured instructions.</p>
