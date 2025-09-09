from __future__ import annotations
from typing import List, Dict, Any
import chromadb
from chromadb.utils import embedding_functions

# Minimal RAG skeleton with ChromaDB (local). Replace embedding_fn/LLM with your choices.

class LocalRAG:
    def __init__(self, collection_name: str = "docs"):
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            embedding_function=embedding_functions.DefaultEmbeddingFunction(),
        )

    def index(self, doc_id: str, text: str, metadata: Dict[str, Any] | None = None):
        self.collection.add(ids=[doc_id], documents=[text], metadatas=[metadata or {}])

    def retrieve(self, query: str, k: int = 5):
        return self.collection.query(query_texts=[query], n_results=k)

    def answer(self, query: str) -> str:
        results = self.retrieve(query, k=5)
        # TODO: Call your LLM here with retrieved context to form an answer.
        contexts = [d for d in results.get("documents", [[]])[0]]
        return f"[DRAFT ANSWER]
Query: {query}
Context: {contexts[:2]} ..."

if __name__ == "__main__":
    rag = LocalRAG()
    rag.index("ex1", "The Eiffel Tower is in Paris.", {"source": "wiki"})
    print(rag.answer("Where is the Eiffel Tower?"))
