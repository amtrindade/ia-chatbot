import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import YoutubeLoader
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

os.environ['GROQ_API_KEY'] = api_key
os.environ['USER_AGENT'] = "Chrome/58.0.3029.110"
chat = ChatGroq(model='llama-3.1-70b-versatile')

url = 'https://www.youtube.com/watch?v=WguziPIjZXk'

loader = YoutubeLoader.from_youtube_url(url, language=['pt'])

documents_list = loader.load()

document = ''
for doc in documents_list:
    document = document + doc.page_content
    
template = ChatPromptTemplate.from_messages([
    ('system', 'Você é um assistente amigável que possui as seguintes informações para formular uma resposta: {informacoes}'),
    ('user', '{input}')
])

chain_youtube = template | chat
response = chain_youtube.invoke({'informacoes': document, 'input': 'Qual o volume de treinos em dias, quantidade e quilometragem para se correr uma maratona?'})
print(response.content)

response = chain_youtube.invoke({'informacoes': document, 'input': 'Quanto tempo para se preparar para uma maratona considerando que já corro 10 km?'})
print(response.content)


