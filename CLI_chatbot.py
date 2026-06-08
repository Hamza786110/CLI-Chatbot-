import os
import re
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.tools import tool
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver
load_dotenv()

# model instantiation

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
model=ChatGroq(model='qwen/qwen3-32b')

agent=create_agent(
    model=model,
    system_prompt='you are a helpful in terminal chatbot which answers to the users question and always ending with a kind text of appriciation',
    checkpointer=InMemorySaver()
)

config={"configurable":{"thread_id":"testid1"}}
while True:

    query=input("Enter you query here : \n",).strip()

    if not query:
        break

    response=agent.invoke({
        "messages":
        [
            {
            "role":"user",
            "content":query
            }
        ]
    },
        config=config
    )
    output=response['messages'][-1].content
    ans = re.sub(r'<think>.*?</think>', '', output, flags=re.DOTALL).strip()
    print(ans,"\n")

        
