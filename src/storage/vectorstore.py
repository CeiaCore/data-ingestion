from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from qdrant_client.models import PointStruct
import uuid


class VectorStore:
    def __init__(self, host="localhost", port=6333):
        self.client = QdrantClient(f"http://{host}:{port}")
        print("VectorStore initialized")

    def create_collection(self, collection_name: str, vector_dimension=4, similarity_method="cosine"):
        similarity_map = {
            "dot": Distance.DOT,
            "euclidian": Distance.EUCLID,
            "cosine": Distance.COSINE,
            "manhattan": Distance.MANHATTAN,
        }

        self.client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=vector_dimension, distance=similarity_map[similarity_method]),
        )

    @staticmethod
    def insert_vectors(self, collection_name: str, vectors: list):
        operation_info = self.client.upsert(
            collection_name=collection_name,
            wait=True, # o que esse parâmetro faz?
            points=vectors # { id, vector, payload }
        )

        print(operation_info)

    def insert_chunks_with_embedding_and_metadata(self, collection_name: str, chunks):
        vectors = [{
            "id": chunk.get("id", str(uuid.uuid4())), # será que é melhor remover o uuid e deixar o qdrant gerar?
            "vector": chunk["embedding"],
            "payload": chunk["metadata"]
        } for chunk in chunks]

        self.insert_vectors(collection_name, vectors)