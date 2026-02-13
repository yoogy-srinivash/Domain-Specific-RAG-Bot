# Domain-Specific RAG Bot

## Overview

This project implements a **production-ready Retrieval-Augmented Generation (RAG) system** designed for domain-specific question answering.

The system:
- Ingests PDF documents
- Performs intelligent chunking with metadata
- Stores embeddings in persistent ChromaDB
- Applies retrieval + cross-encoder re-ranking
- Generates grounded answers with citations
- Computes confidence scores
- Logs queries in MySQL
- Provides an interactive Gradio UI
- Evaluates performance (Direct LLM vs RAG)

---

## System Architecture

User → Gradio UI  
→ Retriever (ChromaDB)  
→ Cross-Encoder Re-ranker  
→ Strict Prompt + Local LLM (Ollama - phi3:mini)  
→ Answer + Citations + Confidence  
→ MySQL Logging  

---

## Features

### Document Ingestion
- PDF loading
- Intelligent chunking with overlap
- Page-level metadata
- Persistent vector storage (ChromaDB)

### Retrieval Pipeline
- Top-k similarity search
- Cross-encoder re-ranking
- Metadata-aware retrieval

### Grounded Generation
- Strict context-only prompting
- Inline citation references
- Deterministic fallback logic

### Confidence Module
- Keyword overlap scoring
- Threshold-based fallback
- Confidence labeling (High / Medium / Low)

### Logging (Production Habit)
Each query stores:
- Question
- Retrieved chunk IDs
- Generated answer
- Confidence level
- Timestamp

### Evaluation
Comparison between:
- Direct LLM
- RAG System

Metrics:
- Relevance
- Faithfulness
- Hallucination rate
- Refusal accuracy

---

## Project Structure

rag_capstone/
│
├── app/
│   ├── ingestion/
│   │   ├── loader.py
│   │   ├── chunker.py
│   │   └── embedder.py
│   │
│   ├── retrieval/
│   │   ├── retriever.py
│   │   ├── reranker.py
│   │   └── retrieval_pipeline.py
│   │
│   ├── generation/
│   │   ├── ollama_llm.py
│   │   ├── prompt_builder.py
│   │   └── generator.py
│   │
│   ├── confidence/
│   │   └── scorer.py
│   │
│   ├── evaluation/
│   │   ├── evaluator.py
│   │   └── run_evaluation.py
│   │
│   ├── logging_db/
│   │   ├── db.py
│   │   ├── logger.py
│   │   └── schema.sql
│   │
│   ├── config.py
│   └── __init__.py
│
├── ui/
│   └── gradio_app.py
│
├── data/
    └── raw_data/
│   └── evaluation_set.json
│
├── chroma_store/         (ignored in git)
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env                  (ignored in git)

---

## Installation

### 1️. Clone Repository

```bash
git clone <your-repo-url>
cd rag-capstone
```

### 2. Create Virtual enviroment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️. Install & Run Ollama

Install Ollama from: https://ollama.com

```bash
#Pull model:
ollama pull phi3:mini

#Start server:
ollama serve
```
### 5. Database Setup
```bash
#Create MySQL database:
CREATE DATABASE rag_logs_db;
USE rag_logs_db;

#Run schema:
mysql -u root -p < app/logging_db/schema.sql
```

### 6. Create .env file:
```bash
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=yourpassword
MYSQL_DB=rag_logs_db
```

### 7. Run Application
```bash
python main.py
```

### Run Evaluation
```bash
python -m app.evaluation.run_evaluation
```

---

## COMPARISON TABLE 
| Metric                             | Direct LLM | RAG System |
| ---------------------------------- | ---------- | ---------- |
| In-domain Relevance                | 100%       | 100%       |
| Faithfulness (Grounded in Docs)    | 0%         | 100%       |
| Hallucination Rate (Out-of-domain) | 100%       | 0%         |
| Correct Refusal Rate               | 0%         | 100%       |
| Citation Support                   | No         | Yes        |
| Confidence Signaling               | No         | Yes        |

---

## Evalutaion
The evaluation demonstrates that while direct LLM responses maintain high relevance for in-domain questions,
they exhibit a 100% hallucination rate for out-of-domain queries. In contrast, the RAG system maintains equal
in-domain relevance while completely eliminating hallucinations by enforcing grounded retrieval and
confidence-based fallback logic. This highlights RAG's superiority in reliability and domain-constrained
deployments.

---

## Error Analysis
Error analysis reveals that while the RAG system effectively eliminates hallucinations in out-of-domain
scenarios, it remains dependent on heuristic confidence scoring and strict post-generation enforcement. Direct
LLM responses demonstrate high fluency but lack grounding, resulting in significant hallucination risk.
Hardware constraints also influenced model selection, reinforcing the importance of aligning architecture with
deployment resources.

---

## Limitations

- Small evaluation dataset (n=10)
- Heuristic confidence scoring
- No semantic citation verification
- Performance depends on embedding quality
- Limited hardware constrained model selection