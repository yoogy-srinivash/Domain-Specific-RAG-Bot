from app.logging_db.db import get_connection


class QueryLogger:

    def log(self, question, documents, answer, confidence):

        conn = get_connection()
        cursor = conn.cursor()

        chunk_ids = [
            str(doc.metadata.get("chunk_id", "N/A"))
            for doc in documents
        ]

        chunk_ids_str = ",".join(chunk_ids)

        query = """
        INSERT INTO rag_logs (question, retrieved_chunk_ids, answer, confidence)
        VALUES (%s, %s, %s, %s)
        """

        values = (question, chunk_ids_str, answer, confidence)

        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()
