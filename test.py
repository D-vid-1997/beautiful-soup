from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# Print the entire html document with indenting
# print(soup.prettify())

# Print the first occurrence of a particular tag
# print(soup.a)
# print(soup.p)
# print(soup.li)

# Find all of a particular tag
# all_anchor_tags = soup.find_all(name='a')
# print(all_anchor_tags)
# print(all_anchor_tags[1])

# Get the text inside a tag, or the value of a particular tag attribute (like href)
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get('href'))

# Find an item by tag and attribute
# heading = soup.find(name='h1', id='name')
# print(heading)
#
# section_heading = soup.find(name='h3', class_='heading')
# print(section_heading.getText())

# Select an item or list of items using CSS selectors
# company_url = soup.select_one(selector='p a')
# print(company_url)
#
# name = soup.select_one(selector='#name')
# print(name)
#
# headings = soup.select(selector='.heading')
# print(headings)
