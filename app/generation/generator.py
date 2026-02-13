from app.generation.ollama_llm import load_llm
from app.generation.prompt_builder import build_prompt
from app.confidence.scorer import ConfidenceScorer
from app.logging_db.logger import QueryLogger

class AnswerGenerator:

    def __init__(self):
        self.llm = load_llm()
        self.confidence_scorer = ConfidenceScorer()
        self.logger = QueryLogger()

    def generate(self, query, documents):

        # If no documents retrieved → immediate fallback
        if not documents:
            return (
                "I don't know based on the provided documents.\n\n"
                "Confidence: Low (0.00)"
            )

        # Build strict grounded prompt
        prompt = build_prompt(query, documents)

        # Generate response from Ollama
        response = self.llm.invoke(prompt)

        # Format references
        references = []
        for i, doc in enumerate(documents):
            source = doc.metadata.get("source", "Unknown")
            page = doc.metadata.get("page", "N/A")
            references.append(
                f"[{i+1}] {source} — Page {page}"
            )

        # Compute confidence
        confidence_level, score = self.confidence_scorer.compute_confidence(
            query,
            documents
        )

        # Fallback if low confidence
        clean_response = response.strip()

        if clean_response.lower().startswith("i don't know"):
            final_answer = "I don't know based on the provided documents."
        else:
            final_answer = (
                clean_response
                + "\n\nReferences:\n"
                + "\n".join(references)
            )

        # Append confidence
        final_answer += f"\n\nConfidence: {confidence_level} ({score:.2f})"

        self.logger.log(
            question=query,
            documents=documents,
            answer=final_answer,
            confidence=confidence_level
        )

        return final_answer