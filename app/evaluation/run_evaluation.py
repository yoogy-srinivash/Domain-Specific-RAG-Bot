from app.evaluation.evaluator import Evaluator

def main():
    evaluator = Evaluator()
    results = evaluator.evaluate()

    for r in results:
        print("\n============================")
        print("Question:", r["question"])
        print("\n--- Direct LLM ---\n")
        print(r["direct_llm"])
        print("\n--- RAG ---\n")
        print(r["rag_response"])
        print("============================\n")


if __name__ == "__main__":
    main()