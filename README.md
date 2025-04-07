# DiscordBot

This project is a simple Discord bot built using the discord.py library and discord.ext.commands. It features hybrid command support (usable both as traditional prefix commands and as slash commands) and allows for dice rolling and personal greetings.

# 📦 Requirements

-Python 3.8+
-discord.py (v2.0 or higher with app_commands support)

Install the required package:

pip install -U discord.py

# ⚙️ Configuration

The bot requires an API key for authentication, which should be stored in a separate config.py file:

Example config.py:
api_key = "YOUR_DISCORD_BOT_TOKEN"
⚠️ Never expose your API key publicly.

# 🧠 Features

1. Hybrid Commands
   !greet <name>
   Sends a personalized greeting.

Usage: !greet Alice or /greet Alice

Response: Hello, Alice!

!roll <number>
Simulates a dice roll between 1 and the number provided.

Usage: !roll 20 or /roll 20

Response: You rolled a 20 and got 13! (example)

# 🛠️ Event Handling

on_ready
Triggered when the bot connects to Discord and is ready.

Syncs the bot's slash commands using bot.tree.sync()

Prints a confirmation message to the console:
We have logged in as BotUsername

# 🚀 Running the Bot

To start the bot:

python your_bot_file.py
Make sure the config.api_key is valid and your bot is added to a server with appropriate permissions (including message reading/sending and slash command usage).

# 📌 Notes

This bot uses both commands.Bot and discord.Client. For consistency and maintainability, it's generally better to use one approach—preferably commands.Bot, as used in this version.

Ensure you have registered the slash commands properly in the Discord Developer Portal.
