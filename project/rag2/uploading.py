from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore  
from langchain_community.document_loaders import UnstructuredHTMLLoader



loader =  UnstructuredHTMLLoader("htmldoc.html")
pages = loader.load_and_split()

print(pages[0])

embeddings = OllamaEmbeddings(model="llama3.2")


url = "https://f5f1874c-aee6-4fca-891e-479ec4387246.eu-central-1-0.aws.cloud.qdrant.io:6333"
api_key = "P7hXD8Rn2DCed1Ntm7VJY4ZoQLC2dox4ag7Bx4ep2iS79WqBZZ0FZQ"
qdrant = QdrantVectorStore.from_documents(
    pages,
    embeddings,
    url=url,
    prefer_grpc=True,
    api_key=api_key,
    collection_name="5a9fb436a3674693b3d146d54acadaea",
)

