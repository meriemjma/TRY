#Why it matters: this is the first step to building an AI that answers questions about your own files.

#EASY EXAMPLE

#from langchain_community.document_loaders import PyPDFLoader

#docs = PyPDFLoader("your_file.pdf").load()
#print(docs[0].page_content) #This prints the text of page 1.

#REAL

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Load the PDF and join all pages into one text
docs = PyPDFLoader("Studienverlaufsbescheinigung.pdf").load()
text = "\n".join(doc.page_content for doc in docs)

llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash", max_retries=5)

prompt_template = PromptTemplate.from_template(
    "Answer the question using only this document:\n\n{document}\n\nQuestion: {question}"
)

# Ask questions until you type "exit"
while True:
    question = input("\nAsk a question (or 'exit'): ")
    if question == "exit":
        break
    prompt = prompt_template.invoke({"document": text, "question": question}) # filling the promt that we created at line 22
    print(llm.invoke(prompt).text)