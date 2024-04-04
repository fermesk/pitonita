import telebot
import os 
from openai import OpenAI

TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)
bot = telebot.TeleBot(TELEGRAM_API_KEY)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hola chicos, I'm pitonita! I generate python code. enter your prompt i will give you the code ")

@bot.message_handler(func=lambda message: True)
def generate_code(message):
    prompt = message.text
    if prompt:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": prompt},
                ],
                max_tokens=50,
            )
            print(response.choices[0].message.content)
            if response.choices:
                code = response.choices[0].message.content
                bot.reply_to(message, "Here's the generated code:\n" + code)
            else:
                bot.reply_to(message, "No code was generated.")
        except Exception as e:
            bot.reply_to(message, f"Error generating code: {e}")
    else:
        bot.reply_to(message, "Please provide a prompt for generating code.")

bot.polling()