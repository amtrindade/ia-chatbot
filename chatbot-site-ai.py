import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

os.environ['GROQ_API_KEY'] = api_key
os.environ['USER_AGENT'] = "Chrome/58.0.3029.110"
chat = ChatGroq(model='llama-3.1-70b-versatile')

urls = [
    'https://targettrust.com.br',
    'https://targettrust.com.br/formacoes/testes-de-software/'
]

for url in urls:
    loader = WebBaseLoader(url)
    document_list = loader.load()

template = ChatPromptTemplate.from_messages([
    ('system', 'Você é um assistente amigável chamado OsvalBot e tem acesso as seguinte informações para dar as suas respostas: {documentos_informados}'),
    ('user', '{input}')
])

document= ''
for doc in document_list:
  document = document + doc.page_content

chain = template | chat
answer = chain.invoke({'documentos_informados': document, 'input': 'Quais as formações de treinamentos disponíveisna TargetTrust?'})
print(answer.content)

answer = chain.invoke({'documentos_informados': document, 'input': 'Quais as os módulos dos treinamentos envolvendo teste de software?'})
print(answer.content)