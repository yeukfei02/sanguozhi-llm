import time
import streamlit as st
from services.sanguozhi_data_api import sanguozhi_data_api

st.title("三國志 llm")

st.write("")

search_text = st.text_area(
    label="搜尋文字",
    placeholder="輸入搜尋文字",
    height=10
)

number_of_results = st.number_input(
    label="結果數",
    placeholder="輸入結果數",
    value=10,
    min_value=1,
    max_value=10
)

st.subheader("Metadata")

second_name = st.text_input(
    label="字",
    placeholder="輸入字",
)

sex = st.selectbox(
    label="性別",
    placeholder="輸入性別",
    options=["男", "女"]
)

parents = st.text_input(
    label="父母",
    placeholder="輸入父母",
)

leadership = st.number_input(
    label="統率",
    placeholder="輸入統率",
    value=1,
    min_value=1,
    max_value=99
)

force = st.number_input(
    label="武力",
    placeholder="輸入武力",
    value=1,
    min_value=1,
    max_value=99
)

intelligence = st.number_input(
    label="智力",
    placeholder="輸入智力",
    value=1,
    min_value=1,
    max_value=99
)

politics = st.number_input(
    label="政治",
    placeholder="輸入政治",
    value=1,
    min_value=1,
    max_value=99
)

charm = st.number_input(
    label="魅力",
    placeholder="輸入魅力",
    value=1,
    min_value=1,
    max_value=99
)

submit_button_clicked = st.button("Submit", type="primary")
if submit_button_clicked:
    if search_text and number_of_results:
        print(f"search_text = {search_text}")
        print(f"number_of_results = {number_of_results}")
        print(f"second_name = {second_name}")
        print(f"sex = {sex}")
        print(f"parents = {parents}")
        print(f"leadership = {leadership}")
        print(f"force = {force}")
        print(f"intelligence = {intelligence}")
        print(f"politics = {politics}")
        print(f"charm = {charm}")

        params = {
            "search_text": search_text,
            "number_of_results": number_of_results,
        }

        if second_name:
            params["second_name"] = second_name
        if sex:
            params["sex"] = sex
        if parents:
            params["parents"] = parents
        if leadership:
            params["leadership"] = leadership
        if force:
            params["force"] = force
        if intelligence:
            params["intelligence"] = intelligence
        if politics:
            params["politics"] = politics
        if charm:
            params["charm"] = charm

        sanguozhi_data_api_response = sanguozhi_data_api(params)
        if sanguozhi_data_api_response:
            with st.spinner('Loading...'):
                time.sleep(2)

                result = sanguozhi_data_api_response['result']
                embedding_result = sanguozhi_data_api_response['embedding_result']

                st.write(f"Result: {result}")
                st.write(f"Embedding Result: {embedding_result}")
