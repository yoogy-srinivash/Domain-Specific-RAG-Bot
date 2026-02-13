from .retriever import VectorRetriever
from .reranker import CrossEncoderReranker


class RetrievalPipeline:
    def __init__(self):
        self.retriever = VectorRetriever()
        self.reranker = CrossEncoderReranker()

    def run(self, query):

        # Step 1: Retrieve
        retrieved_docs = self.retriever.retrieve(query, top_k=5)

        # Step 2: Rerank
        reranked_docs = self.reranker.rerank(
            query,
            retrieved_docs,
            top_n=3
        )

        return reranked_docs
