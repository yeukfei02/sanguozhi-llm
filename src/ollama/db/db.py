import chromadb


def get_collection():
    client = chromadb.PersistentClient(path="src/ollama/db")

    heartbeat = client.heartbeat()
    print(f"heartbeat = {heartbeat}")

    collection = client.get_or_create_collection(name="sanguozhi-data")
    return collection


def add_data(collection, ids, documents, embeddings, metadatas):
    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )
    print("add data success")


def get_data(collection, query_texts=[], query_embeddings=[], n_results=1, metadata_filter={}, search_text=""):
    result = None

    if query_texts:
        where_document = {"$contains": search_text} if search_text else {}

        result = collection.query(
            query_texts=query_texts,
            n_results=n_results,
            where=metadata_filter,
            where_document=where_document
        )

    if query_embeddings:
        where_document = {"$contains": search_text} if search_text else {}

        result = collection.query(
            query_embeddings=query_embeddings,
            n_results=n_results,
            where=metadata_filter,
            where_document=where_document
        )

    return result
