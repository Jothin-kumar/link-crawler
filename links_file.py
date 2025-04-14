from os import path


if not path.exists("links.txt"):
    with open("links.txt", "w") as file:
        file.write("")

def filter_out_existing_links(links):
    with open("links.txt", "r") as file:
        existing_links = file.read().splitlines()
        new_links = [link for link in links if link not in existing_links]
    with open("links.txt", "a") as file:
        file.write("\n".join(new_links) + "\n")
    return new_links