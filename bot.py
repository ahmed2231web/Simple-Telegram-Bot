import os
import logging
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from datetime import datetime

# Load environment variables
load_dotenv()

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Create downloads directory if it doesn't exist
DOWNLOADS_DIR = os.path.join(os.path.dirname(__file__), 'downloads')
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

# Keyboard layout
def get_keyboard():
    keyboard = [
        ['/start', '/help'],
        ['/about']
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    try:
        user = update.effective_user
        welcome_message = (
            f"👋 Hello {user.first_name}!\n\n"
            "Welcome to my Telegram Bot. Here's what I can do:\n"
            "/help - Show available commands\n"
            "/about - About this bot\n\n"
            "📸 You can also send me any image and I'll save it!"
        )
        await update.message.reply_text(welcome_message, reply_markup=get_keyboard())
    except Exception as e:
        logger.error(f"Error in start_command: {e}")
        await update.message.reply_text('An error occurred. Please try again.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /help is issued."""
    try:
        help_text = """
🤖 Available Commands:

/start - Start the bot
/help - Show this help message
/about - About this bot

📸 Features:
• Send any image and I'll save it!
• Images are stored in the downloads folder
• Each image is saved with timestamp
        """
        await update.message.reply_text(help_text, reply_markup=get_keyboard())
    except Exception as e:
        logger.error(f"Error in help_command: {e}")
        await update.message.reply_text('An error occurred. Please try again.')

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send information about the bot"""
    try:
        about_text = """
🤖 About This Bot

This is a simple Telegram Bot that can:
• Handle basic commands
• Download images you send
Version: 1.0
Created with ❤️ using Python
        """
        await update.message.reply_text(about_text, reply_markup=get_keyboard())
    except Exception as e:
        logger.error(f"Error in about_command: {e}")
        await update.message.reply_text('An error occurred. Please try again.')

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle photos sent by users"""
    try:
        # Get the photo with the highest resolution
        photo = update.message.photo[-1]
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"image_{timestamp}.jpg"
        file_path = os.path.join(DOWNLOADS_DIR, file_name)
        
        # Download the photo
        photo_file = await context.bot.get_file(photo.file_id)
        await photo_file.download_to_drive(file_path)
        
        # Send confirmation message
        await update.message.reply_text(
            f"✅ Image saved successfully!\n"
            f"📁 Saved as: {file_name}",
            reply_markup=get_keyboard()
        )
        
    except Exception as e:
        logger.error(f"Error in handle_photo: {e}")
        await update.message.reply_text('Failed to save the image. Please try again.')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Echo the user message."""
    try:
        await update.message.reply_text(f"You said: {update.message.text}", reply_markup=get_keyboard())
    except Exception as e:
        logger.error(f"Error in echo: {e}")
        await update.message.reply_text('An error occurred. Please try again.')

def main():
    """Start the bot."""
    try:
        # Create the Application
        application = Application.builder().token(os.getenv('BOT_TOKEN')).build()

        # Add command handlers
        application.add_handler(CommandHandler("start", start_command))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CommandHandler("about", about_command))
        
        # Add photo handler
        application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
        
        # Add message handler
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

        # Start the Bot
        logger.info("Starting bot...")
        application.run_polling(allowed_updates=Update.ALL_TYPES)

    except Exception as e:
        logger.error(f"Error starting bot: {e}")

if __name__ == '__main__':
    main()
