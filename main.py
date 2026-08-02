from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_text = "درود برشما، من همراه شما در طول مسیر ایمانتان هستم.چطور میتوانم به شما کمک کنم؟"
    await update.message.reply_text(message_text)

if __name__ == '__main__':
    token = '8650379209:AAFF4HDAmL-F9TME1ImdD6TEaYjd8qzemy4' 
    
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Bot is running...")
    app.run_polling()
