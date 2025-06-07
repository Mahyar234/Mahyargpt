import telebot
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"
openai.organization = ""  # خالی بمونه
openai.api_type = "open_ai"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

@bot.message_handler(commands=['ask'])
def handle_ask_command(message):
    user_input = message.text.replace('/ask', '').strip()
    if not user_input:
        bot.reply_to(message, "❗ لطفاً بعد از /ask سوالتو بپرس.")
        return

    try:
        model="openrouter/openai/gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "شما یک دستیار هوشمند هستید که به فارسی و انگلیسی پاسخ می‌دهید."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response['choices'][0]['message']['content']
        bot.reply_to(message, reply)
    except Exception as e:
        bot.reply_to(message, f"⚠️ خطا: {str(e)}")

print("🤖 ربات در حال اجراست...")
bot.polling()
