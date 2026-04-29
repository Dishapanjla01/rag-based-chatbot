from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
llm = ChatGroq(model="openai/gpt-oss-20b")
from langchain_community.utilities import GoogleSerperAPIWrapper
search = GoogleSerperAPIWrapper()
tool=[search.run]
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver
import streamlit as st

if"memory"not in st.session_state:
    st.session_state.memory = MemorySaver()
    st.session_state.history=[]


st.subheader("⚡Quickchat-Answers as you question😊")
st.title("hii")

for message in st.session_state.history:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)


agent = create_agent(
        model = llm ,
        tools=tool,
        checkpointer = st.session_state.memory,
        system_prompt="you are an amazing ai agent and you can search on google as well"
    )

print(st.session_state.memory)

query = st.chat_input("Ask Anything? ")
if query:
    st.chat_message("user").markdown(query)
    st.session_state.history.append({"role":"user","content":query})
    response= agent.invoke({"messages":[{"role":"user","content":query}]},
                        {"configurable":{"thread_id":"1"}})

    answer = response["messages"][-1].content
    st.chat_message("Ai").markdown(answer)
    st.session_state.history.append({"role":"ai","content":answer})