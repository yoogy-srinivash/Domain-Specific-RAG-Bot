import gradio as gr
from app.retrieval.retrieval_pipeline import RetrievalPipeline
from app.generation.generator import AnswerGenerator


# Initialize once (important for performance)
retriever = RetrievalPipeline()
generator = AnswerGenerator()


def rag_chat(query):

    if not query.strip():
        return "Please enter a question."

    # Step 1: Retrieve documents
    documents = retriever.run(query)

    # Step 2: Generate grounded answer
    answer = generator.generate(query, documents)

    return answer


with gr.Blocks(title="Domain-Specific RAG Bot") as demo:

    gr.Markdown("# 📚 Production-Ready Domain-Specific RAG Bot")
    gr.Markdown("Ask questions related to the ingested AI/Git documents.")

    with gr.Row():
        query_input = gr.Textbox(
            label="Enter your question",
            placeholder="e.g., What is Git?",
            lines=2
        )

    submit_button = gr.Button("Submit")

    output_box = gr.Textbox(
        label="Answer",
        lines=20
    )

    submit_button.click(
        fn=rag_chat,
        inputs=query_input,
        outputs=output_box
    )

    query_input.submit(
        fn=rag_chat,
        inputs=query_input,
        outputs=output_box
    )


if __name__ == "__main__":
    demo.launch()