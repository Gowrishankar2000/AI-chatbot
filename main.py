from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM
import streamlit as st

st.title('AI chatbot')
input_txt=st.text_input('Enter your queries:')

prompt=ChatPromptTemplate.from_messages(
    [('system', 'you are a helpful AI assistent.'),
     ('human:{query}')]
)

llm=OllamaLLM(model='llama2')
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_txt:
    st.write(chain.invoke({'query': input_txt}))

