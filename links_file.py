from os import path


if not path.exists("links.txt"):
    with open("links.txt", "w") as file:
        file.write("")

def filter_out_existing_links(links):
    with open("links.txt", "r") as file:
        existing_links = file.read().splitlines()
        new_links = [l for l in links if l[0] not in existing_links]
    if new_links:
        with open("links.txt", "a") as file:
            file.write("\n".join([l[0] for l in new_links]) + "\n")
    return new_links