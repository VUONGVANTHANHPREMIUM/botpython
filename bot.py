from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Token của bot (thay bằng token bạn nhận từ BotFather)
TOKEN = "8065098811:AAFBH8eNSdvXc3MzKNBQ9JjnGxZlbnsBXeg"

# Hàm xử lý lệnh /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm a simple bot.")

# Hàm xử lý tin nhắn văn bản
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

def main():
    # Tạo ứng dụng bot
    app = Application.builder().token(TOKEN).build()

    # Thêm handler cho lệnh /start
    app.add_handler(CommandHandler("start", start))

    # Thêm handler cho tin nhắn văn bản (không phải lệnh)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Bắt đầu bot
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
