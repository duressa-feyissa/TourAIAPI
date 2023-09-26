from langchain.llms import OpenAI
from langchain.retrievers.self_query.base import SelfQueryRetriever
from langchain.chains.query_constructor.base import AttributeInfo
from langchain.schema import Document
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

import os
os.environ["OPENAI_API_KEY"]
embeddings = OpenAIEmbeddings(temperature=0.5)

vectorstore  = Chroma(persist_directory="./chroma_db", embedding_function=embeddings).as_retriever()
docs = vectorstore.get_relevant_documents("What place to visit")

document_content_description = "Brief summary of a recommended tourist attraction place"
llm = OpenAI(temperature=0)

retriever = SelfQueryRetriever.from_llm(
    llm, vectorstore, document_content_description, verbose=True
)

def get_relevant_documents(query):
    return retriever.get_relevant_documents(query)

