from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


class VectorRetriever:
    def __init__(self, persist_directory="chroma_store"):
        self.embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.db = Chroma(
            persist_directory=persist_directory,
            embedding_function=self.embedding_model
        )

    def retrieve(self, query, top_k=5, source_filter=None):

        if source_filter:
            results = self.db.similarity_search(
                query,
                k=top_k,
                filter={"source": source_filter}
            )
        else:
            results = self.db.similarity_search(query, k=top_k)

        return results
