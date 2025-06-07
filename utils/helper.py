import faiss
import json
import numpy as np

def load_index_and_metadata(index_path="fanlabs_vector_index.faiss", metadata_path="fanlabs_chunk_metadata.json"):
    # Load FAISS index
    index = faiss.read_index(index_path)
    
    # Load metadata
    with open(metadata_path, "r") as f:
        metadata = json.load(f)
    
    return index, metadata