from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer


chatbot = ChatBot('ChatBot')
trainer = ChatterBotCorpusTrainer(chatbot)

trainer.train("chatterbot.corpus.english")

#print(chatbot.get_response("Hello"))

while True:
    question = input(">>")
    print(chatbot.get_response(Statement(text=question, search_text=question)))




