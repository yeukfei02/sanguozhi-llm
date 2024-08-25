from fastapi import Request, status
from fastapi.responses import JSONResponse
from src.ollama.db.db import get_collection, get_data
from src.ollama.sanguozhi_ollama import ollama_embedding, ollama_generate


def sanguozhi_data_controller(request: Request):
    data = {
        "message": "sanguozhi-data",
        "result": {}
    }

    query_params = request.query_params
    if query_params:
        embedding_result = get_data_by_ollama_embedding_and_vector_db(
            query_params)
        print(f"embedding_result = {embedding_result}")

        generated_text = ""

        search_text = request.query_params.get('search_text')
        documents = embedding_result.get('documents')
        if search_text and documents:
            for document in documents:
                prompt = f"Using this data: {document}. Respond to this prompt with Chinese: {search_text}"
                generated_result = ollama_generate(
                    'digimonster/llama3-chinese-response', prompt)
                print(f"generated_result = {generated_result}")

                generated_text += generated_result

        data = {
            "message": "sanguozhi-data",
            "result": generated_text,
            "embedding_result": embedding_result
        }

    response = JSONResponse(status_code=status.HTTP_200_OK, content=data)
    return response


def get_data_by_ollama_embedding_and_vector_db(query_params):
    collection = get_collection()

    search_text = query_params.get('search_text')
    print(f"search_text = {search_text}")

    number_of_results = query_params.get('number_of_results')
    print(f"number_of_results = {number_of_results}")

    second_name = query_params.get('second_name')
    print(f"second_name = {second_name}")

    sex = query_params.get('sex')
    print(f"sex = {sex}")

    parents = query_params.get('parents')
    print(f"parents = {parents}")

    leadership = query_params.get('leadership')
    print(f"leadership = {leadership}")

    force = query_params.get('force')
    print(f"force = {force}")

    intelligence = query_params.get('intelligence')
    print(f"intelligence = {intelligence}")

    politics = query_params.get('politics')
    print(f"politics = {politics}")

    charm = query_params.get('charm')
    print(f"charm = {charm}")

    metadata_filter_list = []

    if second_name:
        data = {
            "字": {
                "$in": [second_name]
            },
        }
        metadata_filter_list.append(data)
    if sex:
        data = {
            "性別": {
                "$in": [sex]
            },
        }
        metadata_filter_list.append(data)
    if parents:
        data = {
            "父母": {
                "$in": [parents]
            },
        }
        metadata_filter_list.append(data)
    if leadership:
        data = {
            "統率": {
                "$gte": int(leadership)
            },
        }
        metadata_filter_list.append(data)
    if force:
        data = {
            "武力": {
                "$gte": int(force)
            },
        }
        metadata_filter_list.append(data)
    if intelligence:
        data = {
            "智力": {
                "$gte": int(intelligence)
            },
        }
        metadata_filter_list.append(data)
    if politics:
        data = {
            "政治": {
                "$gte": int(politics)
            },
        }
        metadata_filter_list.append(data)
    if charm:
        data = {
            "魅力": {
                "$gte": int(charm)
            },
        }
        metadata_filter_list.append(data)

    number_of_results = int(number_of_results)

    embeddings_data = ollama_embedding("shaw/dmeta-embedding-zh", search_text)

    metadata_filter = {}
    if metadata_filter_list:
        if len(metadata_filter_list) > 1:
            metadata_filter = {
                "$and": metadata_filter_list
            }
        elif len(metadata_filter_list) == 1:
            metadata_filter = metadata_filter_list[0]

    result = get_data(
        collection,
        query_embeddings=embeddings_data,
        n_results=number_of_results,
        metadata_filter=metadata_filter
    )
    return result
