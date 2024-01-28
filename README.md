# A.R.M.E.D. - Discord Bot
A.R.M.E.D. stands for **A**utomatic **R**eminder **M**essage **E**nabeld for **D**iscord and has the purpose to send a reminder message onto a Discord-Server, whenever a specific day in a month is reached.
E.g. this message can contain a reminder for a specific role[^1] on a server to pay for a Spotify-Family or remind everyone to drink some water.

## How To Use The Bot
### Preperation
1. Create your own Discord-Application. If you need help, look up the [docs](https://discord.com/developers/docs/intro).
2. Make sure you use Python 3.12 or higher.
3. Replace the text in the file `bot_token.txt` with your bot token. You can find it in the `resources` folder.
4. In `resources/config.json` file you can configure when the bot sends it's message and the message content itself.

### Hosting
For executing the bot, just run the `bot_main.py` file.
You can run the bot temporarly on your PC/Laptop, your own server or pay for some server online.[^2]
Here i can highliy recommend a RaspberryPi.

### Productive Use
List of commands:
- `!ping`: bot responds with "Pong!". Use this command to check if the bot is online.
- `!start`: starts a 24h loop, that is responsible for sending the automated message. Use this command when you want the bot to check every day (24h cycle), if it is time to send your message.
- `!send_manual`: bot responds with the message you configured in `config.json`. Use this command to send your message any time.

by sylvan013

[^1]: e.g. `@everyone` or `@Your cool role`
[^2]: As of January 2024 - to my knowledge - there is no real option of hosting a discord bot 24/7 for free, as long as it is not your own device.
