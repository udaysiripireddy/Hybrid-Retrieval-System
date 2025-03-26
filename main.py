from utils.hybrid_retriever import hybrid_retrieval

# Sample queries
queries = [
    "What are the rules for participating?",
    "When should I send my project?"
]

# Run hybrid retrieval for each query
for query in queries:
    results = hybrid_retrieval(query)
    print(f"\nQuery: {query}")
    for doc, score in results:
        print(f"- {doc} (Score: {score:.4f})")
