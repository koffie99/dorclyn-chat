import os
import openai
import telegram
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

#set OpenAI API key
openai.api_key = "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"

#initialize Telegram bot
bot = telegram.Bot(token="6065055791:AAHy3xq8Pwy-iR7ODx4NT7unPvkGNwiqyDI")

def generate_response(prompt):
  completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
  )

  message = completions.choices[0].text
  return message

#define a function that handles incoming messages from Telegram
def handle_message(update, context):
  text = update.message.text
  response = generate_response(text)
  chat_id = update.message.chat_id
  bot.send_message(chat_id=chat_id, text=response)

#set up the Telegram bot to listen for incoming messages
updater = Updater("6065055791:AAHy3xq8Pwy-iR7ODx4NT7unPvkGNwiqyDI", use_context=True)
dispatcher = updater.dispatcher
message_handler = MessageHandler(Filters.text, handle_message)
dispatcher.add_handler(message_handler)

#start the bot
updater.start_polling()