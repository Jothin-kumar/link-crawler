from json import loads
from crawl import crawl
from links_file import filter_out_existing_links
from notify import notify


with open("config.json", "r") as file:
    data = loads(file.read())

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