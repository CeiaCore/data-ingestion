from langchain_openai import OpenAIEmbeddings
from langchain_google_vertexai import VertexAIEmbeddings

class Embedder:
    def __init__(self):
        print("Embedder initialized")

    def get_embedding_model_vertexai(self, model_name="text-multilingual-embedding-002"):
        embedding_model = VertexAIEmbeddings(model_name=model_name)

        return embedding_model

    def get_embedding_model_openai(self, model_name="text-embedding-3-small"):
        embedding_model = OpenAIEmbeddings(model=model_name)

        return embedding_model

    def get_embedding_langchain(self, text, embedding_model):
        embedding = embedding_model.embed_query(text)

        return embedding
    