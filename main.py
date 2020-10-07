
import telebot # pip install pyTelegramBotAPI
import redis # pip install redis

bot = telebot.TeleBot("Insira o token aqui")


# r = redis.Redis(
#     host='127.0.0.1',
#     port=6379, 
# )


bot.state = None # create own value `.state` in `bot` - so I don't have to use `global state`. Similar way I could create and use `bot.data`

CRIAR = 1
TAREFAS = 2
DONE = 3


@bot.message_handler(commands=['criar'])
def criar(message):
    bot.send_message(message.chat.id, 'Por favor digite sua tarefa:')
    bot.state = CRIAR


@bot.message_handler(func=lambda msg:bot.state==CRIAR)
def criar_tarefa(message):
    chat_id = message.chat.id
    teste = r.hgetall(chat_id)
    r.hset(chat_id, message.text,'a')

    bot.send_message(message.chat.id,'Tarefa criada com sucesso!')
    bot.state = None
        
bot.polling()


