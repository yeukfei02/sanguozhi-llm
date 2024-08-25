import os
import json
import uuid
import ollama
import pandas
from packages.ollama.db.db import get_collection, add_data


def sanguozhi_ollama():
    collection = get_collection()

    created_json_folder_path = create_folder()

    extract_xls_and_create_json_file(created_json_folder_path)

    read_json_file(collection, created_json_folder_path)


def create_folder():
    # create folder is not exists
    created_json_folder_path = 'packages/ollama/json/三國志十遊戲'
    if not os.path.exists(created_json_folder_path):
        os.makedirs(created_json_folder_path)

    return created_json_folder_path


def extract_xls_and_create_json_file(created_json_folder_path):
    excel_file_path = 'packages/ollama/data/excel/sanguozhi.xls'

    # name
    name_data_df = pandas.read_excel(
        excel_file_path, sheet_name='data', usecols=['姓名'])
    # print(f"name_data_df = {name_data_df}")

    # create name json file
    with open(f"{created_json_folder_path}/name_data_df.json", 'w', encoding='utf-8') as file:
        name_data_df.to_json(file, force_ascii=False)

    # second name
    second_name_data_df = pandas.read_excel(
        excel_file_path, sheet_name='data', usecols=['字'])
    # print(f"second_name_data_df = {second_name_data_df}")

    # create second name json file
    with open(f"{created_json_folder_path}/second_name_data_df.json", 'w', encoding='utf-8') as file:
        second_name_data_df.to_json(file, force_ascii=False)

    # sex
    sex_data_df = pandas.read_excel(
        excel_file_path, sheet_name='data', usecols=['性別'])
    # print(f"sex_data_df = {sex_data_df}")

    # create sex json file
    with open(f"{created_json_folder_path}/sex_data_df.json", 'w', encoding='utf-8') as file:
        sex_data_df.to_json(file, force_ascii=False)

    # parent
    parent_data_df = pandas.read_excel(
        excel_file_path, sheet_name='data', usecols=['父母'])
    # print(f"parent_data_df = {parent_data_df}")

    # create parent json file
    with open(f"{created_json_folder_path}/parent_data_df.json", 'w', encoding='utf-8') as file:
        parent_data_df.to_json(file, force_ascii=False)

    # leadership
    leadership_data_df = pandas.read_excel(
        excel_file_path, sheet_name='data', usecols=['統率'])
    # print(f"leadership_data_df = {leadership_data_df}")

    # create leadership json file
    with open(f"{created_json_folder_path}/leadership_data_df.json", 'w', encoding='utf-8') as file:
        leadership_data_df.to_json(file, force_ascii=False)

    # force
    force_data_df = pandas.read_excel(
        excel_file_path, sheet_name='data', usecols=['武力'])
    # print(f"force_data_df = {force_data_df}")

    # create force json file
    with open(f"{created_json_folder_path}/force_data_df.json", 'w', encoding='utf-8') as file:
        force_data_df.to_json(file, force_ascii=False)

    # intelligence
    intelligence_data_df = pandas.read_excel(
        excel_file_path, sheet_name='data', usecols=['智力'])
    # print(f"intelligence_data_df = {intelligence_data_df}")

    # create intelligence json file
    with open(f"{created_json_folder_path}/intelligence_data_df.json", 'w', encoding='utf-8') as file:
        intelligence_data_df.to_json(file, force_ascii=False)

    # politics
    politics_data_df = pandas.read_excel(
        excel_file_path, sheet_name='data', usecols=['政治'])
    # print(f"politics_data_df = {politics_data_df}")

    # create politics json file
    with open(f"{created_json_folder_path}/politics_data_df.json", 'w', encoding='utf-8') as file:
        politics_data_df.to_json(file, force_ascii=False)

    # charm
    charm_data_df = pandas.read_excel(
        excel_file_path, sheet_name='data', usecols=['魅力'])
    # print(f"charm_data_df = {charm_data_df}")

    # create charm json file
    with open(f"{created_json_folder_path}/charm_data_df.json", 'w', encoding='utf-8') as file:
        charm_data_df.to_json(file, force_ascii=False)

    # biographies of generals
    biographies_of_generals_data_df = pandas.read_excel(
        excel_file_path, sheet_name='data', usecols=['武將列傳'])
    # print(f"biographies_of_generals_data_df = {biographies_of_generals_data_df}")

    # create biographies of generals json file
    with open(f"{created_json_folder_path}/biographies_of_generals_data_df.json", 'w', encoding='utf-8') as file:
        biographies_of_generals_data_df.to_json(file, force_ascii=False)


