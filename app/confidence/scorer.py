import numpy as np
import re


class ConfidenceScorer:

    def __init__(self, similarity_threshold=0.3):
        self.similarity_threshold = similarity_threshold

    def keyword_overlap(self, query, documents):
        query_tokens = set(re.findall(r"\w+", query.lower()))
        doc_tokens = set()

        for doc in documents:
            doc_tokens.update(
                re.findall(r"\w+", doc.page_content.lower())
            )

        overlap = query_tokens.intersection(doc_tokens)
        if len(query_tokens) == 0:
            return 0

        return len(overlap) / len(query_tokens)


    def compute_confidence(self, query, documents):

        keyword_score = self.keyword_overlap(query, documents)

        if keyword_score < 0.2:
            return "Low", keyword_score
        elif keyword_score < 0.5:
            return "Medium", keyword_score
        else:
            return "High", keyword_score