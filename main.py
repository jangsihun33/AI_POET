from langchain_openai import ChatOpenAI

import openai

openai_api_key = "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"

chat_model = ChatOpenAI(openai_api_key=openai_api_key)

# subject = "AI"
# result = chat_model.invoke(subject + "에 대한 시를 써줘.")
# print(result.content)

import streamlit as st

st.title("인공지능 시인")
subject = st.text_input("시의 주제를 입력해주세요")
st.write("시의 주제 : " + subject)

if st.button("시 작성"):
    with st.spinner("시 작성 중"):
        result = chat_model.invoke( subject + "에 대한 시를 써줘")
        st.write(result.content)

