LangChain Libraries Used — Sequential Flow

1. PyPDFLoader (langchain_community)

Loads the uploaded PDF file and converts it into a list of Document objects — the entry point for your data.

worker.py & ServerHuggingFace.py:
```
loader = PyPDFLoader(document_path)
documents = loader.load()
```



2. RecursiveCharacterTextSplitter (langchain)

Splits the loaded document into smaller text chunks (1024 chars, 64 overlap). These chunks are passed to Chroma in the next step where they get converted into vectors.

worker.py & ServerHuggingFace.py:
```
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=64)
texts = text_splitter.split_documents(documents)
```


3. HuggingFaceEmbeddings (langchain_huggingface)

Initializes the embedding model instance using all-MiniLM-L6-v2. No conversion happens here — this simply loads the model into memory so it is ready to be used by Chroma in the next step.

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



4. Chroma (langchain_community)

Calls the embedding model (from point 3) to convert each text chunk into a numeric vector, then stores all vectors in an in-memory vector database. Exposes a retriever that fetches the most semantically relevant chunks when a question is asked.

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



