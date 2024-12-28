# 🤖 TelegramImageBot

<div align="center">

![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue?style=for-the-badge&logo=telegram)
![Python](https://img.shields.io/badge/Python-3.8+-yellow?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A powerful and user-friendly Telegram bot that handles images with style! Built with Python and ❤️

</div>

## ✨ Features

🎯 **Core Functionality**
- Interactive command system with custom keyboard interface
- Seamless image handling and storage
- Real-time user interaction
- Robust error handling and logging

🛠️ **Commands**
- `/start` - Begin your journey with a friendly welcome
- `/help` - Discover all available commands
- `/about` - Learn more about the bot

📸 **Image Processing**
- High-resolution image storage
- Automatic timestamp naming
- Instant download confirmation
- Organized file management

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Telegram account
- Bot token from [@BotFather](https://t.me/botfather)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/TelegramImageBot.git
   cd TelegramImageBot
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   .\venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   - Create a `.env` file in the project root
   - Add your bot token:
     ```
     BOT_TOKEN=your_telegram_bot_token_here
     ```

5. **Launch the bot**
   ```bash
   python bot.py
   ```

## 📝 Usage

1. **Start the Bot**
   - Search for your bot on Telegram
   - Click "Start" or send `/start`
   - The bot will display a welcome message with available commands

2. **Send Images**
   - Simply send any image to the bot
   - The bot will save it with a timestamp
   - You'll receive a confirmation message

3. **Available Commands**
   - Use the custom keyboard or type commands manually
   - All commands come with helpful descriptions
   - Error messages will guide you if something goes wrong

## 🛡️ Error Handling

The bot includes comprehensive error handling:
- Graceful handling of invalid commands
- Informative error messages
- Detailed logging for debugging
- Automatic recovery from common issues

## 🔧 Technical Details

- **Framework**: python-telegram-bot
- **Storage**: Local file system with organized structure
- **Logging**: Built-in Python logging module
- **Environment**: dotenv for configuration management

## 📁 Project Structure

```
TelegramImageBot/
├── bot.py              # Main bot logic
├── .env                # Environment variables
├── requirements.txt    # Project dependencies
├── downloads/          # Image storage directory
└── README.md          # Documentation
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request


## 📬 Contact

For questions, suggestions, or issues:
- Create an issue in this repository
- Contact [@yourusername](https://github.com/yourusername) on GitHub

---
<div align="center">
Made with ❤️ by [Ahmed]
</div>
