from json import loads
from crawl import crawl
from links_file import filter_out_existing_links
from notify import notify
from time import sleep
from datetime import datetime


with open("config.json", "r") as file:
    data = loads(file.read())

def __main__():
    for page in data:
        for match in page["matches"]:
            new_links = filter_out_existing_links(
                [*crawl(
                    page["url"],
                    startswith=match["startswith"],
                    endswith=match["endswith"]
                )]
            )
            for link, detail in new_links:
                notify(match.get("message") or page["message"], link, detail)

if __name__ == "__main__":
    while True:
        __main__()
        print("Last checked at:", datetime.now())
        sleep(30)
