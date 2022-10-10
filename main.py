from module_csv import create_csv, add_csv
from module_scrapper import extract_product_data, extract_categories_data

product_url = "catalogue/sapiens-a-brief-history-of-humankind_996/index.html"

# Scrapping product data and Generation the csv
print("Data product Start!")
# SCRAPING DATA
product_data = extract_product_data(product_url)

# generate the csv with data result
create_csv(product_data)
print("Data product extracted!")

url_pagination = "catalogue/category/books/mystery_3/page-1.html"
urls_category = extract_categories_data(url_pagination)

for url in urls_category:
    product_data = extract_product_data(url)
    add_csv(product_data)
