import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import YoutubeLoader
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.1-70b-versatile')

def bot_response(message_list, document):
    message_system = '''Você é um assistente amigável e descolado chamado OsvaldBot,
    Você utiliza as seguintes informações para formular as suas resposta: {information}'''    
    messages_model = [('system', message_system)]
    messages_model += message_list
    
    template = ChatPromptTemplate.from_messages(message_list)
    chain = template | chat
    return chain.invoke({'information': document}).content

def load_site():
    url_site = input('Digite a url do site: ')
    loader = WebBaseLoader(url_site)
    document_list = loader.load()
    
    document= ''
    for doc in document_list:
        document += doc.page_content    
    return document
    
def load_pdf():
    path = 'files/RoteiroViagemEgito.pdf'
    loader = PyPDFLoader(path)
    document_list = loader.load()

    document = ''
    for doc in document_list:
        document += doc.page_content
    return document
    
def load_youtube():
    url_video = input('Digite a url do vídeo no YouTube: ')
    loader = YoutubeLoader.from_youtube_url(url_video, language=['pt'])
    documents_list = loader.load()

    document = ''
    for doc in documents_list:
        document += doc.page_content
    return document

print('Bem-vindo ao ChatBot OsvalBot! (Digite x se você quiser sair!)\n')

text_option = '''
Digite 1 se você quiser conversar com um site
Digite 2 se você quiser conversar com um pdf
Digite 3 se você quiser conversar com um vídeo do YouTube:

'''

while True:
    option = input(text_option)
    if option == '1':
        document = load_site()
        break
    elif option == '2':
        document = load_pdf()
        break
    elif option == '3':
        document = load_youtube()
        break
    else:
        print('Digite um valor entre 1 e 3!')

messages = []
while True:
  question = input('Usuário: ')
  if question.lower() == 'x':
    break
  messages.append(('user', question))
  response = bot_response(messages, document)
  messages.append(('assistant', response))
  print(f'Bot: {response}')

print('\nMuito obrigado por utilizar o OsvalBot!')
