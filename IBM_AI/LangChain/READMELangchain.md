LangChain Libraries Used — Sequential Flow

1. PyPDFLoader (langchain_community)

Loads the uploaded PDF file and converts it into a list of Document objects — the entry point for your data.

worker.py & ServerHuggingFace.py:
```
loader = PyPDFLoader(document_path)
documents = loader.load()
```

Loads the uploaded PDF file and converts it into a list of Document objects — the entry point for your data.

2. RecursiveCharacterTextSplitter (langchain)

Splits large documents into smaller chunks (1024 chars, 64 overlap). Ensures the LLM receives focused, digestible context rather than an entire document at once.

worker.py & ServerHuggingFace.py:
```
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=64)
texts = text_splitter.split_documents(documents)
```

Splits large documents into smaller chunks (1024 chars, 64 overlap). Ensures the LLM receives focused, digestible context rather than an entire document at once.

3. HuggingFaceEmbeddings (langchain_huggingface)

Converts each text chunk into a numeric vector using all-MiniLM-L6-v2. Enables semantic similarity search — finding chunks by meaning, not just keywords.

worker.py:

```
from langchain_community.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": DEVICE}
)
```

ServerHuggingFace.py:
```
from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": DEVICE},
)
```

Converts each text chunk into a numeric vector using all-MiniLM-L6-v2. Enables semantic similarity search — finding chunks by meaning, not just keywords.

4. Chroma (langchain_community)

Stores all the vectors in an in-memory vector database and exposes a retriever. When a question is asked, it fetches the most relevant chunks to pass to the LLM.

worker.py:
```
db = Chroma.from_documents(texts, embedding=embeddings)
retriever=db.as_retriever(search_type="mmr", search_kwargs={'k': 6, 'lambda_mult': 0.25})
```

ServerHuggingFace.py:
```
db = Chroma.from_documents(texts, embedding=embeddings)
retriever=db.as_retriever(search_kwargs={"k": 3})
```

Stores all the vectors in an in-memory vector database and exposes a retriever. When a question is asked, it fetches the most relevant chunks to pass to the LLM.

5. HuggingFaceEndpoint + ChatHuggingFace (langchain_huggingface)

HuggingFaceEndpoint connects to the hosted Llama model via the HuggingFace Inference API. ChatHuggingFace wraps it to support the chat message format expected by the chain.

ServerHuggingFace.py only — worker.py uses WatsonxLLM instead:
```
base_llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.environ["HUGGINGFACEHUB_API_TOKEN"],
    temperature=0.1,
    max_new_tokens=600,
)
llm_hub = ChatHuggingFace(llm=base_llm)
```

HuggingFaceEndpoint connects to the hosted Llama model via the HuggingFace Inference API. ChatHuggingFace wraps it to support the chat message format expected by the chain.

6. RetrievalQA (langchain)

The orchestrator — ties everything together. On each question, it retrieves relevant chunks from Chroma and feeds them alongside the question to the LLM, producing a grounded answer.

worker.py:
```
conversation_retrieval_chain = RetrievalQA.from_chain_type(
    llm=llm_hub,
    chain_type="stuff",
    retriever=db.as_retriever(search_type="mmr", search_kwargs={'k': 6, 'lambda_mult': 0.25}),
    return_source_documents=False,
    input_key="question"
)
output = conversation_retrieval_chain.invoke({"question": prompt, "chat_history": chat_history})
```

ServerHuggingFace.py:
```
conversation_retrieval_chain = RetrievalQA.from_chain_type(
    llm=llm_hub,
    chain_type="stuff",
    retriever=db.as_retriever(search_kwargs={"k": 3}),
    return_source_documents=False,
    input_key="question",
)
output = conversation_retrieval_chain.invoke({"question": prompt, "chat_history": chat_history})
```

The orchestrator — ties everything together. On each question, it retrieves relevant chunks from Chroma and feeds them alongside the question to the LLM, producing a grounded answer.

