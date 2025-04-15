from discord_webhook import DiscordWebhook
from dotenv import load_dotenv
from os import getenv


load_dotenv()
def notify(message, url, detail):
    DiscordWebhook(
        url=getenv("DISCORD_WEBHOOK"),
        rate_limit_retry=True,
        content=f"{message}\n[{detail}]({url})",
    ).execute()
    print(f"Notified: {message}\n{detail}\nLink: {url}")