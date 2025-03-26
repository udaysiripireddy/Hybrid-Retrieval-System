📚 BM25 + BERT Hybrid Retrieval System

This project is a **Hybrid Retrieval System** using **BM25** and **BERT** to rank documents efficiently. It combines:

- **BM25**: Lexical-based retrieval to score document relevance.
- **BERT**: Transformer-based semantic retrieval for re-ranking.



📂 Project Structure

```
/bm25_bert_hybrid_project
├── /data
│   └── sample_data.csv          # (Optional: For custom CSV data)
├── /models
│   └── bert_model.py            # Loads SentenceTransformer model
├── /utils
│   └── hybrid_retriever.py      # BM25 + BERT hybrid logic
├── main.py                      # Main script to run the project
└── requirements.txt             # Required packages
```



⚡️ Prerequisites

1. Install Python
- Download and install Python from [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Create and Activate Virtual Environment

# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on Linux/Mac
source venv/bin/activate


3. Install Required Packages
Run the following command to install dependencies:

pip install -r requirements.txt -i https://pypi.org/simple

🚀 How to Run the Project

1. Clone the Repository

git clone https://github.com/your-repo/bm25_bert_hybrid_project.git
cd bm25_bert_hybrid_project


2. Run `main.py`

python main.py
📄 Sample Data
The system uses sample FAQ-style documents. You can modify the data in `sample_data.csv` or update `documents` in `hybrid_retriever.py`.

📄 sample_data.csv

id,document
1,What is the eligibility criteria for the challenge?
2,How do I submit my solution?
3,What is the deadline for the submission?
4,How is my submission evaluated?
5,Can I participate in multiple challenges?

📝 Modifying or Extending

- **Modify documents:** Change the list in `hybrid_retriever.py`.
- **Change BERT model:** Update the model in `bert_model.py`.


🔍 Troubleshooting

1. Connection Issues
pip install -r requirements.txt -i https://pypi.org/simple

2. Model Not Downloading
If BERT model download fails, download manually from [Hugging Face Models](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2).

🤝 Contribution
Feel free to contribute and improve the project!

📧 Contact
For issues, contact **udaysiripireddy7@gmail.com**

