from langchain_google_genai import ChatGoogleGenerativeAI
#the new part 
from langchain_core.prompts import PromptTemplate

llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash", max_retries=5)

#the new part
promt_template = PromptTemplate.from_template("Tell me a joke about {topic}") 
promt = promt_template.invoke({"topic": "cats"})

result = llm.invoke(promt)

print(result.text)

#written in Terminal
#to verify: echo $GOOGLE_API_KEY
#trying again
