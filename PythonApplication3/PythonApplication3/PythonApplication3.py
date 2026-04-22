import requests
from bs4 import BeautifulSoup
def find_my_book(website, book_i_want):
    if not website.endswith('/'):
        website = website + '/'
    current_page = "index.html"
    while current_page != "none":
        address = website + current_page
        try:
            raw_data = requests.get(address)
        except:
            return "Check the website address—it doesn't seem to work!"
        readable_page = BeautifulSoup(raw_data.content, 'html.parser')
        book_boxes = readable_page.find_all('article', class_='product_pod')
        for box in book_boxes:
            full_name = box.h3.a['title']
            if book_i_want.lower() in full_name.lower():
                price = box.find('p', class_='price_color').text
                return "'{}' costs {}.".format(full_name, price)
        next_button = readable_page.find('li', class_='next')
        if next_button:
            link = next_button.a['href']
            if "catalogue/" in link:
                current_page = link
            else:
                current_page = "catalogue/" + link
        else:
            current_page = "none" 
    return "I looked everywhere, but I couldn't find that book."
answer = "yes"
while answer == "yes":
    print("\n--- Book Scrape Website Thing ---")
    user_site = input("Website link: ")
    user_book = input("What book or keyword are you looking for: ")
    result = find_my_book(user_site, user_book)
    print(result)
    answer = input("\nSearch again? (yes/no): ").lower()
print("Bye Mr.Clarke")
