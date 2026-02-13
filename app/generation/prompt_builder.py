def build_prompt(query, documents):
    context = ""
    for i, doc in enumerate(documents):
        context += f"[{i+1}] {doc.page_content}\n\n"

    prompt = f"""
You are an AI assistant specialized in artificial intelligence concepts.

Use ONLY the provided context to answer the question.
If the answer is not found in the context, respond with:
"I don't know based on the provided documents."

Context:
{context}

Question:
{query}

Answer:
Include citation numbers like [1], [2] in your answer.
"""

    return prompt
