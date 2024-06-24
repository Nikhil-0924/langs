import os
import cohere
from dotenv import load_dotenv
from langchain_cohere import ChatCohere
load_dotenv()
COHERE_API_KEY = os.getenv('COHERE_API_KEY')
cohere_llm =ChatCohere(cohere_api_key=COHERE_API_KEY)
cohere_llm = ChatCohere(
    model="command",
    max_tokens=256,
    temperature=0.75, 
    cohere_api_key=COHERE_API_KEY)
response=cohere_llm.invoke('Write a title for a blog post about API design. Only output the title text.')
 
print(response)
