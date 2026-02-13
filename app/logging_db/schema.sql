CREATE DATABASE IF NOT EXISTS rag_logs_db;
USE rag_logs_db;

CREATE TABLE IF NOT EXISTS rag_logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT NOT NULL,
    retrieved_chunk_ids TEXT,
    answer TEXT NOT NULL,
    confidence VARCHAR(20),
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);