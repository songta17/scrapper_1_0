from module_csv import create_csv
from module_scrapper import extract_product_data

host = "http://books.toscrape.com/"
product_url = "catalogue/sapiens-a-brief-history-of-humankind_996/index.html"

# Scrapping product data and Generation the csv
print("Data product Start!")
# SCRAPING DATA
product_data = extract_product_data(host, product_url)

# generate the csv with data result
create_csv(product_data)
print("Data product extracted!")