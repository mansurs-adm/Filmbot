import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Logging sozlamalari
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Bot boshlash komandasi"""
    await update.message.reply_text(
        "Salom! 👋\n\n"
        "Men Filmbot. Film qidirishda yordam beraman.\n\n"
        "Dostlarga qo'yin: /help"
    )

# /help komandasi
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Yordam komandasi"""
    help_text = (
        "📽️ *Filmbot Komandalar*\n\n"
        "/start - Botni boshlash\n"
        "/help - Bu xabar\n"
        "/about - Bot haqida\n\n"
        "Film nomini yuboring - qidirib beraman!"
    )
    await update.message.reply_text(help_text, parse_mode='Markdown')

# /about komandasi
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Bot haqida ma'lumot"""
    await update.message.reply_text(
        "🎬 *Filmbot Haqida*\n\n"
        "Film qidiruv uchun maxsus bot.\n"
        "Versiya: 1.0\n\n"
        "Savollar uchun: @mansurs_adm"
    , parse_mode='Markdown')

# Oddiy xabar handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Film qidiruvi"""
    user_message = update.message.text
    await update.message.reply_text(
        f"🔍 Qidirayapman: *{user_message}*\n\n"
        "Hozircha bu funksiya tayyor emas."
    , parse_mode='Markdown')

# Asosiy funksiya
def main() -> None:
    """Bot ishlatiladi"""
    # Bot tokenini shu joyga qo'ying
    TOKEN = "YOUR_BOT_TOKEN_HERE"
    
    # Application yaratish
    application = Application.builder().token(TOKEN).build()

    # Komanda handlerlar
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about))

    # Oddiy xabar handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Bot ishini boshlash
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()