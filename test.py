# from bs4 import BeautifulSoup
# import requests

# with open("website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')

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

# response = requests.get('https://news.ycombinator.com/news')

# yc_webpage = response.text

# soup = BeautifulSoup(yc_webpage, 'html.parser')

# articles = soup.find_all(name='a', class_='storylink')
# article_text = [article.getText() for article in articles]
# article_links = [article.get('href') for article in articles]

# upvotes_text = [int(upvotes.getText().split()[0]) for upvotes in soup.find_all(name='span', class_='score')]

# print(article_text)
# print(article_links)
# print(upvotes_text)

# print(int(upvotes_text[0].split()[0]))


# def get_index_of_greatest_item_value(list_of_int_values):
#     highest_value = max(list_of_int_values)
#     index_of_highest_item_value = list_of_int_values.index(highest_value)
#     return index_of_highest_item_value


# print(upvotes_text)
# print(get_index_of_greatest_item_value(upvotes_text))

# highest_value_index = get_index_of_greatest_item_value(upvotes_text)
# print(article_text[highest_value_index])
# print(article_links[highest_value_index])
