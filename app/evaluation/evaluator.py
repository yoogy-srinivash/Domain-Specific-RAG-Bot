import json
from app.retrieval.retrieval_pipeline import RetrievalPipeline
from app.generation.generator import AnswerGenerator
from app.generation.ollama_llm import load_llm


class Evaluator:

    def __init__(self):
        self.retriever = RetrievalPipeline()
        self.generator = AnswerGenerator()
        self.llm = load_llm()

    def direct_llm(self, query):
        return self.llm.invoke(query)

    def rag_answer(self, query):
        docs = self.retriever.run(query)
        return self.generator.generate(query, docs)

    def evaluate(self, dataset_path="data/evaluation_set.json"):

        with open(dataset_path, "r") as f:
            dataset = json.load(f)

        results = []

        for item in dataset:
            question = item["question"]
            q_type = item["type"]

            print(f"\nEvaluating: {question}")

            direct_response = self.direct_llm(question)
            rag_response = self.rag_answer(question)

            results.append({
                "question": question,
                "type": q_type,
                "direct_llm": direct_response,
                "rag_response": rag_response
            })

        return results
