from app.retrieval.retrieval_pipeline import RetrievalPipeline
from app.generation.generator import AnswerGenerator


def main():
    retriever = RetrievalPipeline()
    generator = AnswerGenerator()

    print("\n=== RAG SYSTEM TEST ===\n")

    while True:
        query = input("Enter your question (type 'exit' to quit): ")

        if query.lower() == "exit":
            break

        # Step 1: Retrieve + rerank
        documents = retriever.run(query)

        # Step 2: Generate answer
        answer = generator.generate(query, documents)

        print("\n--- ANSWER ---\n")
        print(answer)
        print("\n========================\n")   


if __name__ == "__main__":
    main()
