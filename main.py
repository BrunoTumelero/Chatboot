#import sys
import json
import time
import telepot
from telepot.loop import MessageLoop
from camarada import Camarada

bot = Camarada()

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    texto = bot.pega_frases(frase=msg['text'])
    resposta = bot.processa_dados(texto)
    telegram.sendMessage(chat_id, resposta)
    #if content_type == 'text':
    #    telegram.sendMessage(chat_id, msg['text'])

#TOKEN = sys.argv[1]  # get token from command-line
with open('token.json', 'r') as jf:
    TOKEN = json.load(jf)

telegram = telepot.Bot(TOKEN)
MessageLoop(telegram, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)