from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import CharacterTextSplitter
import os

load_dotenv()  # Load environment variables from .env file
print(os.environ.get("PINECONE_API_KEY"))  # P

if __name__ == "__main__":
    print("ingesting data")
    loader = TextLoader("/Users/dimpee/Desktop/langchain-projects/mediumblog1.txt")
    document = loader.load()

    print("splitting data")
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(document)
    print(f"Number of chunks: {len(texts)}")

    embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))

    print("creating vector store")
    PineconeVectorStore.from_documents(
        texts,
        embeddings,
        index_name=os.environ.get("INDEX_NAME")
    )