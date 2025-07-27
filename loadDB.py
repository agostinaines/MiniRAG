import csv
import chromadb

chroma_client = chromadb.PersistentClient()
collection_name="quotes"

try:
    chroma_client.delete_collection(collection_name)
    print(f"Colección '{collection_name}' eliminada.")
except Exception as e:
    print(f"No se pudo eliminar la colección: {e}")

collection = chroma_client.create_collection(collection_name)

documents = []
metadatas = []
ids = []

with open("quotes.csv", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for i, row in enumerate(reader):
        quote = row["quote"].strip()
        author = row["author"].strip()
        if quote and author:
            documents.append(quote)
            ids.append(f"quote_{i}")
            metadatas.append({"author": author})

if documents:
    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )
    print(f"{len(documents)} citas fueron agregadas con éxito.")
else:
    print("No hay citas válidas.")
