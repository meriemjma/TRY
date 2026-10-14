from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash", max_retries=5)
result = llm.invoke("Tell me a joke about programming")

print(result.text)

#written in Terminal
#to verify: echo $GOOGLE_API_KEY
#trying again
