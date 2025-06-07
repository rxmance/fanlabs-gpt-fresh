from sentence_transformers import SentenceTransformer

def search_index(query, index, metadata, top_k=5):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_embedding = model.encode([query])
    D, I = index.search(query_embedding, top_k)

    results = []
    for i in I[0]:
        if i < len(metadata):
            results.append(metadata[i])
    return results