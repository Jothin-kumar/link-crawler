from json import loads
from crawl import crawl
from links_file import filter_out_existing_links


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
        print(new_links)
