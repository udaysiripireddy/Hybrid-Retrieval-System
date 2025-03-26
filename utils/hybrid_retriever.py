import numpy as np
from rank_bm25 import BM25Okapi
from models.bert_model import load_bert_model
from sentence_transformers import util

# Sample documents
documents = [
    "What is the eligibility criteria for the challenge?",
    "How do I submit my solution?",
    "What is the deadline for the submission?",
    "How is my submission evaluated?",
    "Can I participate in multiple challenges?"
]

# Preprocessing documents
tokenized_docs = [doc.lower().split() for doc in documents]

# Initialize BM25
bm25 = BM25Okapi(tokenized_docs)

# Load BERT model
bert_model = load_bert_model()
doc_embeddings = bert_model.encode(documents, convert_to_tensor=True)

# Hybrid Retrieval Function
def hybrid_retrieval(query, top_k=3, bm25_weight=0.5):
    tokenized_query = query.lower().split()
    bm25_scores = bm25.get_scores(tokenized_query)
    top_n_bm25 = np.argsort(bm25_scores)[::-1][:top_k]

    query_embedding = bert_model.encode(query, convert_to_tensor=True)
    bert_scores = util.pytorch_cos_sim(query_embedding, doc_embeddings)[0].cpu().numpy()

    hybrid_scores = bm25_weight * bm25_scores + (1 - bm25_weight) * bert_scores
    top_n_hybrid = np.argsort(hybrid_scores)[::-1][:top_k]

    results = [(documents[i], hybrid_scores[i]) for i in top_n_hybrid]
    return results
