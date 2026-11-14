import json
import os

from dotenv import load_dotenv

from deerflow.agents.memory.backends.mem0.client import Mem0Client

load_dotenv()

MEM0_BASE_URL = os.environ.get("MEM0_BASE_URL", "https://api.mem0.ai")
MEM0_API_KEY = os.environ["MEM0_API_KEY"]

print(f"{MEM0_BASE_URL=}")

USER_ID = "my_deerflow_mem_client"
AGENT_ID = "hahaha_deerflow_mem_client"
RUN_ID = "hahaha_run_xxdeg5545"

m = Mem0Client(base_url=MEM0_BASE_URL, api_key=MEM0_API_KEY)


def mem0_demo():
    messages = [{"role": "user", "content": "Hi, I'm Alex. I'm a vegetarian and I'm allergic to nuts."}, {"role": "assistant", "content": "Hello Alex! I see that you're a vegetarian with a nut allergy."}]
    query = "What can I cook for dinner tonight?"

    r = m.add_memories(messages=messages, user_id=USER_ID, agent_id=AGENT_ID, run_id=RUN_ID)
    print(json.dumps(r, indent=2))

    r = m.search_memories(query=query, filters={"user_id": USER_ID}, top_k=10, threshold=0.3)
    print(json.dumps(r, indent=2))


def mem0_ping():
    r = m.ping()
    print(json.dumps(r, indent=2))


mem0_demo()
