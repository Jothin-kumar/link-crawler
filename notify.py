from discord_webhook import DiscordWebhook
from dotenv import load_dotenv
from os import getenv


load_dotenv()
def notify(message, url):  # TODO
    DiscordWebhook(
        url=getenv("DISCORD_WEBHOOK"),
        rate_limit_retry=True,
        content=f"{message}\n{url}",
    ).execute()