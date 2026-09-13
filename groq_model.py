import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
groq_api_key=os.getenv("GROQ_API_KEY")

llm=ChatGroq(
    api_key=groq_api_key,
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    max_tokens=None
)
llm

single_turn_prompt="Can you give sample proof for how to create a portifoilo"
print(llm.invoke(single_turn_prompt).content)