pip install -r requirements.txt

pip install "langchain==0.3.27" "langchain-core==0.3.80" "langchain-community==0.3.31" "langchain-huggingface==0.3.1" "langchain-text-splitters==0.3.11" "huggingface-hub==0.36.0" "tokenizers==0.19.1" "transformers==4.43.3" "sentence-transformers==2.7.0" "requests==2.32.5"

#################################### Understand Flow #################################################################

Understanding the worker(.py), part 2
Processing of documents: process_document function is responsible for processing the PDF documents. It uses the PyPDFLoader to load the document, splits the document into chunks using the RecursiveCharacterTextSplitter, and then creates a vector store (Chroma) from the document chunks using the language model embeddings. This vector store is then used to create a retriever interface, which is used to create a ConversationalRetrievalChain.

Document loading: The PDF document is loaded using the PyPDFLoader class, which takes the path of the document as an argument. (Todo exercise: assign PyPDFLoader(...) to loader)

Document splitting: The loaded document is split into chunks using the RecursiveCharacterTextSplitter class. The chunk_size and overlap can be specified. (Todo exercise: assign RecursiveCharacterTextSplitter(...) to text_splitter)

Vector store creation: A vector store, which is a kind of index, is created from the document chunks using the language model embeddings. This is done using the Chroma class.

Retrieval system setup: A retrieval system is set up using the vector store. This system, calls a ConversationalRetrievalChain, used to answer questions based on the document content.


Chroma (or ChromaDB) is an open-source vector database commonly used in RAG (Retrieval-Augmented Generation) applications to store and search embeddings.

```

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1024,
    chunk_overlap=64
)

```

What is RecursiveCharacterTextSplitter?

It is a text splitting strategy that tries to keep text semantically meaningful by splitting recursively using different separators.

Typically, it tries separators in this order:

Plain Text
"\n\n" # Paragraphs

"\n" # Lines

" " # Words

"" # Characters

Show more lines

Instead of cutting text blindly every 1024 characters, it first tries to split at paragraph boundaries, then line boundaries, and so on.

Understanding the Parameters
1. chunk_size=1024

This defines the maximum size of each chunk.

Python
chunk_size=1024

means:

Each chunk should contain approximately 1024 characters.
If a paragraph is larger than 1024 characters, it will be split further.

Example:

Plain Text
Document length = 5000 characters

Result:

Plain Text
Chunk 1 = 1024 chars

Chunk 2 = 1024 chars

Chunk 3 = 1024 chars

Chunk 4 = 1024 chars

Chunk 5 = remaining chars


2. chunk_overlap=64

This specifies how many characters from the end of one chunk should be repeated at the beginning of the next chunk.

Python
chunk_overlap=64

means:

Plain Text
Chunk 1

[----------------1024 chars----------------]

Chunk 2

 [64 chars overlap][---------]

#################################################

##################################################
ServerHuggingFace.py


Another option for watsonX is using HuggingFace API . 

```
def init_llm():
    global llm_hub, embeddings

    # Set up the environment variable for HuggingFace
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = "Your HuggingFace API"

    # Step 1: Create the base LLM using HuggingFaceEndpoint
    base_llm = # --> create HuggingFaceEndpoint with 
               #     repo_id="add model name",
               #     task="text-generation",
               #     huggingfacehub_api_token="add environment variable",
               #     temperature=0.1,
               #     max_new_tokens=600

    # Step 2: Wrap the base LLM with ChatHuggingFace for chat-based interaction
    llm_hub = # --> wrap the base_llm using ChatHuggingFace

    # Initialize embeddings using a pre-trained sentence-transformer model
    embeddings = # --> create HuggingFaceEmbeddings with
                  #     model_name="sentence-transformers/all-MiniLM-L6-v2",
                  #     model_kwargs={"device": DEVICE}


```

Initialize HuggingFace API key from your account with the following steps:

Go to the https://huggingface.co/
Log in to your account (or sign up free if it is your first time)
Go to Settings -> Access Tokens -> click on New Token (refer image below)
Select either read or write option and copy the token