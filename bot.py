from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes, CommandHandler

# توکن رباتت رو اینجا بذار
BOT_TOKEN = "8029326807:AAFGmLSuSb4YKzkmnT_-bmxd8UcAvZnMow0"

# وقتی کاربر می‌نویسه /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! من یک ربات چت ساده‌ام. باهام حرف بزن 😊")

# پاسخ دادن به پیام‌های معمولی
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = f"تو گفتی: {user_message}"
    await update.message.reply_text(response)

# اجرای برنامه
if name == 'main':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # ثبت دستور start
    app.add_handler(CommandHandler("start", start))

    # ثبت پاسخ به پیام‌های متنی
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))

    print("ربات روشن شد...")
    app.run_polling()
