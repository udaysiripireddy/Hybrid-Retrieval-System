from sentence_transformers import SentenceTransformer

# Load BERT model
def load_bert_model():
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    return model
