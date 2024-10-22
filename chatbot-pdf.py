import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

os.environ['GROQ_API_KEY'] = api_key
os.environ['USER_AGENT'] = "Chrome/58.0.3029.110"
chat = ChatGroq(model='llama-3.1-70b-versatile')

path = 'files/RoteiroViagemEgito.pdf'
loader = PyPDFLoader(path)
document_list = loader.load()

document = ''
for doc in document_list:
  document += doc.page_content

template = ChatPromptTemplate.from_messages([
    ('system', 'Você é um assistente amigável que possui as seguintes informações para formular uma resposta: {informacoes}'),    
    ('user', '{input}')
])

chain_youtube = template | chat
resposta = chain_youtube.invoke({'informacoes': document, 'input': 'Quais são as cidades previstas no roteiro? E quantos dias previstos de viagem? Onde fica o aeroporto para desembarcar e para embarcar?'})
print(resposta.content)
