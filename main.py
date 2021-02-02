from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')

articles = soup.find_all(name='a', class_='storylink')
article_text = [article.getText() for article in articles]
article_links = [article.get('href') for article in articles]

upvotes_text = [int(upvotes.getText().split()[0]) for upvotes in soup.find_all(name='span', class_='score')]

# print(article_text)
# print(article_links)
# print(upvotes_text)

# print(int(upvotes_text[0].split()[0]))


def get_index_of_greatest_item_value(list_of_int_values):
    highest_value = max(list_of_int_values)
    index_of_highest_item_value = list_of_int_values.index(highest_value)
    return index_of_highest_item_value


print(upvotes_text)
print(get_index_of_greatest_item_value(upvotes_text))

highest_value_index = get_index_of_greatest_item_value(upvotes_text)
print(article_text[highest_value_index])
print(article_links[highest_value_index])
