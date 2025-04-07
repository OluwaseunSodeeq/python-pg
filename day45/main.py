from bs4 import BeautifulSoup

with open("./website.html", encoding="utf-8") as file:

    contents = file.read()
    print(contents)


soup = BeautifulSoup(contents, "html.parser")
print(soup)
# print(soup.title.string)

# find_all method returns a list of all matching tags

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for  tag in all_anchor_tags:
    print(f"{tag.getText()}: {tag.get("href")}")


# while find method returns the first matching tag
heading_tag = soup.find(name="h1")  
print(heading_tag)
print(heading_tag.string)


company_url = soup.select_one(selector="p a")
print(company_url)

heading_tag = soup.select_one(selector="#heading")