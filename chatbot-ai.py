import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')

os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.1-70b-versatile')

def bot_response(message_list):
  template = ChatPromptTemplate.from_messages(
      [('system', 'Você é um assistente amigável e descolado chamado OsvalBot')] +
      message_list
  )
  chain = template | chat
  return chain.invoke({}).content

print('Bem-vindo ao ChatBot OsvalBot! (Digite x se você quiser sair!)\n')
messages = []

while True:
  question = input('Usuário: ')
  if question.lower() == 'x':
    break
  messages.append(('user', question))
  response = bot_response(messages)
  messages.append(('assistant', response))
  print(f'Bot: {response}')

print('\nMuito obrigado por utilizar o OsvalBot!')
