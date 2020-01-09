import time

import chatterbot as chatterbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from pynput.keyboard import Key, Controller
keyboard = Controller()

my_bot = ChatBot(name='PyBot', read_only=True,
                     logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                                     'chatterbot.logic.BestMatch'])

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english.conversations')


def ai_chat(msg):
    ans = my_bot.get_response(msg)
    # time.sleep(5)
    ans = str(ans) + '\n'
    keyboard.type(str(ans))
    print(ans)