def read_json_file(collection, created_json_folder_path):
    ids = []
    documents = []
    embeddings = []
    metadatas = [{}] * 1071

    temp_obj = {}

    with open(f'{created_json_folder_path}/name_data_df.json') as f:
        name_data_json = json.load(f)

        names = name_data_json['姓名']
        # print(f"names = {names}")

        if names:
            for key, value in names.items():
                uuid_str = str(uuid.uuid4())

                temp_obj[key] = value

                ids.append(uuid_str)

    with open(f'{created_json_folder_path}/second_name_data_df.json') as f:
        second_name_data_json = json.load(f)

        second_names = second_name_data_json['字']
        # print(f"second_names = {second_names}")

        if second_names:
            for key, value in second_names.items():
                existing_value = temp_obj[key]

                new_value = f"{existing_value}, 字: {value if value else ""}"

                temp_obj[key] = new_value

                metadatas[int(key)] = {
                    "字": value if value else ""
                }

    with open(f'{created_json_folder_path}/sex_data_df.json') as f:
        sex_data_json = json.load(f)

        sex_list = sex_data_json['性別']
        # print(f"sex_list = {sex_list}")

        if sex_list:
            for key, value in sex_list.items():
                existing_value = temp_obj[key]

                new_value = f"{existing_value}, 性別: {value if value else ""}"

                temp_obj[key] = new_value

                existing_metadata = metadatas[int(key)]

                new_metadata = {
                    "性別": value if value else ""
                }

                existing_metadata.update(new_metadata)

    with open(f'{created_json_folder_path}/parent_data_df.json') as f:
        parent_data_json = json.load(f)

        parents = parent_data_json['父母']
        # print(f"parents = {parents}")

        if parents:
            for key, value in parents.items():
                existing_value = temp_obj[key]

                new_value = f"{existing_value}, 父母: {value if value else ""}"

                temp_obj[key] = new_value

                existing_metadata = metadatas[int(key)]

                new_metadata = {
                    "父母": value if value else ""
                }

                existing_metadata.update(new_metadata)

    with open(f'{created_json_folder_path}/leadership_data_df.json') as f:
        leadership_data_json = json.load(f)

        leaderships = leadership_data_json['統率']
        # print(f"leaderships = {leaderships}")

        if leaderships:
            for key, value in leaderships.items():
                existing_value = temp_obj[key]

                new_value = f"{existing_value}, 統率: {int(value) if value else ""}"

                temp_obj[key] = new_value

                existing_metadata = metadatas[int(key)]

                new_metadata = {
                    "統率": int(value) if value else ""
                }

                existing_metadata.update(new_metadata)

    with open(f'{created_json_folder_path}/force_data_df.json') as f:
        force_data_json = json.load(f)

        forces = force_data_json['武力']
        # print(f"forces = {forces}")

        if forces:
            for key, value in forces.items():
                existing_value = temp_obj[key]

                new_value = f"{existing_value}, 武力: {int(value) if value else ""}"

                temp_obj[key] = new_value

                existing_metadata = metadatas[int(key)]

                new_metadata = {
                    "武力": int(value) if value else ""
                }

                existing_metadata.update(new_metadata)

    with open(f'{created_json_folder_path}/intelligence_data_df.json') as f:
        intelligence_data_json = json.load(f)

        intelligences = intelligence_data_json['智力']
        # print(f"intelligences = {intelligences}")

        if intelligences:
            for key, value in intelligences.items():
                existing_value = temp_obj[key]

                new_value = f"{existing_value}, 智力: {int(value) if value else ""}"

                temp_obj[key] = new_value

                existing_metadata = metadatas[int(key)]

                new_metadata = {
                    "智力": int(value) if value else ""
                }

                existing_metadata.update(new_metadata)

    with open(f'{created_json_folder_path}/politics_data_df.json') as f:
        politics_data_json = json.load(f)

        politics = politics_data_json['政治']
        # print(f"politics = {politics}")

        if politics:
            for key, value in politics.items():
                existing_value = temp_obj[key]

                new_value = f"{existing_value}, 政治: {int(value) if value else ""}"

                temp_obj[key] = new_value

                existing_metadata = metadatas[int(key)]

                new_metadata = {
                    "政治": int(value) if value else ""
                }

                existing_metadata.update(new_metadata)

    with open(f'{created_json_folder_path}/charm_data_df.json') as f:
        charm_data_json = json.load(f)

        charms = charm_data_json['魅力']
        # print(f"charms = {charms}")

        if charms:
            for key, value in charms.items():
                existing_value = temp_obj[key]

                new_value = f"{existing_value}, 魅力: {int(value) if value else ""}"

                temp_obj[key] = new_value

                existing_metadata = metadatas[int(key)]

                new_metadata = {
                    "魅力": int(value) if value else ""
                }

                existing_metadata.update(new_metadata)

    with open(f'{created_json_folder_path}/biographies_of_generals_data_df.json') as f:
        biographies_of_generals_data_json = json.load(f)

        biographies_of_generals = biographies_of_generals_data_json['武將列傳']
        # print(f"biographies_of_generals = {biographies_of_generals}")

        if biographies_of_generals:
            for key, value in biographies_of_generals.items():
                existing_value = temp_obj[key]

                new_value = f"{existing_value}, 武將列傳: {value if value else ""}"

                temp_obj[key] = new_value

                existing_metadata = metadatas[int(key)]

                new_metadata = {
                    "武將列傳": value if value else ""
                }

                existing_metadata.update(new_metadata)

    # print(f"temp_obj = {temp_obj}")

    if temp_obj:
        for _, value in temp_obj.items():
            documents.append(value)

            embeddings_data = ollama_embedding(
                "shaw/dmeta-embedding-zh", value)
            embeddings.append(embeddings_data)

    json_folder_path = "packages/ollama/json/books/三國志"
    books = ['吳書', '蜀書', '魏書']
    for book in books:
        # read json file from books folder
        with open(f"{json_folder_path}/{book}/目錄.json") as f:
            table_of_contents_data_json = json.load(f)

            for chapter in table_of_contents_data_json:
                with open(f"{json_folder_path}/{book}/{chapter}.json") as json_file:
                    data = json.load(json_file)
                    # print(f"data = {data}")

                    for value in data:
                        id = str(uuid.uuid4())
                        ids.append(id)

                        documents.append(value)

                        embeddings_data = ollama_embedding(
                            "shaw/dmeta-embedding-zh", value)
                        embeddings.append(embeddings_data)

                        metadatas.append(
                            {
                                "id": id,
                                "book": book,
                                "chapter": chapter
                            }
                        )

    # print(f"ids = {ids}")
    print(f"documents = {documents}")
    # print(f"embeddings = {embeddings}")
    print(f"metadatas = {metadatas}")

    add_data(collection, ids, documents, embeddings, metadatas)


def ollama_chat(model, content):
    response = ollama.chat(
        model=model,
        messages=[
            {
                'role': 'user',
                'content': content,
            },
        ],
        options={
            'temperature': 0,
        },
    )
    content = response['message']['content']
    return content


def ollama_generate(model, prompt):
    response = ollama.generate(
        model=model,
        prompt=prompt,
        options={
            'temperature': 0,
        },
    )
    generated_result = response['response']
    return generated_result


def ollama_embedding(model, prompt):
    response = ollama.embeddings(
        model=model,
        prompt=prompt
    )
    embedding = response['embedding']
    return embedding
