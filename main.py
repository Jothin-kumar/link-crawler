from json import loads
from crawl import crawl


with open("config.json", "r") as file:
    data = loads(file.read())
for page in data:
    for match in page["matches"]:
        for link in crawl(
            page["url"],
            startswith=match["startswith"],
            endswith=match["endswith"]
        ):
            print(link)
